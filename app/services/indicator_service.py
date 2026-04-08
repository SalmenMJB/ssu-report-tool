import pandas as pd


"""
def compute_dspe_indicators(df):
    indicators = {}

    indicators["Total lignes"] = len(df) # nb de séances]

    if "1res séances" in df.columns:
        indicators["Premières séances"] = df['1res séances'].fillna(0).sum()
    else: indicators["Premières séances"] = 0

    if "séances de suivi" in df.columns:
        indicators["Séances de suivi"] = df['séances de suivi'].fillna(0).sum()
    else: indicators["Séances de suivi"] = 0

    return indicators



def compute_ide_indicators(df):
    # Initialise un dictionnaire vide pour stocker tous les indicateurs
    indicators = {}
    # Compte le nombre total de lignes = nombre de consultations
    indicators["total_consultations"] = len(df) # nb lignes
    # Si la colonne existe, compte le nombre d'étudiants uniques
    if "id_etu" in df.columns:
        indicators["etudiants"] = df['id_etu'].nunique()
    # Si la colonne existe, calcule la moyenne d'âge en ignorant les valeurs manquantes
    if "âge" in df.columns:
        indicators["age_moyen"] = df['âge'].dropna().mean()
    # Si la colonne existe, retourne les 5 nationalités les plus fréquentes
    if "nationalité" in df.columns:
        indicators["top_nationalites"] = df['nationalité'].value_counts(dropna=False).head(5)
    # Si la colonne existe, compte les occurrences de chaque modalité de visite
    if "visite effectuée" in df.columns:
        indicators["visites_effectuees"] = df['visite effectuée'].value_counts(dropna=False) # laisser les 0
    # Si la colonne existe, compte les occurrences de chaque type de vaccination
    if "vaccination effectuée" in df.columns:
        indicators["vaccinations"] = df['vaccination effectuée'].value_counts(dropna=False) # laisser les 0
    # Si la colonne existe, compte la répartition des situations de handicap
    if "handicap" in df.columns:
        indicators["handicap"] = df['handicap'].value_counts(dropna=False) # laisser les 0

    return indicators
"""

def compute_stat_activite_indicators(df):
    indicators = {}

    indicators["total_consultations"] = len(df)

    if "id_etu" in df.columns:
        indicators["etudiants_uniques"] = df["id_etu"].nunique()

    if "âge" in df.columns:
        indicators["age_moyen"] = df["âge"].dropna().mean()

    if "centre" in df.columns:
        indicators["consultations_par_centre"] = df["centre"].value_counts(dropna=False)

    if "motif" in df.columns:
        motif_counts = df["motif"].value_counts(dropna=False)

        indicators["top_motifs"] = motif_counts.head(10)

        indicators["consultations_medecine_generale"] = motif_counts.get("Consultations médecine générale", 0)
        indicators["consultations_psychologie"] = motif_counts.get("Psychologie", 0)
        indicators["consultations_psychiatrie"] = motif_counts.get("Psychiatrie", 0)
        indicators["consultations_ide"] = motif_counts.get("Consultations IDE", 0)
        indicators["consultations_css"] = motif_counts.get("Centre de planification", 0)
        indicators["consultations_bilans"] = motif_counts.get("Bilan de prévention", 0)

    if "motif réels" in df.columns:
        indicators["top_motifs_reels"] = df["motif réels"].value_counts(dropna=False).head(10)

    if "établissement" in df.columns:
        indicators["consultations_par_etablissement"] = df["établissement"].value_counts(dropna=False).head(10)

    if "sexe" in df.columns:
        indicators["repartition_sexe"] = df["sexe"].value_counts(dropna=False)

    if "nationalité" in df.columns:
        indicators["top_nationalites"] = df["nationalité"].value_counts(dropna=False).head(10)

    if "visite effectuée" in df.columns:
        indicators["visites_effectuees"] = df["visite effectuée"].value_counts(dropna=False)

    if "vaccination effectuée" in df.columns:
        indicators["vaccinations"] = df["vaccination effectuée"].value_counts(dropna=False)

    if "handicap" in df.columns:
        indicators["handicap"] = df["handicap"].value_counts(dropna=False)

    return indicators


