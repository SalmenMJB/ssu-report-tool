import os
import matplotlib.pyplot as plt
import pandas as pd


def plot_actions_par_theme(bilan_indicators: dict) -> None:
    """Graphique en barres horizontales des actions par thème."""
    data = bilan_indicators.get("actions_par_theme")
    if data is None or len(data) == 0:
        return

    data = data[data.index.notna()].sort_values(ascending=True)

    os.makedirs("output/charts", exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, max(5, len(data) * 0.5)))
    bars = ax.barh(data.index.astype(str), data.values, color="#3498DB")

    offset = max(data.values) * 0.01 if len(data.values) > 0 else 1
    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + offset,
            bar.get_y() + bar.get_height() / 2,
            str(int(width)),
            va="center",
            fontsize=9,
        )

    ax.set_title("Actions d'éducation sanitaire par thème")
    ax.set_xlabel("Nombre d'actions")
    ax.set_ylabel("Thème")
    plt.tight_layout()
    plt.savefig("output/charts/bilan_actions_par_theme.png")
    plt.close()


def plot_bilan_actions_par_campus(bilan_indicators: dict) -> None:
    """Graphique en barres des actions par campus."""
    data = bilan_indicators.get("actions_par_campus")
    if data is None or len(data) == 0:
        return

    data = data[data.index.notna()]

    os.makedirs("output/charts", exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(data.index.astype(str), data.values, color="#16A085")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            str(int(height)),
            ha="center",
            va="bottom",
            fontsize=9,
        )

    ax.set_title("Actions d'éducation sanitaire par campus")
    ax.set_xlabel("Campus")
    ax.set_ylabel("Nombre d'actions")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig("output/charts/bilan_actions_par_campus.png")
    plt.close()


def plot_consommables_bilan_actions(bilan_indicators: dict) -> None:
    """
    Graphique des consommables distribués lors des actions de bilan.
    Utilise les clés préfixées par 'total_' dans les indicateurs.
    """
    data = {
        key.replace("total_", "").replace("_", " "): value
        for key, value in bilan_indicators.items()
        if key.startswith("total_") and isinstance(value, (int, float)) and value > 0
    }

    if not data:
        return

    data = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))

    os.makedirs("output/charts", exist_ok=True)

    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(list(data.keys()), list(data.values()), color="#2ECC71")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            str(int(height)),
            ha="center",
            va="bottom",
            fontsize=9,
        )

    ax.set_title("Consommables distribués lors des actions")
    ax.set_xlabel("Type de matériel")
    ax.set_ylabel("Quantité")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("output/charts/consommables_bilan_actions.png")
    plt.close()


def plot_actions_par_site_lisible(bilan_indicators: dict) -> None:
    """
    Graphique en barres horizontales des actions par site/établissement
    à partir des indicateurs du bilan d'actions.
    """
    data = bilan_indicators.get("actions_par_etablissement")
    if data is None:
        data = bilan_indicators.get("actions_par_site")
    if data is None or len(data) == 0:
        return

    if hasattr(data, "index"):
        data = data[data.index.notna()]
        s = data.sort_values(ascending=True)
    else:
        import pandas as pd
        s = pd.Series(data).sort_values(ascending=True)

    os.makedirs("output/charts", exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, max(5, len(s) * 0.5)))
    bars = ax.barh(s.index.astype(str), s.values, color="#3498DB")

    offset = max(s.values) * 0.01 if len(s.values) > 0 else 1

    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + offset,
            bar.get_y() + bar.get_height() / 2,
            str(int(width)),
            va="center",
            fontsize=9,
        )

    ax.set_title("Répartition des lieux et nombre d'actions par site")
    ax.set_xlabel("Nombre d'actions")
    ax.set_ylabel("Site")
    plt.tight_layout()
    plt.savefig("output/charts/actions_par_site_lisible.png")
    plt.close()
