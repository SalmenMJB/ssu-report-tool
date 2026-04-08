import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_repartition_activite_infirmiere(csv_path: str):
    df = pd.read_csv(csv_path)

    labels = df["categorie"].astype(str)
    values = df["valeur"]

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(8, 8))

    def autopct_format(values):
        def inner(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return f"{pct:.1f}%"
        return inner

    plt.pie( 
        values,
        labels=labels,
        autopct=autopct_format(values),
        startangle=90
    )

    plt.title("Répartition de l'activité infirmière")
    plt.tight_layout()
    plt.savefig("output/charts/repartition_activite_infirmiere.png")
    plt.close()




def plot_activite_infirmiere_compare(csv_path):
    df = pd.read_csv(csv_path)

    categories = df["categorie"]
    values_1 = df["2023-2024"]
    values_2 = df["2024-2025"]

    x = np.arange(len(categories))
    width = 0.35

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(11, 6))

    bars1 = plt.bar(x - width/2, values_1, width, label="2023-2024")
    bars2 = plt.bar(x + width/2, values_2, width, label="2024-2025")

    # valeurs au-dessus
    offset = max(max(values_1), max(values_2)) * 0.00002

    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                height + offset,
                str(int(height)),
                ha="center",
                va="bottom",
                fontsize=8
            )

    plt.xticks(x, categories, rotation=30, ha="right")
    plt.title("Comparaison de l'activité infirmière sur deux années")
    plt.ylabel("Nombre d'actes")
    plt.legend()

    plt.tight_layout()
    plt.savefig("output/charts/activite_infirmiere_compare.png")
    plt.close()

def plot_repartition_activite_depuis_reel(df):

    motifs = df["motif réels"].dropna()

    categories = {
        "Entretien / écoute": motifs.str.contains("Entretien|Première écoute", case=False).sum(),
        "Suivi psy": motifs.str.contains("Suivi santé mentale", case=False).sum(),
        "Bilans": motifs.str.contains("Bilan", case=False).sum(),
        "Aménagement": motifs.str.contains("Aménagement", case=False).sum(),
        "Gynéco / sexualité": motifs.str.contains("gynéco|contraception|IST", case=False).sum(),
        "Nutrition": motifs.str.contains("nutrition", case=False).sum(),
        "Autres": len(motifs)
    }

    # corriger "Autres"
    categories["Autres"] = len(motifs) - sum(v for k, v in categories.items() if k != "Autres")

    labels = list(categories.keys())
    values = list(categories.values())

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(7, 7))

    def autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100))
        return f"{val}\n({pct:.1f}%)"

    plt.pie(values, labels=labels, autopct=autopct)
    plt.title("Répartition des activités (basé sur motifs réels)")
    plt.tight_layout()
    plt.savefig("output/charts/repartition_activite_reelle.png")
    plt.close()