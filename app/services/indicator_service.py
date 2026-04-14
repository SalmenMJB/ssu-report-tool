"""
Service de calcul des indicateurs SSU.

Ce module fournit des fonctions pour calculer les indicateurs statistiques
à partir des DataFrames chargés par les parsers.
"""

import pandas as pd


# ---------------------------------------------------------------------------
# Effectifs
# ---------------------------------------------------------------------------

def compute_effectifs_indicators(df):
    """
    Calcule les indicateurs d'effectifs à partir du DataFrame effectifs.

    Retourne un dict avec :
    - total_{année} : total par colonne année
    - latest_year_used : libellé de la dernière année disponible
    """
    if df is None or df.empty:
        return {}

    indicators = {}
    year_cols = [col for col in df.columns if "/" in col]

    for col in year_cols:
        total = pd.to_numeric(df[col], errors="coerce").fillna(0).sum()
        if total > 0:
            indicators[f"total_{col}"] = int(total)

    if year_cols:
        # Dernière année avec des données non nulles
        for col in reversed(year_cols):
            total = pd.to_numeric(df[col], errors="coerce").fillna(0).sum()
            if total > 0:
                indicators["latest_year_used"] = col
                break

    return indicators


# ---------------------------------------------------------------------------
# Statistiques standard (appels)
# ---------------------------------------------------------------------------

def compute_stats_standard_indicators(df):
    """
    Calcule les indicateurs de statistiques standard (appels téléphoniques).

    Retourne un dict avec :
    - total_appels_latest_year : total de la dernière année
    - latest_year : libellé de la colonne de la dernière année
    """
    if df is None or df.empty:
        return {}

    indicators = {}

    year_cols = [col for col in df.columns if "appels_" in col]
    valid_cols = [col for col in year_cols if df[col].notna().sum() > 0]

    if not valid_cols:
        return indicators

    latest_year = valid_cols[-1]
    indicators["latest_year"] = latest_year

    total = pd.to_numeric(df[latest_year], errors="coerce").fillna(0).sum()
    indicators["total_appels_latest_year"] = int(total)

    return indicators


# ---------------------------------------------------------------------------
# Activité générale
# ---------------------------------------------------------------------------

def compute_stat_activite_indicators(df):
    """
    Calcule les indicateurs d'activité générale à partir du fichier stat_activite.

    Retourne un dict avec de nombreuses clés (Series et scalaires).
    """
    if df is None or df.empty:
        return {}

    indicators = {}

    # Consultations par centre / établissement
    if "établissement" in df.columns:
        indicators["consultations_par_centre"] = df["établissement"].value_counts()
    elif "etablissement" in df.columns:
        indicators["consultations_par_centre"] = df["etablissement"].value_counts()

    # Top motifs (première valeur de motif réel, en cas de valeurs multiples séparées par ";")
    if "motif réels" in df.columns:
        motifs = df["motif réels"].dropna().str.split(";").explode().str.strip()
        indicators["top_motifs"] = motifs.value_counts()

        # Indicateurs scalaires par type de consultation
        motif_counts = indicators["top_motifs"]
        indicators["consultations_medecine_generale"] = int(
            motif_counts.get("Consultations médecine générale", 0)
            or motif_counts.get("Medecine generale", 0)
            or motif_counts.get("Médecine générale", 0)
        )
        indicators["consultations_bilans"] = int(
            motif_counts.get("Bilan de santé", 0)
            or motif_counts.get("Bilans de prévention", 0)
            or motif_counts.get("Bilan préventif", 0)
            or motif_counts.get("Bilan", 0)
        )
        indicators["consultations_psychologie"] = int(
            motif_counts.get("Psychologie", 0)
        )
        indicators["consultations_psychiatrie"] = int(
            motif_counts.get("Psychiatrie", 0)
        )
        indicators["consultations_css"] = int(
            motif_counts.get("Centre de planification", 0)
            or motif_counts.get("CSS", 0)
            or motif_counts.get("Gynécologie", 0)
        )
        indicators["consultations_ide"] = int(
            motif_counts.get("Consultations IDE", 0)
            or motif_counts.get("IDE", 0)
            or motif_counts.get("Consultation infirmière", 0)
        )

    # Répartition par sexe
    if "sexe" in df.columns:
        indicators["repartition_sexe"] = df["sexe"].value_counts()

    # Top nationalités
    if "nationalité" in df.columns:
        indicators["top_nationalites"] = df["nationalité"].value_counts()
    elif "nationalite" in df.columns:
        indicators["top_nationalites"] = df["nationalite"].value_counts()

    # Visites effectuées
    if "visite" in df.columns:
        indicators["visites_effectuees"] = df["visite"].value_counts()
    elif "visites" in df.columns:
        indicators["visites_effectuees"] = df["visites"].value_counts()

    # Vaccinations
    if "vaccination" in df.columns:
        indicators["vaccinations"] = df["vaccination"].value_counts()
    elif "vaccinations" in df.columns:
        indicators["vaccinations"] = df["vaccinations"].value_counts()

    # Handicap
    if "handicap" in df.columns:
        indicators["handicap"] = df["handicap"].value_counts()
    elif "type handicap" in df.columns:
        indicators["handicap"] = df["type handicap"].value_counts()

    return indicators


