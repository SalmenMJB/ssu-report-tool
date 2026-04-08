import pandas as pd

def parse_effectifs_file(filepath):
    # Charge le fichier Excel en partant de la 4ème ligne comme en-tête
    df = pd.read_excel(filepath, header=3)

    # Supprime les lignes entièrement vides
    df = df.dropna(how="all")
    # Normalise les noms de colonnes : supprime les espaces et met en minuscules
    df.columns = [str(col).strip().lower() for col in df.columns]
    # Supprime les colonnes sans nom générées automatiquement par pandas
    df = df.loc[:, ~df.columns.str.contains("^unnamed", na=False)] # na=False: # Si une cellule est NaN → retourne False

    # Garder uniquement les VRAIES lignes établissements (le nom d'établissement est renseigné)
    if "etablissement" in df.columns:
        df = df[df["etablissement"].notna()]
        # SUPPRIMER LES LIGNES type TOTAL (lignes de synthèse)
        df = df[~df["etablissement"].str.lower().str.contains("total", na=False)] # ~: not
        # Supprime les lignes de type "à compter de..." (remarques ou notes)
        df = df[~df["etablissement"].str.lower().str.contains("compter", na=False)] # ~: not

    # Réinitialise l'index après toutes les suppressions
    df = df.reset_index(drop=True)

    return df