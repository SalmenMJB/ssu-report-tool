import os
import matplotlib.pyplot as plt


def plot_appels_par_mois(df):
    year_cols = [col for col in df.columns if "appels_" in col]
    valid_cols = [col for col in year_cols if df[col].notna().sum() > 0]

    if not valid_cols:
        raise ValueError("Aucune colonne d'appels exploitable trouvée.")

    latest_year = valid_cols[-1]

    data = df[["mois", latest_year]].dropna()

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(10, 5))
    plt.plot(data["mois"], data[latest_year], marker="o")
    plt.title(f"Appels par mois ({latest_year})")
    plt.xlabel("Mois")
    plt.ylabel("Nombre d'appels")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/charts/appels_par_mois.png")
    plt.close()