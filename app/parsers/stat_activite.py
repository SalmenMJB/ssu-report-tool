# INUTILE POUR L'INSTANT
import pandas as pd

def parse_stat_activite_file(filepath):
    df = pd.read_excel(filepath, header=None) # on ne va faire eliminer le header ici
    df = df.dropna(how='all')
    df = df.reset_index(drop=True)

    return df