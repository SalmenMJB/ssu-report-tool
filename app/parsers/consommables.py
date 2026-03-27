import pandas as pd

def parse_consommables_file(filepath):
    df = pd.read_excel(filepath)

    df = df.dropna(how="all")
    df.columns = [str(col).strip().lower() for col in df.columns]
    df = df.reset_index(drop=True)

    rename_map = {
        "numéro de l'action ? []": "numero_action",
        "date de l'action ?": "date_action",
        "dans quel établissement a eu lieu l'action ?": "etablissement",
        "dans quels sites l'action a-t-elle-eu-lieu ?": "site",
        "sur quel campus ?": "campus",
        "dans quel établissement a-t-elle eu lieu ?": "etablissement_2",
        "quantités de matériels distribués durant l'action ? [préservatifs externes][quantités]": "preservatifs_externes",
        "quantités de matériels distribués durant l'action ? [banane][quantités]": "preservatifs_banane",
        "quantités de matériels distribués durant l'action ? [fraise][quantités]": "preservatifs_fraise",
        "quantités de matériels distribués durant l'action ? [sans latex][quantités]": "preservatifs_sans_latex",
        "quantités de matériels distribués durant l'action ? [préservatifs internes][quantités]": "preservatifs_internes",
        "quantités de matériels distribués durant l'action ? [gel lubrifiant][quantités]": "gel_lubrifiant",
        "quantités de matériels distribués durant l'action ? [bouchon d'oreille][quantités]": "bouchons_oreille",
        "quantités de matériels distribués durant l'action ? [livrets cocktails sans alcool][quantités]": "livrets_cocktails",
        "quantités de matériels distribués durant l'action ? [réglettes alcool][quantités]": "reglettes_alcool",
        "quantités de matériels distribués durant l'action ? [ethylo 0.5][quantités]": "ethylo_0_5",
        "quantités de matériels distribués durant l'action ? [ethylo 0.2][quantités]": "ethylo_0_2",
        "quantités de matériels distribués durant l'action ? [eco cup][quantités]": "eco_cup",
        "quantités de matériels distribués durant l'action ? [capuchon de verre][quantités]": "capuchons_verre",
        "quantités de matériels distribués durant l'action ? [packs arrêt sans tabac][quantités]": "packs_arret_tabac",
        "quantités de matériels distribués durant l'action ? [sur sac à dos réfléchissant][quantités]": "sur_sac_reflechissant",
        "quantités de matériels distribués durant l'action ? [livret recette automne][quantités]": "livret_recette_automne",
        "quantités de matériels distribués durant l'action ? [livret recette hiver][quantités]": "livret_recette_hiver",
        "quantités de matériels distribués durant l'action ? [livret recette printemps][quantités]": "livret_recette_printemps",
        "quantités de matériels distribués durant l'action ? [livret recette été][quantités]": "livret_recette_ete",
        "quantités de matériels distribués durant l'action ? [autres][quantités]": "autres_quantites",
    }

    df = df.rename(columns=rename_map)

    numeric_cols = [ # noms après normalisation
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

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df