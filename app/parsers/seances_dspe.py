import pandas as pd

def parse_dspe_file(filepath):
    df = pd.read_excel(filepath)

    # supprimer les lignes totalement vides
    df = df.dropna(how="all")

    # nettoyer les noms de colonnes
    df.columns = [str(col).strip().lower() for col in df.columns]

    # supprimer les colonnes "unnamed"
    df = df.loc[:, ~df.columns.str.contains("^unnamed")]

    # réindexer proprement
    df = df.reset_index(drop=True)

    return df