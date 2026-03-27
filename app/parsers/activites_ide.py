import pandas as pd 

def parse_ide_file(filepath):
    df = pd.read_excel(filepath, header=4)

    df = df.dropna(how="all")
    df.columns = [str(col).strip().lower() for col in df.columns]
    df = df.loc[:, ~df.columns.str.contains("^unnamed", na=False)]
    df = df.reset_index(drop=True)

    return df