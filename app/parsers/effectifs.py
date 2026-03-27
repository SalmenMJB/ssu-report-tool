import pandas as pd

def parse_effectifs_file(filepath):
    df = pd.read_excel(filepath, header=3)

    df.dropna(how="all")
    df.columns = [str(col).strip().lower() for col in df.columns]
    df = df.loc[:, ~df.columns.str.contains("^unnamed", na=False)]

    #garder uniquement les VRAIES lignes établissements
    if "etablissement" in df.columns:
        df = df[df["etablissement"].notna()]
        # SUPPRIMER LES LIGNE type TOTAL / remarques
        df = df[~df["etablissement"].str.lower().str.contains("total", na=False)]
        df = df[~df["etablissement"].str.lower().str.contains("compter", na=False)]

    df = df.reset_index(drop=True)

    return df