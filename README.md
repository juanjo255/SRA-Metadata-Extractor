# get sra metadata

This script is intended to get SRA run accessions and its metadata for every bioproject presented in a csv file.

Example folder contains example of the input and the ouputs of the tool:
1. **wgs_***: These are csv examples of the input, these datasets can be retrieve from the NCBI.
2. **sra_per_bioproject**: This is an output file which is a intermediate file that contains the sra accessions for the final file.
3. **sra_metadata**: This is the final file which contains the metada from the SRA accessions, specifically the script saves the "organism_name", "instrument", "instrument_model", "total_size", "run_accession", "bioproject", plus "create_date_dt" which is retrieved from the input csv file. 
