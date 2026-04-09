# Architecture du Rapport SSU 2024-2025

## Vue d'ensemble

Le rapport SSU est généré de manière modulaire et cohérente en utilisant :
- **Configuration centralisée** (config/)
- **Composants réutilisables** (app/report_generator/components/)
- **Chapitres indépendants mais homogènes** (app/report_generator/chapters/)
- **Thème global cohérent** (styling/)

## Structure des dossiers

### `app/report_generator/`
Cœur de la génération du rapport

- **`document_builder.py`** : Classe principale pour construire le document Word
- **`styling/`** : Gestion des styles (thème, polices, couleurs)
- **`components/`** : Composants réutilisables (titres, bullets, encadrés)
- **`charts/`** : Génération des graphiques
- **`chapters/`** : Contenu spécifique à chaque chapitre

### `config/`
Configuration globale et constantes

- **`report_config.py`** : Configuration Python
- **`styles_config.json`** : Styles en JSON
- **`colors_config.json`** : Palette de couleurs

### `data/raw/`
Données d'entrée (fichiers Excel)

### `output/`
Fichiers générés

- **`rapport_ssu_2024_2025.docx`** : Document Word final
- **`charts/`** : Graphiques générés en PNG

## Flux de génération
generate_report.py ↓ Chargement des données (parsers/) ↓ Création du document (ReportBuilder) ↓ Ajout titre et table des matières ↓ Génération de chaque chapitre ├── intro.py ├── effectifs.py ├── medecine.py ├── ide.py ├── consommables.py ├── pssm.py ├── dspe.py ├── css.py ├── dietetique.py └── partenariats.py ↓ Sauvegarde du document ↓ output/rapport_ssu_2024_2025.docx

## Principes de design
1. **Cohérence** : Un seul endroit pour les styles
2. **Réutilisabilité** : Composants partagés
3. **Maintenabilité** : Code clair et bien structuré
4. **Extensibilité** : Facile d'ajouter de nouveaux chapitres
5. **Testabilité** : Chaque composant peut être testé

## Dépendances
- `python-docx` : Création de documents Word
- `matplotlib` : Génération de graphiques
- `openpyxl` : Lecture de fichiers Excel
- `pandas` : Traitement des données

## Pour développer
1. Modifier les styles : `config/styles_config.json`
2. Modifier les couleurs : `config/colors_config.json`
3. Ajouter un composant : `app/report_generator/components/`
4. Ajouter un chapitre : `app/report_generator/chapters/`