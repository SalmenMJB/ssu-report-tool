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
        # Thème
        "thème": "theme",
        "theme": "theme",
        "thème(s) abordé(s)": "theme",
        "themes abordés": "theme",
        # Établissement
        "établissement": "etablissement",
        "etablissement": "etablissement",
        # Site
        "site": "site",
        "site ua": "site",
        # Campus
        "campus": "campus",
        # Date
        "date": "date_action",
        "date de l'action": "date_action",
        "date de l'action ?": "date_action",
        # Participants
        "nombre de participants": "nb_participants",
        "participants": "nb_participants",
        "nbre etudiants touchés": "nb_participants",
        "nbre étudiants touchés": "nb_participants",
        # Intervenants
        "intervenant": "intervenant",
        "intervenante": "intervenant",
        "nbre ssu": "nb_ssu",
        "nbre ers": "nb_ers",
        # Type et description
        "type d'action": "type_action",
        "type action": "type_action",
        "description": "description",
        "remarques": "remarques",
        # Numéro
        "numéro action": "numero_action",
        "numéro de l'action": "numero_action",
        # Consommables distribués
        "préservatifs externes": "preservatifs_externes",
        "xl": "preservatifs_xl",
        "skin": "preservatifs_skin",
        "préservatifs internes": "preservatifs_internes",
        "gel": "gel_lubrifiant",
        "digues": "digues",
        "dépistages réalisés": "depistages",
        "ethylotests 0,2": "ethylo_0_2",
        "ethylotests 0,5": "ethylo_0_5",
        "réglettes alcool": "reglettes_alcool",
        "réglettes alcool ": "reglettes_alcool",
        "capuchons de verre": "capuchons_verre",
        "livret cocktails sans alcool": "livrets_cocktails",
        "ecocups": "eco_cup",
        "pack mois sans tabac": "packs_arret_tabac",
        "roule ta paille": "roule_ta_paille",
        "bouchons d'oreilles": "bouchons_oreille",
        "audiogrammes": "audiogrammes",
        "tête accoustique": "tete_acoustique",
        "livret cuisine hiver": "livret_recette_hiver",
        "livret cuisine été": "livret_recette_ete",
        "livret cuisine automne": "livret_recette_automne",
        "livret cuisine printemps": "livret_recette_printemps",
        "recettes salées": "recettes_salees",
        "recettes sucrées": "recettes_sucrees",
        "nbre petit dej": "nb_petit_dej",
        "vélosmoothie": "velosmoothie",
        "nbre de sieste flash": "nb_sieste_flash",
        "nbre de sophrologie": "nb_sophrologie",
        "bandeau réfléchissant": "bandeau_reflechissant",
        "sur sac à dos réfléchissant": "sur_sac_reflechissant",
    }

    existing_rename = {k: v for k, v in rename_map.items() if k in df.columns}
    df = df.rename(columns=existing_rename)

    if "nb_participants" in df.columns:
        df["nb_participants"] = pd.to_numeric(df["nb_participants"], errors="coerce")

    # Convertir les colonnes de consommables en numérique
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
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df