# ---------------------------------------------------------------------------
# CSS (Centre de Santé Sexuelle)
# ---------------------------------------------------------------------------

def compute_css_indicators(df):
    """
    Calcule les indicateurs spécifiques au Centre de Santé Sexuelle.

    Retourne un dict avec :
    - motifs_reels_css : Series des motifs au CSS
    - total_consultations_css : int
    """
    if df is None or df.empty:
        return {}

    indicators = {}

    # Identifier les consultations CSS (centre de planification / gynécologie)
    css_keywords = ["centre de planification", "planification", "gynéco", "css",
                    "contraception", "ist", "frottis"]

    if "motif réels" in df.columns:
        css_mask = df["motif réels"].str.lower().str.contains(
            "|".join(css_keywords), na=False
        )
        df_css = df[css_mask]

        if not df_css.empty:
            motifs = df_css["motif réels"].dropna().str.split(";").explode().str.strip()
            indicators["motifs_reels_css"] = motifs.value_counts()
            indicators["total_consultations_css"] = int(css_mask.sum())

    return indicators


# ---------------------------------------------------------------------------
# Bilans professionnels
# ---------------------------------------------------------------------------

def compute_bilans_professionnels_indicators(df, medecins, infirmieres):
    """
    Calcule les indicateurs de bilans par profession à partir du fichier activité.

    Paramètres :
    - df : DataFrame stat_activite
    - medecins : liste de chaînes identifiant les médecins
    - infirmieres : liste de chaînes identifiant les infirmier·ère·s

    Retourne un dict avec :
    - bilans_medecins : int
    - bilans_infirmieres : int
    - bilans_autres_intervenants : int
    """
    if df is None or df.empty:
        return {"bilans_medecins": 0, "bilans_infirmieres": 0, "bilans_autres_intervenants": 0}

    # Identifier la colonne praticien/intervenant
    praticien_col = None
    for candidate in ["praticien", "intervenant", "professionnel", "medecin", "nom praticien"]:
        if candidate in df.columns:
            praticien_col = candidate
            break

    # Si pas de colonne praticien, on s'appuie sur le motif pour déduire le type
    if praticien_col is None:
        # Essayer de déduire via le motif
        if "motif réels" in df.columns:
            bilan_mask = df["motif réels"].str.contains(
                "bilan", case=False, na=False
            )
            df_bilans = df[bilan_mask]
        else:
            df_bilans = df

        n = len(df_bilans)
        if n == 0:
            return {"bilans_medecins": 0, "bilans_infirmieres": 0, "bilans_autres_intervenants": 0}

        # Sans colonne praticien, répartir proportionnellement (fallback)
        return {
            "bilans_medecins": 0,
            "bilans_infirmieres": 0,
            "bilans_autres_intervenants": n,
        }

    # Filtrer les bilans de prévention
    if "motif réels" in df.columns:
        bilan_mask = df["motif réels"].str.contains("bilan", case=False, na=False)
        df_bilans = df[bilan_mask]
    else:
        df_bilans = df

    if df_bilans.empty:
        return {"bilans_medecins": 0, "bilans_infirmieres": 0, "bilans_autres_intervenants": 0}

    praticiens = df_bilans[praticien_col].fillna("").astype(str).str.lower()

    medecins_lower = [m.lower() for m in medecins]
    infirmieres_lower = [i.lower() for i in infirmieres]

    mask_medecins = praticiens.apply(
        lambda p: any(m in p for m in medecins_lower)
    )
    mask_infirmieres = praticiens.apply(
        lambda p: any(i in p for i in infirmieres_lower)
    )

    nb_medecins = int(mask_medecins.sum())
    nb_infirmieres = int(mask_infirmieres.sum())
    nb_autres = int((~mask_medecins & ~mask_infirmieres).sum())

    return {
        "bilans_medecins": nb_medecins,
        "bilans_infirmieres": nb_infirmieres,
        "bilans_autres_intervenants": nb_autres,
    }


# ---------------------------------------------------------------------------
# PSSM
# ---------------------------------------------------------------------------

