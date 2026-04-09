"""
Configuration globale du rapport SSU.
Centralize tous les paramètres du rapport.
"""

class ReportConfig:
    """Configuration du rapport SSU 2024-2025"""
    
    # Infos générales
    REPORT_TITLE = "Rapport d'activité"
    REPORT_SUBTITLE = "2024 – 2025"
    ACADEMIC_YEAR = "2024-2025"
    OUTPUT_FILENAME = "output/rapport_ssu_2024_2025.docx"
    
    # Chemins
    LOGO_PATH = "app/templates/assets/logo_ua.png"
    DATA_INPUT_PATH = "data/raw/"
    CHARTS_OUTPUT_PATH = "output/charts/"
    
    # Fichiers de données attendus
    DATA_FILES = {
        'activite': 'stat_activite.xlsx',
        'effectifs': 'evolution_etab_conventionnes.xlsx',
        'stats_standard': 'stats_standard_ssu.xlsx',
        'consommables': 'extraction_consommables_actions_24_25.xlsx',
        'pssm': 'recap_pssm.xlsx',
        'psy': 'stats_psy.xlsx',
    }
    
    # Paramètres de style
    DEFAULT_FONT = 'Calibri'
    DEFAULT_FONT_SIZE = 11
    DEFAULT_LINE_SPACING = 1.15
    
    # Marges du document (en cm)
    MARGINS = {
        'top': 2.0,
        'bottom': 2.0,
        'left': 2.0,
        'right': 2.0,
    }
    
    # Couleurs (sera complété par colors_config.json)
    PRIMARY_COLOR = '#0099CC'  # Bleu ciel
    SECONDARY_COLOR = '#333333'  # Noir
    LIGHT_COLOR = '#F5F5F5'  # Gris clair
    
    # Chapitres dans l'ordre
    CHAPTERS_ORDER = [
        'intro',
        'effectifs',
        'medecine',
        'ide',
        'consommables',
        'pssm',
        'dspe',
        'css',
        'dietetique',
        'partenariats',
    ]
    
    # Configuration des graphiques
    CHART_CONFIG = {
        'dpi': 300,
        'figure_size': (10, 6),
        'style': 'seaborn-v0_8-darkgrid',
        'colors': ['#0099CC', '#FFA500', '#333333', '#F5F5F5'],
    }
    
    # Paramètres de tableau
    TABLE_CONFIG = {
        'header_background': '#0099CC',
        'header_font_color': 'FFFFFF',
        'row_alternate_color': '#F5F5F5',
        'border_color': '#CCCCCC',
    }