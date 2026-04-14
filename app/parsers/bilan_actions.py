import pandas as pd


def parse_bilan_actions_file(filepath):
    """
    Parse le fichier bilan_actions.xlsx contenant les actions
    d'éducation sanitaire réalisées par le SSU.

    Retourne un DataFrame nettoyé avec les colonnes standardisées.
    """
    df = pd.read_excel(filepath)

    df = df.dropna(how="all")
    df.columns = [str(col).strip().lower() for col in df.columns]
    df = df.loc[:, ~df.columns.str.contains("^unnamed", na=False)]
    df = df.reset_index(drop=True)

    rename_map = {
        "thème": "theme",
        "theme": "theme",
        "établissement": "etablissement",
        "etablissement": "etablissement",
        "site": "site",
        "campus": "campus",
        "date": "date_action",
        "date de l'action": "date_action",
        "date de l'action ?": "date_action",
        "nombre de participants": "nb_participants",
        "participants": "nb_participants",
        "intervenant": "intervenant",
        "intervenante": "intervenant",
        "type d'action": "type_action",
        "type action": "type_action",
        "description": "description",
        "remarques": "remarques",
    }

    existing_rename = {k: v for k, v in rename_map.items() if k in df.columns}
    df = df.rename(columns=existing_rename)

    if "nb_participants" in df.columns:
        df["nb_participants"] = pd.to_numeric(df["nb_participants"], errors="coerce")

    return df