def compute_effectifs_indicators(df):
    indicators = {}

    # Récupère les colonnes qui représentent des années (format "2022/2023" par exemple)
    year_cols = [col for col in df.columns if "/" in col]

    # Calcule le total des effectifs pour chaque année
    for col in year_cols:
        # Remplace les NaN par 0 avant de sommer pour éviter un résultat NaN
        indicators[f"total_{col}"] = df[col].fillna(0).sum()

    # Garde uniquement les colonnes d'années qui contiennent au moins une vraie valeur numérique
    valid_year_cols = [
        col for col in year_cols if pd.to_numeric(df[col], errors="coerce").notna().sum() > 0 # errors="coerce": remplace les vals non convertibles en nb par NaN
    ]

    if valid_year_cols:
        # Prend la dernière année valide (la plus récente dans la liste)
        latest_year = valid_year_cols[-1]

        # Convertit la colonne en numérique, les valeurs non convertibles deviennent NaN
        df[latest_year] = pd.to_numeric(df[latest_year], errors="coerce")

        # Construit un classement des 5 établissements avec le plus grand effectif sur la dernière année
        indicators["top_etablissement"] = df[["etablissement", latest_year]].dropna(subset=[latest_year]).sort_values(by=latest_year, ascending=False).head(5) # dropna(subset): # Exclut les lignes sans effectif

        # Mémorise quelle année a été utilisée pour le classement
        indicators["latest_year_used"] = latest_year

    return indicators



def compute_stats_standard_indicators(df):
    indicators = {}

    # détecter colonnes années
    year_cols = [col for col in df.columns if "appels_" in col]

    # totaux par année
    for col in year_cols:
        indicators[f"total_{col}"] = df[col].fillna(0).sum()

    # dernière année exploitable
    valid_year_cols = [
        col for col in year_cols
        if df[col].notna().sum() > 0
    ]

    if valid_year_cols:
        latest_year = valid_year_cols[-1]

        indicators["latest_year"] = latest_year

        # total appels année récente
        indicators["total_appels_latest_year"] = df[latest_year].fillna(0).sum()

        # appels pour mois
        indicators["appels_par_mois"] = df[["mois", latest_year]].dropna()

    return indicators



def compute_consommables_indicators(df):
    indicators = {}

    indicators["nombres_actions"] = len(df) # nb de lignes

    material_cols = [
        "preservatifs_externes",
        "preservatifs_banane",
        "preservatifs_fraise",
        "preservatifs_sans_latex",
        "preservatifs_internes",
        "gel_lubrifiant",
        "bouchons_oreille",
        "livrets_cocktails",
        "reglettes_alcool",
        "ethylo_0_5",
        "ethylo_0_2",
        "eco_cup",
        "capuchons_verre",
        "packs_arret_tabac",
        "sur_sac_reflechissant",
        "livret_recette_automne",
        "livret_recette_hiver",
        "livret_recette_printemps",
        "livret_recette_ete",
        "autres_quantites",
    ]

    # calcul des totaux
    for col in material_cols:
        if col in df.columns:
            indicators[f"total_{col}"] = df[col].fillna(0).sum()

    if "campus" in df.columns:
        indicators["actions_par_campus"] = df["campus"].value_counts(dropna=False)

    if "etablissement" in df.columns:
        indicators["actions_par_etablissement"] = df["etablissement"].value_counts(dropna=False).head(10)

    return indicators




def compute_pssm_indicators(pssm_sheets):
    indicators = {}
    all_frames = []

    for sheet_name, df in pssm_sheets.items(): # items = pages
        temp = df.copy()

        numeric_cols = [
            "etudiants ua",
            "etudiants autres",
            "personnels ua",
            "personnels autres",
            "total / session",
        ]

        for col in numeric_cols:
            if col in temp.columns:
                temp[col] = pd.to_numeric(temp[col], errors="coerce")

        all_frames.append(temp)

    if not all_frames:
        return indicators


    all_pssm = pd.concat(all_frames, ignore_index=True)

    # garder les lignes avec une vraie date/session
    if "dates" in all_pssm.columns:
        all_pssm = all_pssm[all_pssm["dates"].notna()]

    indicators["nombre_sessions"] = len(all_pssm)

    for col in ["etudiants ua", "etudiants autres", "personnels ua", "personnels autres"]:
        if col in all_pssm.columns:
            indicators[f"total_{col.replace(' ', '_')}"] = all_pssm[col].fillna(0).sum()

        if "total / session" in all_pssm.columns:
            indicators["total_participants_declares"] = all_pssm["total / session"].fillna(0).sum()

        if "sheet_name" in all_pssm.columns:
            indicators["sessions_par_feuille"] = all_pssm["sheet_name"].value_counts()

        if "lieu" in all_pssm.columns:
            indicators["sessions_par_lieu"] = all_pssm["lieu"].fillna("non renseigné").value_counts()

        return indicators






