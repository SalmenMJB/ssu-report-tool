from app.parsers.seances_dspe import parse_dspe_file
from app.parsers.activites_ide import parse_ide_file
from app.parsers.effectifs import parse_effectifs_file
from app.parsers.stats_standard import parse_stats_standard_file
from app.parsers.consommables import parse_consommables_file
from app.parsers.pssm import parse_pssm_file
from app.parsers.stat_activite import parse_stat_activite_file

from app.services.indicator_service import  compute_dspe_indicators
from app.services.indicator_service import compute_ide_indicators
from app.services.indicator_service import compute_effectifs_indicators
from app.services.indicator_service import compute_stats_standard_indicators
from app.services.indicator_service import compute_consommables_indicators
from app.services.indicator_service import compute_pssm_indicators

from app.charts.effectifs_graph import generer_graph_effectifs


""" Deux fonctions pour un affichage plus propre dans le terminal """
def print_section(title: str):
    print(f"\n{'=' * 10} {title} {'=' * 10}\n")

def print_indicators(indicators: dict):
    for key, value in indicators.items():
        print(f"{key} :")
        print(value)
        print()


def main():
    print_section("DSPE")
    dspe_path = "data/raw/seances_dspe_24_25.xlsx" 
    df_dspe = parse_dspe_file(dspe_path)
    print(df_dspe.head())
    dspe_stats = compute_dspe_indicators(df_dspe)
    print_indicators(dspe_stats)

    
    print_section("IDE")
    ide_path = "data/raw/stats_activites_ide_24_25.xlsx" 
    df_ide = parse_ide_file(ide_path)
    print(df_ide.head())
    ide_stats = compute_ide_indicators(df_ide)
    print_indicators(ide_stats)
    
    print_section("Effectifs")
    effectifs_path = "data/raw/evolution_etab_conventionnes.xlsx" 
    df_effectifs = parse_effectifs_file(effectifs_path)
    print(df_effectifs.head())
    effectifs_stats = compute_effectifs_indicators(df_effectifs)
    print_indicators(effectifs_stats)


    print_section("STATS STANDARD")
    stats_path = "data/raw/stats_standard_ssu.xlsx"
    df_stats = parse_stats_standard_file(stats_path)
    stats_stats = compute_stats_standard_indicators(df_stats)
    print_indicators(stats_stats)

    print_section("CONSOMMABLES")
    consommables_path = "data/raw/extraction_consommables_actions_24_25.xlsx"
    df_consommables = parse_consommables_file(consommables_path)
    print(df_consommables.head())
    print()
    consommables_stats = compute_consommables_indicators(df_consommables)
    print_indicators(consommables_stats)


    print_section("PSSM")
    pssm_path = "data/raw/recap_pssm.xlsx"
    pssm_sheets = parse_pssm_file(pssm_path)
    print("Onglets retenus :")
    print(list(pssm_sheets.keys()))
    print()
    pssm_stats = compute_pssm_indicators(pssm_sheets)
    print_indicators(pssm_stats)


    print_section("STAT ACTIVITE")
    path = "data/raw/stat_activite.xlsx"
    df_stat = parse_stat_activite_file(path)
    print(df_stat.head(30))
    print()

    generer_graph_effectifs()

if __name__ == "__main__":
    main()