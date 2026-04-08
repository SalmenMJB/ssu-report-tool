import pandas as pd

def parse_stat_activite_file(filepath):
    df_raw = pd.read_excel(filepath, header=None)

    # trouver ligne header
    header_row = None
    for i, row in df_raw.iterrows():
        if row.astype(str).str.contains("id_etu", case=False).any():
            header_row = i
            break

    if header_row is None:
        raise ValueError("Header non trouvé")
    
    df = pd.read_excel(filepath, header=header_row)

    df.dropna(how="all")
    df = df.reset_index(drop=True)

    # nettoyage noms colonnes
    df.columns = [str(col).strip().lower() for col in df.columns]

    return df