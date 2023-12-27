import pandas as pd
from ncbi.datasets import GenomeApi as DatasetsGenomeApi
from ncbi.datasets.openapi import ApiClient as DatasetsApiClient
from tqdm import trange

# PARSE CSV FILE DOWNLOADED FROM NCBI
def parse_data(file) -> list:
    data = pd.read_csv(file, delimiter=",", low_memory=False)
    # bioprojects = list()
    # for i in range(len(data.index)):
    #     for replicon in data.loc[i,'Replicons'].split('; '):
    #         if 'mitochondrion' in replicon:
    #             bioprojects.append(data.loc[i,'BioProject'])
    bioprojects = data["bioproject_s"].to_list()
    return bioprojects

# GET DATA FROM EVERY BIOPROJECT
def get_metadata_genome_api(bioprojects) -> list:
    result = list()
    # CONNECT WITH GENOME API
    with DatasetsApiClient() as api_client:
        genome_api = DatasetsGenomeApi(api_client)
        assemblies = genome_api.assembly_descriptors_by_bioproject(bioprojects)
        assemblies_dict = assemblies.to_dict()
        if "assemblies" in assemblies_dict.keys():
            # ITER THROUGH ASSEMBLIES
            for assembly in assemblies_dict["assemblies"]:
                # CHECK THAT KEYS STORING SRA EXIST
                if "biosample" not in assembly["assembly"].keys():
                    continue
                elif "sample_ids" not in assembly["assembly"]["biosample"].keys():
                    continue
                for record in assembly["assembly"]["biosample"]["sample_ids"]:
                    if "SRA" in record.values():
                        # print (assembly["assembly"]["bioproject_lineages"])
                        # print (assembly["assembly"]["biosample"]["sample_ids"])
                        # print (assembly["assembly"]["biosample"]["description"]["organism"]["organism_name"])
                        result.append(
                            (
                                assembly["assembly"]["assembly_accession"],
                                assembly["assembly"]["bioproject_lineages"],
                                assembly["assembly"]["biosample"]["sample_ids"],
                                assembly["assembly"]["biosample"]["description"][
                                    "organism"
                                ]["organism_name"],
                            )
                        )
    return result

# GO THROUGH EVERY RECORD AND FILTER BIOPROJECTS BY SRA AVAILABILITY
def filt_data_by_sra(csv: str, output_file: str):
    print("---> FILTERING DATA BY SRA <---")
    result = list()
    data = parse_data(csv)

    # ITERATE EVERY 500 FILES SINCE API DOES NOT SUPPORT MORE THAN THAT
    for span in trange(0, len(data), 500):
        bioprojects = [i for i in data[span : span + 500] if isinstance(i, str)]
        # bioprojects = ["PRJNA48091"]
        result = result + [
            (*v, bioprojects[k])
            for k, v in enumerate(get_metadata_genome_api(bioprojects))
        ]
        # print(result)
    dataframe = pd.DataFrame(result)
    dataframe.rename(
        columns={
            0: "assembly_accesion",
            1: "bioprojects",
            2: "SRA_accession",
            3: "organism_name",
            4: "bioproject",
        },
        inplace=True,
    )
    dataframe.to_excel(output_file)
    return dataframe.head()

