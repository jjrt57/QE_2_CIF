# QE-2-CIF: Quantum ESPRESSO to CIF Converter

A Python CLI tool to automate the conversion of Quantum ESPRESSO output files into standard Crystallographic Information Files (.cif) for materials science workflows. 

This tool leverages `pymatgen` to parse SCF convergence logs and extract the final, fully relaxed geometry into a universally readable crystallographic format.

## Features
* **Automated Extraction:** Automatically identifies and isolates the final structural geometry from verbose Quantum ESPRESSO logs.
* **CLI Integration:** Fully executable from the command line for seamless integration into high-throughput computational workflows.
* **Instant Validation:** Prints optimized lattice parameters directly to the terminal upon successful conversion.

## 📖 Instructions for Use

Follow these step-by-step instructions to set up and run the converter on your local machine.

Step 1: Clone the repository
Open your terminal and download the project files:

git clone [https://github.com/rohitnongmaithem57-lang/QE-2-CIF.git](https://github.com/rohitnongmaithem57-lang/QE-2-CIF.git)

Step 2: Navigate to the project folder:

cd QE-2-CIF

Step 3: Install the required dependencies Ensure you have Python 3.x installed, then install the required pymatgenlibrary:
pip install ase pymatgen

Step 4: Run the converter Place your Quantum ESPRESSO output file in the same folder as the script. Run the script by passing your input .out file and your desired .cif output name as arguments:
python qe2cif.py -i <input_file.out> -o <output_file.cif>

Example: python qe2cif.py -i espresso2.opt.out -o NaYF4_Iter18.cif

Terminal Output:
Parsing Quantum ESPRESSO output: espresso2.opt.out...
Successfully converted to NaYF4_Iter18.cif
Final Lattice Parameters: a=5.9600 Å, b=5.9600 Å, c=3.5300 Å
Use Case
Designed specifically for physical and computational chemists to bridge the gap between quantum mechanical simulations (Density Functional Theory) and visualization tools like VESTA, Mercury, or BURAI.
