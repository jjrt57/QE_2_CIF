import argparse
from pymatgen.io.espresso import EspressoOut

def convert_qe_to_cif(input_file, output_file):
    """
    Parses a Quantum ESPRESSO output file and extracts the final relaxed 
    geometry into a standard Crystallographic Information File (CIF).
    """
    try:
        print(f"Parsing Quantum ESPRESSO output: {input_file}...")
        
        # Load the Quantum ESPRESSO output file
        exo = EspressoOut(input_file)
        
        # Extract the final optimized structure
        structure = exo.final_structure
        
      
        structure.to(filename=output_file)
        
        print(f"Successfully converted to {output_file}")
        print(f"Final Lattice Parameters: a={structure.lattice.a:.4f} Å, b={structure.lattice.b:.4f} Å, c={structure.lattice.c:.4f} Å")
        
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Automated structural converter: Quantum ESPRESSO out -> CIF.",
        epilog="Example usage: python qe2cif.py -i espresso2.opt.out -o NaYF4_Iter18.cif"
    )
    
    parser.add_argument("-i", "--input", required=True, help="Path to the Quantum ESPRESSO output file")
    parser.add_argument("-o", "--output", required=True, help="Name of the output CIF file to generate")
    
    args = parser.parse_args()
    
    # Run the conversion with terminal arguments
    convert_qe_to_cif(args.input, args.output)
