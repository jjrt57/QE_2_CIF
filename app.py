import argparse
from pymatgen.core import Structure, Lattice

def convert_qe_to_cif(input_file, output_file):
    print(f"Parsing Quantum ESPRESSO output: {input_file}...")
    
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
            
        cell_matrix = []
        species = []
        coords = []
        
        in_cell = False
        in_atoms = False
        is_cartesian = True # Default to True for 'angstrom'
        
        # Loop through the file. We overwrite our lists every time we hit a new block.
        # By the end of the file, we will naturally possess the FINAL relaxed geometry.
        for line in lines:
            # 1. Detect Cell Parameters
            if "CELL_PARAMETERS" in line:
                in_cell = True
                in_atoms = False
                cell_matrix = []
                continue
                
            # 2. Detect Atomic Positions
            if "ATOMIC_POSITIONS" in line:
                in_atoms = True
                in_cell = False
                species = []
                coords = []
                # Check if coordinates are fractional (crystal) or cartesian (angstrom/alat)
                if "crystal" in line.lower():
                    is_cartesian = False
                else:
                    is_cartesian = True
                continue
                
            stripped = line.strip()
            
            # 3. Stop reading if we hit a blank line or the end of the coordinate block
            if in_cell or in_atoms:
                if not stripped or "End final" in line or "End of" in line or "!" in line:
                    in_cell = False
                    in_atoms = False
                    continue
            
            # 4. Extract Cell Matrix Numbers
            if in_cell:
                parts = stripped.split()
                if len(parts) == 3:
                    try:
                        cell_matrix.append([float(p) for p in parts])
                    except ValueError:
                        in_cell = False 
                        
            # 5. Extract Atomic Species and Coordinates
            if in_atoms:
                parts = stripped.split()
                if len(parts) >= 4:
                    try:
                        species.append(parts[0])
                        coords.append([float(p) for p in parts[1:4]])
                    except ValueError:
                        in_atoms = False 
                        
        # Validation Check
        if len(cell_matrix) != 3:
            raise ValueError("Failed to parse a valid 3x3 CELL_PARAMETERS matrix. Is the run finished?")
        if not species or not coords:
            raise ValueError("Failed to parse ATOMIC_POSITIONS.")
            
        # 6. Build the Structure 
        lattice = Lattice(cell_matrix)
        structure = Structure(lattice, species, coords, coords_are_cartesian=is_cartesian)
        
        # 7. Export the to  CIF file
        structure.to(filename=output_file)
        
        print(f"Successfully converted {input_file} -> {output_file}")
        print(f"Final Lattice Parameters: a={structure.lattice.a:.4f} Å, b={structure.lattice.b:.4f} Å, c={structure.lattice.c:.4f} Å")
        
    except FileNotFoundError:
        print(f"Error: Could not find the file '{input_file}'.")
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Automated structural converter: Quantum ESPRESSO out -> CIF."
    )
    
    parser.add_argument("-i", "--input", required=True, help="Path to the Quantum ESPRESSO output file")
    parser.add_argument("-o", "--output", required=True, help="Name of the output CIF file to generate")
    
    args = parser.parse_args()
    convert_qe_to_cif(args.input, args.output)