def compute_pssm_indicators(pssm_sheets):
    """
    Calcule les indicateurs PSSM à partir des feuilles Excel parsées.

    Retourne un dict avec :
    - sessions_par_feuille : Series (feuille -> nb sessions)
    - total_etudiants_ua : int
    - total_etudiants_autres : int
    - total_personnels_ua : int
    - total_personnels_autres : int
    """
    if not pssm_sheets:
        return {}

    indicators = {}

    sessions_counts = {}
    total_etudiants_ua = 0
    total_etudiants_autres = 0
    total_personnels_ua = 0
    total_personnels_autres = 0

    for sheet_name, df in pssm_sheets.items():
        # Compter le nombre de sessions par feuille
        if "dates" in df.columns:
            nb_sessions = df["dates"].notna().sum()
        else:
            nb_sessions = len(df)
        sessions_counts[sheet_name] = int(nb_sessions)

        # Agréger les participants par catégorie
        for col in df.columns:
            col_lower = col.lower()
            if "étudiant" in col_lower and "ua" in col_lower:
                total_etudiants_ua += int(pd.to_numeric(df[col], errors="coerce").fillna(0).sum())
            elif "étudiant" in col_lower or "etudiants" in col_lower:
                total_etudiants_autres += int(pd.to_numeric(df[col], errors="coerce").fillna(0).sum())
            elif "personnel" in col_lower and "ua" in col_lower:
                total_personnels_ua += int(pd.to_numeric(df[col], errors="coerce").fillna(0).sum())
            elif "personnel" in col_lower:
                total_personnels_autres += int(pd.to_numeric(df[col], errors="coerce").fillna(0).sum())

    indicators["sessions_par_feuille"] = pd.Series(sessions_counts)
    indicators["total_etudiants_ua"] = total_etudiants_ua
    indicators["total_etudiants_autres"] = total_etudiants_autres
    indicators["total_personnels_ua"] = total_personnels_ua
    indicators["total_personnels_autres"] = total_personnels_autres

    return indicators


# ---------------------------------------------------------------------------
# Bilan des actions d'éducation sanitaire
# ---------------------------------------------------------------------------

def compute_bilan_actions_indicators(df):
    """
    Calcule les indicateurs du bilan des actions d'éducation sanitaire.

    Retourne un dict avec :
    - actions_par_theme : Series
    - actions_par_campus : Series
    - actions_par_etablissement : Series
    - nombre_actions : int
    - total_participants : int
    - total_preservatifs_externes : int (si colonne disponible)
    - total_preservatifs_internes : int (si colonne disponible)
    - total_ethylo_0_5 : int (si colonne disponible)
    - total_packs_arret_tabac : int (si colonne disponible)
    """
    if df is None or df.empty:
        return {}

    indicators = {}
    indicators["nombre_actions"] = len(df)

    # Actions par thème
    for candidate in ["thème", "theme", "thematique", "thématique", "sujet"]:
        if candidate in df.columns:
            indicators["actions_par_theme"] = df[candidate].value_counts()
            break

    # Actions par campus
    for candidate in ["campus", "site", "lieu"]:
        if candidate in df.columns:
            indicators["actions_par_campus"] = df[candidate].value_counts()
            break

    # Actions par établissement
    for candidate in ["établissement", "etablissement", "etab"]:
        if candidate in df.columns:
            indicators["actions_par_etablissement"] = df[candidate].value_counts()
            break

    # Participants
    for candidate in ["participants", "nb participants", "nombre participants",
                      "nb_participants", "personnes touchées", "personnes touchees"]:
        if candidate in df.columns:
            total = pd.to_numeric(df[candidate], errors="coerce").fillna(0).sum()
            indicators["total_participants"] = int(total)
            break

    # Consommables : parcourir les colonnes pour trouver les totaux
    consommables_map = {
        "préservatifs externes": "total_preservatifs_externes",
        "preservatifs externes": "total_preservatifs_externes",
        "préservatifs internes": "total_preservatifs_internes",
        "preservatifs internes": "total_preservatifs_internes",
        "éthylotests 0,5": "total_ethylo_0_5",
        "ethylotest 0.5": "total_ethylo_0_5",
        "ethylotests": "total_ethylo_0_5",
        "packs arrêt tabac": "total_packs_arret_tabac",
        "pack arret tabac": "total_packs_arret_tabac",
    }

    for col in df.columns:
        col_lower = col.lower().strip()
        for pattern, key in consommables_map.items():
            if pattern in col_lower and key not in indicators:
                total = pd.to_numeric(df[col], errors="coerce").fillna(0).sum()
                if total > 0:
                    indicators[key] = int(total)
                break

    return indicators
