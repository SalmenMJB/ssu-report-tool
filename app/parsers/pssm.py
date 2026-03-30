import pandas as pd

def parse_pssm_file(filepath):
    sheets = pd.read_excel(filepath, sheet_name=None)
    parsed_sheets = {}

    for sheet_name, df in sheets.items():
        df = df.dropna(how="all")
        df.columns = [str(col).strip().lower() for col in df.columns]
        df = df.loc[:, ~df.columns.str.contains("^unnamed", na=False)]
        df = df.reset_index(drop=True)

        rename_map = {
            "formatrice/teur": "formatrice",
        }

        # garder seulement les feuilles qui ressemblent à un tableau de sessions
        if "dates" in df.columns:
            df["sheet_name"] = sheet_name
            parsed_sheets[sheet_name] = df

    return parsed_sheets