import pandas as pd
from pysradb.sraweb import SRAweb

# ASSOCIATE A UNIQUE FEATURE IN THE PRUNED DATASET TO A RECORD IN THE INITIAL DATASET
# TO GET EXTRA INFORMATION
def extend_info_filt_data(base_df, ori_df, output=None):
    my_data = base_df  # pd.read_excel(created_file, index_col=0)
    data_original = ori_df  # pd.read_csv(original_file, delimiter=",")
    new_df = my_data.merge(
        data_original[["bioproject_s", "create_date_dt"]],
        right_on="bioproject_s",
        left_on="bioproject",
    )
    new_df.drop_duplicates(subset="run_accession", inplace=True)
    new_df.reset_index(drop=True, inplace=True)
    #new_df.to_excel(output)
    return new_df

# GET SRA METADATA OF FILTERED GENOMES
def get_sra_metadata(input_excel_file: str, output_file: str, original_file: str):
    db = SRAweb()
    sra = pd.read_excel(input_excel_file, index_col=0)
    data_original = pd.read_csv(original_file, delimiter=",")
    sra_list = list()
    for i in range(0, len(sra)):
        sras = (sra.loc[i, "SRA_accession"]).strip("][").split(", ")
        ## get the sra value
        for index in range(0, len(sras)):
            if "SRA" in sras[index]:
                sra_list.append(sras[index + 1].split("'")[3])
                break
    df = db.sra_metadata(sra_list)
    df = df[
        [
            "organism_name",
            "instrument",
            "instrument_model",
            "total_size",
            "run_accession",
            "bioproject",
        ]
    ]

    ## Get more info from the original dataset for every bioproject
    df = extend_info_filt_data(df, data_original)
    df["create_date_dt"] = df["create_date_dt"].apply(lambda x: x.split("-")[0])

    ## Filt for the instrument of interest
    # df = df[
    #     (df["instrument"].isin(["GridION", "MinION", "PromethION"]))
    #     & (df["total_size"].astype(int) > 0)
    # ]
    ## Get only SRAs with content
    df = df[df["total_size"].astype(int) > 0]
    df.reset_index(drop=True, inplace=True)
    df.to_excel(output_file)
    return df
