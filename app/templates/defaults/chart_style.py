"""
Styles des graphiques (couleurs, fonts, légendes).
"""

import matplotlib.pyplot as plt

# Palette de couleurs pour graphiques
CHART_COLORS = {
    'primary': '#0099CC',  # Bleu ciel
    'secondary': '#333333',  # Noir
    'accent_orange': '#FFA500',  # Orange
    'accent_green': '#4CAF50',  # Vert
    'accent_red': '#F44336',  # Rouge
    'accent_yellow': '#FFEB3B',  # Jaune
    'accent_blue_dark': '#1976D2',  # Bleu foncé
    'accent_turquoise': '#00BCD4',  # Turquoise
    'light_gray': '#F5F5F5',  # Gris clair
}

# Palettes pour différents types de graphiques
PIE_PALETTE = [
    CHART_COLORS['primary'],
    CHART_COLORS['accent_orange'],
    CHART_COLORS['secondary'],
    CHART_COLORS['light_gray'],
    CHART_COLORS['accent_green'],
    CHART_COLORS['accent_yellow'],
]

BAR_SINGLE_PALETTE = [CHART_COLORS['primary']]

BAR_COMPARISON_PALETTE = [
    CHART_COLORS['accent_turquoise'],
    CHART_COLORS['accent_blue_dark'],
]

LINE_PALETTE = [
    CHART_COLORS['primary'],
    CHART_COLORS['accent_red'],
]

# Configuration matplotlib
CHART_STYLE = 'seaborn-v0_8-whitegrid'
CHART_DPI = 300
CHART_FIGURE_SIZE = (10, 6)
CHART_FONT_SIZE = 10
CHART_LEGEND_FONT_SIZE = 9
CHART_TITLE_FONT_SIZE = 12

# Configuration par type
CHART_CONFIG = {
    'pie': {
        'colors': PIE_PALETTE,
        'figure_size': (10, 8),
        'dpi': CHART_DPI,
        'font_size': CHART_FONT_SIZE,
        'legend_fontsize': CHART_LEGEND_FONT_SIZE,
    },
    'bar': {
        'colors': BAR_SINGLE_PALETTE,
        'figure_size': CHART_FIGURE_SIZE,
        'dpi': CHART_DPI,
        'font_size': CHART_FONT_SIZE,
        'legend_fontsize': CHART_LEGEND_FONT_SIZE,
    },
    'line': {
        'colors': LINE_PALETTE,
        'figure_size': CHART_FIGURE_SIZE,
        'dpi': CHART_DPI,
        'font_size': CHART_FONT_SIZE,
        'legend_fontsize': CHART_LEGEND_FONT_SIZE,
        'line_width': 2,
        'marker_size': 8,
    },
}

def apply_chart_style():
    """Applique le style global aux graphiques matplotlib"""
    plt.style.use(CHART_STYLE)
    plt.rcParams['font.size'] = CHART_FONT_SIZE
    plt.rcParams['legend.fontsize'] = CHART_LEGEND_FONT_SIZE
    plt.rcParams['axes.titlesize'] = CHART_TITLE_FONT_SIZE