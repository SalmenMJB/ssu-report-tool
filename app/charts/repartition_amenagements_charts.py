from app.parsers.stat_activite import parse_stat_activite_file
import matplotlib.pyplot as plt
import numpy as np

def plot_reparition_amenagements():
    xlsx_path = "data/raw/stat_activite.xlsx"
    df = parse_stat_activite_file(xlsx_path)

    labels = df["établissement"].drop_duplicates()
    #   changer les noms dans labels
    #   Ecole Technique Supérieure de Chimie de l'Ouest = ETSCO
    #   Université d'Angers = UA
    #   AGRO Campus Ouest = Institut Agro Rennes Angers
    #   Lycée de Pouillé = Campus de Pouillé
    # somme = df["Établissement"].count()
    # nb_par_etabs = df["Établissement"].value_counts()
    # print(nb_par_etabs)
    # print(df.columns)
    motif_regex = r'.*Aménagement ESH.*'
    # motifs = ['Aménagement ESH + certificat inital',"Aménagement ESH + certificat inital;Première écoute","Aménagement ESH + certificat inital;Médecine générale","Aménagement ESH + certificat inital;Contraception","Aménagement ESH + certificat inital;Contraception;Première écoute","Aménagement ESH + certificat inital;dépistage IST","Aménagement ESH + certificat inital;Première écoute","Aménagement ESH + certificat inital;Problème Gynéco","Aménagement ESH + certificat inital;Suivi santé mentale"]
    # df_amenagements = df[df["Motif réels"].isin(motifs)]
    compte_par_etablissement = (df[df["motif réels"].str.contains(motif_regex,case=False, na=False)].groupby("établissement").size().reset_index(name="Nombre amenagements"))
    compte_par_etablissement["établissement"] = compte_par_etablissement["établissement"].replace({
        "Université d\'Angers" : "UA",
        "Lycée de Pouillé" : "Campus de Pouillé"})
    # print(compte_par_etablissement)

    compte_par_etablissement = compte_par_etablissement.sort_values(by="Nombre amenagements", ascending=False)

    plt.figure(figsize=(10,6))
    bars = plt.bar(compte_par_etablissement["établissement"],
        compte_par_etablissement["Nombre amenagements"],
        color='red')

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.,
            height,
            f'{int(height)}',
            ha='center',
            va='bottom')

    plt.title("Nombre d'aménagements ESH par établissement")
    plt.xlabel("Établissement")
    plt.ylabel("Nombre d'aménagements")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.savefig("output/charts/repartition_amenagements.png", dpi=300, bbox_inches="tight")
    # plt.show()