import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_delai_attente_psy(csv_path):
    df = pd.read_csv(csv_path)

    mois = df["mois"]
    valeurs = df["delai"]

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(mois, valeurs, marker="o")

    offset = 0.5

    for x, y in zip(mois, valeurs):
        plt.text(x, y + offset, str(y), ha="center", fontsize=9)

    plt.title("Évolution du délai d'attente en psychologie")
    plt.xlabel("Mois")
    plt.ylabel("Délai moyen (jours)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("output/charts/delai_attente_psy.png")
    plt.close()


# def plot_problematique_psy(df):
#     data = df["catégorie"].dropna().value_counts()

#     labels = data.index.astype(str)
#     values = data.values

#     colors = [
#         "#4A90E2",
#         "#E74C3C",
#         "#F5A623",
#         "#7ED321",
#         "#BD10E0",
#         "#9B9B9B",
#         "#34495E",
#         "#1ABC9C",
#         "#E67E22",
#         "#95A5A6",
#     ]

#     os.makedirs("output/charts", exist_ok=True)

#     plt.figure(figsize=(8, 8))

#     plt.pie(
#         values,
#         labels=labels,
#         autopct="%1.1f%%",
#         startangle=90,
#         wedgeprops=dict(width=0.4),
#         colors=colors[:len(values)]
#     )

#     plt.title("Répartition des problématiques psychologiques")
#     plt.tight_layout()
#     plt.savefig("output/charts/problematique_psy.png")
#     plt.close()


def plot_problematique_psy(df):
    data = df["catégorie"].dropna().value_counts()

    # garder les 8 plus grosses catégories
    top_n = 8
    top_data = data.head(top_n)

    autres = data.iloc[top_n:].sum()
    if autres > 0:
        top_data["Autres"] = autres

    labels = top_data.index.astype(str)
    values = top_data.values

    colors = [
        "#4A90E2",
        "#E74C3C",
        "#F5A623",
        "#7ED321",
        "#BD10E0",
        "#9B9B9B",
        "#34495E",
        "#1ABC9C",
        "#95A5A6",
    ]

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(10, 8))

    wedges, texts, autotexts = plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90,
        wedgeprops=dict(width=0.4),
        labeldistance=1.12,
        pctdistance=0.72,
        colors=colors[:len(values)]
    )

    plt.title("Répartition des problématiques psychologiques")
    plt.tight_layout()
    plt.savefig("output/charts/problematique_psy.png")
    plt.close()


# def plot_duree_suivi_psy(csv_path):
#     import os
#     import pandas as pd
#     import matplotlib.pyplot as plt

#     df = pd.read_csv(csv_path)

#     labels = df["categorie"]
#     values = df["valeur"]

#     os.makedirs("output/charts", exist_ok=True)

#     plt.figure(figsize=(10, 6))
#     bars = plt.bar(labels, values, color="#4A90E2")

#     offset = max(values) * 0.03 if len(values) > 0 else 1

#     for bar in bars:
#         height = bar.get_height()
#         plt.text(
#             bar.get_x() + bar.get_width() / 2,
#             height + offset,
#             str(int(height)),
#             ha="center",
#             va="bottom",
#             fontsize=9
#         )

#     plt.title("Durée de suivi psychologique")
#     plt.xlabel("Nombre de séances")
#     plt.ylabel("Nombre d'étudiants")
#     plt.xticks(rotation=20)
#     plt.tight_layout()
#     plt.savefig("output/charts/duree_suivi_psy.png")
#     plt.close()



def plot_duree_suivi(df):

    # filtrer uniquement les consultations psy
    df_psy = df[df["motif"] == "Psychologie"]

    # nb consultations par étudiant
    suivi = df_psy.groupby("id_etu").size()

    # catégorisation
    bins = [1, 3, 6, 9, 13, float("inf")]
    labels = ["1-3", "4-6", "7-9", "10-13", ">13"]

    categories = pd.cut(suivi, bins=bins, labels=labels, right=True)

    repartition = categories.value_counts().sort_index()

    # en %
    repartition_pct = (repartition / repartition.sum()) * 100

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(8, 5))
    bars = plt.bar(repartition.index.astype(str), repartition_pct.values)

    # valeurs au-dessus
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.05,
            f"{height:.1f}%",
            ha="center"
        )

    plt.title("Durée de suivi psychologique")
    plt.xlabel("Nombre de consultations")
    plt.ylabel("Pourcentage d'étudiants")

    plt.tight_layout()
    plt.savefig("output/charts/duree_suivi.png")
    plt.close()



# def plot_origine_stagiaires_pssm(df):
#     data = df["établissement"].value_counts()

#     labels = data.index.astype(str)
#     values = data.values

#     os.makedirs("output/charts", exist_ok=True)

#     plt.figure(figsize=(7, 7))

#     def autopct(pct):
#         total = sum(values)
#         val = int(round(pct * total / 100))
#         return f"{val}"

#     plt.pie(
#         values,
#         labels=labels,
#         autopct=autopct,
#         startangle=90
#     )

#     plt.title("Origine des stagiaires PSSM")
#     plt.tight_layout()
#     plt.savefig("output/charts/origine_pssm.png")
#     plt.close()