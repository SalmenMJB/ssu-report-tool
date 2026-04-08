import os
import pandas as pd
import matplotlib.pyplot as plt

"""
Plus tard, on pourra faire une fonction du style :
append_current_year_activite_medicale(...)
qui calcule automatiquement la ligne 2025-2026 à partir des exports Calcium, puis met à jour le CSV historique.

Les 3 premières lignes du csv sont des exemples à remplacer plus tard par les vrais chiffres si vous les avez.
La dernière ligne reprend les chiffres du rapport.
"""

def plot_evolution_activite_medicale(csv_path: str):
    df = pd.read_csv(csv_path)

    if df.empty:
        raise ValueError("Le fichier CSV est vide.")

    years = df["annee"]
    os.makedirs("output/charts", exist_ok=True)

    # ---- Graphique 1 : gros volumes ----
    plt.figure(figsize=(10, 6))

    main_series = [
        ("total_medical", "Activité médicale totale"),
        ("medecine_generale", "Médecine générale"),
    ]

    for col, label in main_series:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            plt.plot(years, df[col], marker="o", label=label)

            # offset = df[col].max() * 0 if df[col].notna().any() else 0.01
            # for x, y in zip(years, df[col]):
            #     if pd.notna(y):
            #         plt.text(x, y + offset, str(int(y)), ha="center", va="bottom", fontsize=8)

    plt.title("Évolution de l'activité médicale globale")
    plt.xlabel("Année universitaire")
    plt.ylabel("Nombre d'actes / consultations")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.savefig("output/charts/evolution_activite_medicale_globale.png")
    plt.close()

    # ---- Graphique 2 : activités détaillées ----
    plt.figure(figsize=(10, 6))

    detail_series = [
        ("sante_mentale", "Santé mentale"),
        ("bilans_preventifs", "Bilans préventifs"),
        ("amenagements", "Aménagements"),
        ("suivis_dossiers", "Suivis de dossiers"),
    ]

    for col, label in detail_series:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            plt.plot(years, df[col], marker="o", label=label)

            # offset = df[col].max() * 0.02 if df[col].notna().any() else 1
            # for x, y in zip(years, df[col]):
            #     if pd.notna(y):
            #         plt.text(x, y + offset, str(int(y)), ha="center", va="bottom", fontsize=8)

    plt.title("Évolution détaillée des activités médicales")
    plt.xlabel("Année universitaire")
    plt.ylabel("Nombre d'actes / consultations")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.savefig("output/charts/evolution_activite_medicale_detail.png")
    plt.close()


def plot_repartition_activite_medicale_annee(csv_path: str):
    df = pd.read_csv(csv_path)

    if df.empty:
        raise ValueError("Le fichier CSV est vide.")

    latest = df.iloc[-1]

    data = {
        "Médecine générale": pd.to_numeric(pd.Series([latest["medecine_generale"]]), errors="coerce").iloc[0],
        "Santé mentale": pd.to_numeric(pd.Series([latest["sante_mentale"]]), errors="coerce").iloc[0],
        "Bilans préventifs": pd.to_numeric(pd.Series([latest["bilans_preventifs"]]), errors="coerce").iloc[0],
        "Aménagements": pd.to_numeric(pd.Series([latest["amenagements"]]), errors="coerce").iloc[0],
        "Suivis dossiers": pd.to_numeric(pd.Series([latest["suivis_dossiers"]]), errors="coerce").iloc[0],
    }

    data = {k: v for k, v in data.items() if pd.notna(v)}

    labels = list(data.keys())
    values = list(data.values())

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values)

    offset = max(values) * 0.02 if values else 1
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + offset,
            str(int(height)),
            ha="center",
            va="bottom",
            fontsize=9
        )

    plt.title(f"Répartition de l'activité médicale ({latest['annee']})")
    plt.xlabel("Type d'activité")
    plt.ylabel("Nombre d'actes / consultations")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig("output/charts/repartition_activite_medicale.png")
    plt.close()