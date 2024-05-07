# SRA Metadata Extractor

## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)
+ [Usage](#usage)

## About <a name = "about"></a>

This script is intended to get SRA run accessions and its metadata for every bioproject presented in a csv file.

The folder `datasets_examples/` contains examples of input and ouputs:
1. **wgs_***: These are csv examples of the input, these datasets can be retrieve from the NCBI.
2. **sra_per_bioproject**: This is an output file which is a intermediate file that contains the sra accessions for the final file.
3. **sra_metadata**: This is the final file which contains the metada from the SRA accessions, specifically the script saves the "organism_name", "instrument", "instrument_model", "total_size", "run_accession", "bioproject", plus "create_date_dt" which is retrieved from the input csv file.

## Getting Started <a name = "getting_started"></a>

### Installing
* It's encourage to use conda enviroment.
* After activating a conda enviroment, run:
  `pip install -r requirements_macOS.txt`
* or install every dependency:
  
     ```pip install pandas ncbi-datasets-pyli ncbi-datasets-pyli tqdm```

## Usage <a name = "usage"></a>

* Run `python3 main.py --help` for help message
```usage: python3 main.py [-h] [-o OUTPUT] CSVname

Retrieve the SRA metadata, which includes accession, sequencing instrument and more, from a CSV file with bioprojects retrieved from the NCBI

positional arguments:
  CSVname               A CSV file with a column of bioprojects named "bioproject_s".

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Path to save the output files. [./]

Juan Picon Cossio
```
