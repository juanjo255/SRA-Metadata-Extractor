import argparse
from src import filt_data_by_sra, get_sra_metadata, analyze_dataset 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                        prog='python3 main.py',
                        description='Retrieve the SRA metadata, which includes accession, sequencing instrument and more, from a CSV file with bioprojects retrieved from the NCBI',
                        epilog='Juan Picon Cossio')
    parser.add_argument('CSVname', help='A CSV file with a column of bioprojects named "bioproject_s".')
    parser.add_argument('-o', "--output", help='Path to save the output files. [./]', default="./")
    args = parser.parse_args()

    ## AVOID PROBLEMS WITH PATH SYNTAX
    if  not (args.output).endswith("/"):
        args.output+= "/"

    filt_data_by_sra(
        args.CSVname,
        args.output + "sra_per_bioproject.xlsx",
    )
    get_sra_metadata(
        args.output + "sra_per_bioproject.xlsx",
        args.output + "sra_metadata.xlsx",
        args.output + "wgs_selector_animal.csv",
    )
    analyze_dataset(args.output + "sra_metadata.xlsx")