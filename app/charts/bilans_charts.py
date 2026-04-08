import os
import matplotlib.pyplot as plt


def plot_bilans_par_composante(df_bilans):
    data = df_bilans["composante"].value_counts().head(10)

    labels = data.index.astype(str)
    values = data.values

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(11, 6))
    bars = plt.bar(labels, values, color="#3498DB")

    offset = max(values) * 0.00002

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

    plt.title("Bilans de santé préventifs par composante")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig("output/charts/bilans_par_composante.png")
    plt.close()


def plot_bilans_internationaux(df_bilans):
    df_bilans["type_etudiant"] = df_bilans["nationalité"].apply(
        lambda x: "International" if x != "FRANCE" else "France"
    )

    data = df_bilans["type_etudiant"].value_counts()

    labels = data.index
    values = data.values

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(6, 6))

    def autopct_format(values):
        def inner(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return f"{val}\n({pct:.1f}%)"
        return inner

    plt.pie(
        values,
        labels=labels,
        autopct=autopct_format(values),
        colors=["#2ECC71", "#E74C3C"]
    )

    plt.title("Bilans : étudiants internationaux vs français")
    plt.tight_layout()
    plt.savefig("output/charts/bilans_internationaux.png")
    plt.close()


def plot_bilans_par_filiere(df_bilans):
    data = df_bilans["section"].value_counts().head(10)

    labels = data.index.astype(str)
    values = data.values

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(11, 6))
    bars = plt.bar(labels, values, color="#9B59B6")

    offset = max(values) * 0.002

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

    plt.title("Bilans de santé préventifs par filière")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig("output/charts/bilans_par_filiere.png")
    plt.close()