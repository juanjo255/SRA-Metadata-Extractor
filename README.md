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

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## Usage <a name = "usage"></a>

Add notes about how to use the system.
