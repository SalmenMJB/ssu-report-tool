====== STRUCTURE DU PROJET:

ssu-report-tool/
├── app/
│   ├── __init__.py
│   ├── generate_report.py: python -m app.generate_report
│   │ 
│   ├── parsers/
│   │   ├── __init__.py
│   │   ├── effectifs.py
│   │   ├── stats_standard.py
│   │   ├── consommables.py
│   │   ├── stat_activite.py
│   │   ├── pssm.py
│   │   └── psy.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── indicator_service.py
│   │
│   ├── report_generator/
│   │   ├── __init__.py
│   │   ├── document_builder.py: MAJOR
│   │   ├── styles.py: Gestion centralisée des styles
│   │   ├── colors.py NOUVEAU: Palette de couleurs
│   │   ├── graphics_helper.py: Graphiques avancés
│   │   ├── layout_helper.py: Mise en page
│   │   │
│   │   └── chapters/
│   │       ├── __init__.py
│   │       ├── intro.py
│   │       ├── effectifs.py
│   │       ├── medecine.py
│   │       ├── ide.py
│   │       ├── consommables.py: Éducation à la santé
│   │       ├── pssm.py
│   │       ├── dspe.py: DSPE/Psychologie/Psychiatrie/Santé mentale
│   │       ├── css.py: Centre de santé sexuelle
│   │       ├── dietetique.py: NOUVEAU - Diététique et Nutrition
│   │       └── partenariats.py
│   │
│   └── templates/
│       ├── assets/
│       │   ├── logo_ua.png
│       │   └── colors_config.json: Config couleurs
│       │
│       └── defaults/
│           ├── bullet_style.py
│           ├── table_style.py
│           └── chart_style.py
│
├── output/
│   ├── rapport_ssu_2024_2025.docx (GÉNÉRÉ)
│   └── charts/: Graphiques générés
│       ├── pssm_sessions.png
│       ├── activity_pie.png
│       ├── consultation_bar.png
│       └── ... (autres graphiques)
│
├── data/
│   └── raw/: SOURCES (tableaux EXCEL)
│   |    ├── evolution_etab_conventionnes.xlsx
│   |    ├── stats_standard_ssu.xlsx
│   |    ├── stat_activite.xlsx
│   |    ├── extraction_consommables_actions_24_25.xlsx
│   |    ├── recap_pssm.xlsx
|   |    ├── stats_psy.xlsx
│   |    └── (autres...)   
|   |____ processed/: SOURCES collectés à la main depuis l'ancien rapport (à garder sauf trouver des vraies valeurs)
│
├── tests/
│   ├── __init__.py
│   ├── test_document_builder.py
│   ├── test_styles.py
│   ├── test_graphics.py
│   └── test_chapters/
│       ├── __init__.py
│       ├── test_intro.py
│       ├── test_effectifs.py
│       └── ... (tests par chapitre)
│
├── config/
│   ├── __init__.py
│   ├── report_config.py: Config globale
│   ├── styles_config.json: Styles en JSON
│   └── colors_config.json: Palette de couleurs
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── STYLES_GUIDE.md: Guide des styles
│   ├── GRAPHICS_GUIDE.md: Types de graphiques
│   ├── CHAPTERS_STRUCTURE.md
│   └── API_REFERENCE.md
│
│
├── requirements.txt: bibliothèques à installer: pip install -r requirements.txt
├── README.md
└── .gitignore


======= À quoi sert chaque dossier:
**app/**
C’est le cœur du projet.
    _app/main.py_
        Le point d’entrée principal.
        C’est lui qui lance le pipeline :
            lecture des fichiers
            parsing
            calculs
            génération des graphiques
            génération du rapport

**app/parsers/**
    Un fichier par type d’Excel.
    C’est super important dans votre cas.
    Exemple :
        calcium_standard.py : pour les exports statistiques standards
        activites_ide.py : pour le fichier IDE
        seances_dspe.py : pour le fichier DSPE
        effectifs.py : pour le fichier effectifs
    Chaque parser doit savoir :
        ouvrir le bon fichier
        ignorer les mauvaises lignes
        nettoyer les colonnes
        retourner un DataFrame propre

**app/services/**
    Ici, on mets la logique métier.
    Par exemple : 
        _import_service.py_
            coordonne l’import de plusieurs fichiers
        _indicator_service.py_
            calcule les KPI (chiffres clés (indicateurs)):
                nombre de consultations
                évolution annuelle
                répartition par service
                etc.
    _chart_service.py_
        génère les graphiques
    _report_service.py_
        prépare le HTML puis le PDF

**app/models/**
    Pas forcément une “base de données” tout de suite.
    on peut y mettre des structures de données simples :
        noms de colonnes normalisés
        objets métier
        formats attendus

**app/utils/**
    Fonctions utilitaires réutilisables.
    Exemples :
        trouver la vraie ligne d’en-tête
        nettoyer les colonnes Unnamed
        convertir des nombres
        gérer les dates

**app/templates/**
    Si vous générez le rapport en HTML avec Jinja2.
    Tu peux avoir :
        un template principal
        des sous-sections par service
        un CSS pour le rendu PDF

**data/raw/**
    Les fichiers bruts importés, jamais modifiés.

**data/processed/**
    Les données nettoyées ou intermédiaires.

**data/sample**
Des petits fichiers d’exemple pour tester sans utiliser les vrais à chaque fois.

**output/**
    Tout ce que l’outil produit :
        graphiques
        rapport PDF
        exports intermédiaires

**tests/**
    Même si vous n’en faites pas beaucoup, mets au moins quelques tests simples.
    Ça fera très sérieux et très utile.
