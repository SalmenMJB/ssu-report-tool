# Guide de style – Rapport SSU / Université d'Angers

Ce document décrit les conventions visuelles et typographiques à respecter pour
assurer la cohérence du rapport d'activité SSU avec la charte graphique de
l'Université d'Angers.

---

## 1. Couleurs

| Rôle | Couleur | Hex |
|------|---------|-----|
| Bleu ciel UA (principal) | `COLOR_UA_BLUE` | `#00A8E1` |
| Bleu ciel pâle (alternance tableau) | `COLOR_BLUE_PALE` | `#E1F5FE` |
| Gris clair (alternance tableau) | `COLOR_GRAY_LIGHT` | `#F5F5F5` |
| Noir (corps de texte) | `COLOR_BLACK` | `#000000` |
| Blanc | `COLOR_WHITE` | `#FFFFFF` |

Toutes les constantes sont définies dans `app/report_generator/styles.py`.

---

## 2. Typographie

| Élément | Police | Taille | Style | Couleur |
|---------|--------|--------|-------|---------|
| Titre de couverture | Calibri | 28 pt | Gras | Bleu ciel UA |
| Heading 1 (chapitre) | Calibri | 22 pt | Gras | Bleu ciel UA |
| Heading 2 (section) | Calibri | 16 pt | Gras | Bleu ciel UA |
| Heading 3 (sous-section) | Calibri | 13 pt | Gras | Bleu ciel UA |
| Sous-titre italique | Calibri | 13 pt | Italique | Bleu ciel UA |
| Corps de texte | Calibri | 11 pt | Normal | Noir |
| Légende graphique | Calibri | 9 pt | Italique | Gris |

---

## 3. Flèches bleues

Les flèches bleues `➠` sont utilisées systématiquement pour mettre en valeur
les données clés, les points importants et les listes structurées.

### Niveau 1 — `➠` (bleu ciel UA, gras)
```python
builder.add_blue_arrow_paragraph("Total consultations : 5 432")
```

### Niveau 2 — `➠➠` (bleu ciel pâle, indenté)
```python
builder.add_nested_arrow_list([
    "Point principal",
    ("Point avec sous-points", [
        "Sous-point A",
        "Sous-point B",
    ]),
])
```

---

## 4. Tableaux

- **En-tête** : fond bleu ciel UA (`#00A8E1`), texte blanc, centré, gras
- **Lignes impaires** : fond bleu pâle (`#E1F5FE`)
- **Lignes paires** : fond gris clair (`#F5F5F5`)
- **Style** : `"Table Grid"` avec alignement centré

```python
builder.add_key_indicators_table(
    {"Consultations": 1500, "Étudiants uniques": 800},
    title="Chiffres clés"
)
```

---

## 5. Boîtes bleues

Pour encadrer une information importante :

```python
builder.add_blue_box("Information importante à mettre en valeur.")
```

Rendu : tableau 1×1 avec bordure bleue (`#00A8E1`) et fond blanc.

---

## 6. Graphiques

- **Largeur pleine** : `IMAGE_WIDTH_FULL = Cm(16)` — pour les graphiques principaux
- **Demi-largeur** : `IMAGE_WIDTH_HALF = Cm(7.5)` — pour deux graphiques côte à côte
- **Largeur standard** : `IMAGE_WIDTH_CHART = Cm(9)` — pour les graphiques centrés
- Toujours centrés dans la page
- Légende courte en italique gris sous chaque graphique

```python
builder.add_image(
    "output/charts/mon_graphique.png",
    caption="Titre court du graphique",
)
```

---

## 7. Structure d'un chapitre type

```python
# Titre du chapitre (Heading 1)
builder.add_chapter("Nom du chapitre", "Texte d'introduction court.")

# Section (Heading 2)
builder.add_section("Titre de la section", "Texte optionnel.")

# Sous-titre italique bleu
builder.add_section_subtitle("Précision sur la sous-section")

# Données clés en flèches bleues
builder.add_blue_arrow_paragraph("Donnée clé : valeur")

# Graphique
builder.add_image("output/charts/graphique.png", caption="Légende")

# Tableau de chiffres clés
builder.add_key_indicators_table({"Indicateur": valeur}, title="Chiffres clés")

# Zone éditable pour l'équipe SSU
builder.add_editable_comment_zone()
```

---

## 8. Page de titre

Design minimaliste :
- Logo UA (4,5 cm de large, centré)
- Titre en majuscules, bleu ciel UA, 28 pt
- Ligne décorative `─────` en bleu ciel
- Année en noir, 18 pt
- "Service de Santé Universitaire" en bleu ciel, 16 pt
- "Université d'Angers" en noir, 13 pt
- **Page blanche** entre la couverture et le sommaire

---

## 9. Sommaire

- Titre "Sommaire" centré en Heading 1
- Champ TOC Word (`\\o "1-3"`) mis à jour automatiquement par Word/LibreOffice
- Pour mettre à jour : cliquer dans le sommaire puis appuyer sur **F9** (Windows)
  ou **Cmd+A+F9** (Mac)

---

## 10. Espacement

| Zone | Espace avant | Espace après |
|------|-------------|--------------|
| Heading 1 | 18 pt | 12 pt |
| Heading 2 | 14 pt | 8 pt |
| Heading 3 | 10 pt | 6 pt |
| Corps de texte | 4 pt | 8 pt |
| Flèche bleue | 4 pt | 4 pt |

---

## 11. Marges

- Haut, bas, gauche, droite : **2,5 cm** (défini par `MARGIN_CM`)

---

## 12. Ajout d'un nouveau chapitre

1. Créer un fichier `app/report_generator/chapters/mon_chapitre.py`
2. Importer `ReportBuilder` depuis `app.report_generator.document_builder`
3. Définir une fonction `build_mon_chapitre_chapter(builder, ...):`
4. Utiliser les méthodes ci-dessus pour respecter le style
5. Ajouter l'appel dans `app/generate_report.py`
6. Mettre à jour le test `test_full_report_structure` dans `tests/test_report.py`
