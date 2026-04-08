import matplotlib.pyplot as plt
import pandas as pd

def plot_top_etablissements(df):
    # detecter colonnes années
    year_cols = [col for col in df.columns if "/" in col]

    # garder celles qui ont des données
    valid_year_cols = [
        col for col in year_cols
        if pd.to_numeric(df[col], errors="coerce").notna().sum() > 0
    ]

    latest_year = valid_year_cols[-1]

    # préparer données
    temp = df[["etablissement", latest_year]].copy()
    temp[latest_year] = pd.to_numeric(temp[latest_year], errors="coerce")
    temp = temp.dropna(subset=[latest_year])

    # top 10
    temp = temp.sort_values(by=latest_year, ascending=False).head(10)
    
    plt.figure(figsize=(10,6))
    bars = plt.bar(temp["etablissement"], temp[latest_year])

    # ajouter valeurs au-dessus des barres
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            str(int(height)),
            ha='center',
            va='bottom'
        )

    plt.title(f"Top établissements ({latest_year})")
    plt.xlabel("Établissement")
    plt.ylabel("Nombre d'étudiants")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig("output/charts/top_etablissements.png")
    plt.close()