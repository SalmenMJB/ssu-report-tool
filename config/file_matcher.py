"""
Matcher pour associer les fichiers sélectionnés à leurs rôles.
Permet de gérer les noms différents des fichiers Excel.
"""

import json
import os
from pathlib import Path
from fnmatch import fnmatch


class FileMatcher:
    def __init__(self):
        """Charge la configuration de mapping des fichiers"""
        config_path = Path(__file__).parent / "excel_mapping.json"
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        self.mappings = self.config['file_mappings']
    
    def match_file(self, filepath: str) -> str:
        """
        Trouve le rôle d'un fichier basé sur son nom.
        
        Args:
            filepath: Chemin complet du fichier
        
        Returns:
            str: Rôle du fichier (effectifs, stats_standard, etc.)
        
        Raises:
            ValueError: Si le fichier ne correspond à aucun rôle
        """
        filename = os.path.basename(filepath).lower()
        
        for role, mapping in self.mappings.items():
            for pattern in mapping['patterns']:
                if fnmatch(filename, pattern.lower()):
                    return role
        
        raise ValueError(f"❌ Impossible d'identifier le rôle du fichier : {filename}")
    
    def match_files(self, filepaths: list) -> dict:
        """
        Associe une liste de fichiers à leurs rôles.
        
        Args:
            filepaths: Liste des chemins de fichiers
        
        Returns:
            dict: Dictionnaire {rôle: filepath}
        
        Raises:
            ValueError: Si fichiers obligatoires manquent
        """
        matched = {}
        
        for filepath in filepaths:
            try:
                role = self.match_file(filepath)
                if role in matched:
                    print(f"⚠️ Attention : plusieurs fichiers pour '{role}'")
                matched[role] = filepath
            except ValueError as e:
                raise ValueError(str(e))
        
        # Vérifie les fichiers obligatoires
        for role, mapping in self.mappings.items():
            if mapping['required'] and role not in matched:
                raise ValueError(
                    f"❌ Fichier obligatoire manquant : {mapping['description']}\n"
                    f"Patterns attendus : {', '.join(mapping['patterns'])}"
                )
        
        return matched
    
    def get_required_files(self) -> list:
        """Retourne la liste des fichiers obligatoires"""
        return [
            f"{role}: {mapping['description']}"
            for role, mapping in self.mappings.items()
            if mapping['required']
        ]
    
    def get_optional_files(self) -> list:
        """Retourne la liste des fichiers optionnels"""
        return [
            f"{role}: {mapping['description']}"
            for role, mapping in self.mappings.items()
            if not mapping['required']
        ]