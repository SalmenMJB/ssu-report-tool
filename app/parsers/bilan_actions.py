import pandas as pd


def parse_bilan_actions_file(filepath):
    """
    Parse le fichier Excel de bilan des actions d'éducation sanitaire.

    Retourne un DataFrame avec les colonnes normalisées.
    """
    df = pd.read_excel(filepath)

    df = df.dropna(how="all")
    df.columns = [str(col).strip().lower() for col in df.columns]
    df = df.loc[:, ~df.columns.str.contains("^unnamed", na=False)]
    df = df.reset_index(drop=True)

    return df
