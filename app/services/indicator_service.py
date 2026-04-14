import pandas as pd

from app.utils.cleaning import standardize_simple_labels, standardize_etablissement
from app.config.intervenants import get_profession


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
        df = df.copy()
        df["centre"] = standardize_simple_labels(df["centre"])
        indicators["consultations_par_centre"] = df["centre"].value_counts(dropna=False)

    if "motif" in df.columns:
        df = df.copy() if "centre" not in df.columns else df
        df["motif"] = standardize_simple_labels(df["motif"])
        motif_counts = df["motif"].value_counts(dropna=False)

        indicators["top_motifs"] = motif_counts.head(10)

        # Recherche tolérante à la casse pour les principaux motifs
        def _get_motif(counts, *candidates):
            for c in candidates:
                val = counts.get(c, None)
                if val is not None:
                    return val
                # essai insensible à la casse
                for idx in counts.index:
                    if str(idx).lower() == c.lower():
                        return counts[idx]
            return 0

        indicators["consultations_medecine_generale"] = _get_motif(
            motif_counts,
            "Consultations médecine générale",
            "Consultations medecine generale",
        )
        indicators["consultations_psychologie"] = _get_motif(motif_counts, "Psychologie")
        indicators["consultations_psychiatrie"] = _get_motif(motif_counts, "Psychiatrie")
        indicators["consultations_ide"] = _get_motif(
            motif_counts, "Consultations IDE", "Consultations ide"
        )
        indicators["consultations_css"] = _get_motif(
            motif_counts, "Centre de planification"
        )
        indicators["consultations_bilans"] = _get_motif(
            motif_counts, "Bilan de prévention", "Bilan de prevention"
        )

    if "motif réels" in df.columns:
        indicators["top_motifs_reels"] = df["motif réels"].value_counts(dropna=False).head(10)

    if "établissement" in df.columns:
        etab_series = df["établissement"].map(standardize_etablissement)
        indicators["consultations_par_etablissement"] = etab_series.value_counts(dropna=False).head(10)

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

    # Gérer les colonnes de dates alternatives : "dates", "date début", "date de début"
    date_col = None
    for candidate in ("dates", "date début", "date de début", "date debut", "date"):
        if candidate in all_pssm.columns:
            date_col = candidate
            break

    if date_col:
        all_pssm = all_pssm[all_pssm[date_col].notna()]

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


def compute_bilan_actions_indicators(df):
    """
    Analyse des actions d'éducation sanitaire :
    thèmes, établissements, sites UA et consommables.
    """
    indicators = {}

    indicators["nombre_actions"] = len(df)

    if "theme" in df.columns:
        df = df.copy()
        df["theme"] = standardize_simple_labels(df["theme"])
        indicators["actions_par_theme"] = df["theme"].value_counts(dropna=False)

    if "etablissement" in df.columns:
        etab_series = df["etablissement"].map(standardize_etablissement)
        indicators["actions_par_etablissement"] = etab_series.value_counts(dropna=False)

    if "site" in df.columns:
        df = df.copy() if "theme" not in df.columns else df
        df["site"] = standardize_simple_labels(df["site"])
        indicators["actions_par_site"] = df["site"].value_counts(dropna=False)
        # utiliser le site comme campus si pas de colonne campus
        if "campus" not in df.columns:
            indicators["actions_par_campus"] = indicators["actions_par_site"]

    if "campus" in df.columns:
        indicators["actions_par_campus"] = df["campus"].value_counts(dropna=False)

    if "nb_participants" in df.columns:
        indicators["total_participants"] = df["nb_participants"].fillna(0).sum()

    # Calculer les totaux de consommables
    consommables_cols = [
        "preservatifs_externes", "preservatifs_xl", "preservatifs_skin",
        "preservatifs_internes", "gel_lubrifiant", "digues", "depistages",
        "ethylo_0_2", "ethylo_0_5", "reglettes_alcool", "capuchons_verre",
        "livrets_cocktails", "eco_cup", "packs_arret_tabac", "roule_ta_paille",
        "bouchons_oreille", "audiogrammes", "livret_recette_hiver",
        "livret_recette_ete", "livret_recette_automne", "livret_recette_printemps",
        "sur_sac_reflechissant",
    ]
    for col in consommables_cols:
        if col in df.columns:
            total = df[col].fillna(0).sum()
            if total > 0:
                indicators[f"total_{col}"] = total

    return indicators


def compute_css_indicators(df):
    """
    Analyse du Centre de Santé Sexuelle :
    filtre les lignes avec motif == "Centre de planification".
    """
    indicators = {}

    if "motif" not in df.columns:
        return indicators

    df_css = df[
        df["motif"].str.lower().str.contains("planification", na=False)
    ].copy()

    indicators["total_consultations_css"] = len(df_css)

    if "motif réels" in df_css.columns:
        motifs_reels = df_css["motif réels"].value_counts(dropna=False)
        indicators["motifs_reels_css"] = motifs_reels

    if "établissement" in df_css.columns:
        etab_series = df_css["établissement"].map(standardize_etablissement)
        indicators["css_par_etablissement"] = etab_series.value_counts(dropna=False)

    if "sexe" in df_css.columns:
        indicators["css_repartition_sexe"] = df_css["sexe"].value_counts(dropna=False)

    return indicators


def compute_bilans_professionnels_indicators(df, medecins=None, infirmieres=None):
    """
    Analyse des bilans de prévention par profession
    (médecins vs infirmières vs autres).

    Paramètres :
    - df : DataFrame des activités
    - medecins : liste des noms de médecins (optionnel)
    - infirmieres : liste des noms d'infirmières (optionnel)
    """
    indicators = {}

    if medecins is None:
        medecins = []
    if infirmieres is None:
        infirmieres = []

    if "motif" not in df.columns:
        return indicators

    df_bilans = df[
        df["motif"].str.lower().str.contains("bilan", na=False)
    ].copy()

    indicators["total_bilans"] = len(df_bilans)

    # Déterminer la colonne intervenant
    intervenant_col = None
    for candidate in ("intervenant", "praticien", "médecin", "professionnel"):
        if candidate in df_bilans.columns:
            intervenant_col = candidate
            break

    if intervenant_col:
        def _categorize(name):
            if name is None or pd.isna(name):
                return "Autre"
            name_lower = str(name).lower()
            for m in medecins:
                if m.lower() in name_lower:
                    return "Médecin"
            for i in infirmieres:
                if i.lower() in name_lower:
                    return "Infirmier/Infirmière"
            if name_lower.startswith("dr") or name_lower.startswith("dr."):
                return "Médecin"
            if name_lower.startswith("inf") or "infirm" in name_lower:
                return "Infirmier/Infirmière"
            return "Autre"

        df_bilans["profession"] = df_bilans[intervenant_col].map(_categorize)
        indicators["bilans_par_profession"] = df_bilans["profession"].value_counts(dropna=False)
        indicators["bilans_medecins"] = int(
            (df_bilans["profession"] == "Médecin").sum()
        )
        indicators["bilans_infirmieres"] = int(
            (df_bilans["profession"] == "Infirmier/Infirmière").sum()
        )
        indicators["bilans_autres_intervenants"] = int(
            (df_bilans["profession"] == "Autre").sum()
        )

    if "établissement" in df_bilans.columns:
        etab_series = df_bilans["établissement"].map(standardize_etablissement)
        indicators["bilans_par_etablissement"] = etab_series.value_counts(dropna=False)

    if "composante" in df_bilans.columns:
        indicators["bilans_par_composante"] = df_bilans["composante"].value_counts(dropna=False).head(10)

    return indicators


