import pandas as pd


def parse_dspe_file(filepath):
    """
    Parse le fichier seances_dspe.xlsx contenant les séances de psychologie
    du Dispositif Santé Psy Étudiant (DSPE).

    Retourne un DataFrame nettoyé avec les colonnes standardisées.
    """
    df = pd.read_excel(filepath)

    df = df.dropna(how="all")
    df.columns = [str(col).strip().lower() for col in df.columns]
    df = df.loc[:, ~df.columns.str.contains("^unnamed", na=False)]
    df = df.reset_index(drop=True)

    rename_map = {
        "1res séances": "premieres_seances",
        "1ères séances": "premieres_seances",
        "1ères seances": "premieres_seances",
        "première séance": "premieres_seances",
        "séances de suivi": "seances_suivi",
        "seances de suivi": "seances_suivi",
        "suivi": "seances_suivi",
        "total séances": "total_seances",
        "total seances": "total_seances",
        "total": "total_seances",
        "psychologue": "psychologue",
        "date début": "date_debut",
        "date de début": "date_debut",
        "date fin": "date_fin",
        "date de fin": "date_fin",
        "établissement": "etablissement",
        "etablissement": "etablissement",
        "id_etu": "id_etu",
    }

    existing_rename = {k: v for k, v in rename_map.items() if k in df.columns}
    df = df.rename(columns=existing_rename)

    numeric_cols = ["premieres_seances", "seances_suivi", "total_seances"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df
