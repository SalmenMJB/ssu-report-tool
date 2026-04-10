"""
Interface Tkinter pour générer le rapport SSU.
Permet aux utilisateurs sans connaissances Python de générer le rapport.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading
import os
import sys
from pathlib import Path

# Ajoute le répertoire parent au path pour importer les modules
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from app.generate_report import main as generate_report
from config.file_matcher import FileMatcher 

class SSUReportGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🏥 Générateur Rapport SSU 2024-2025")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        
        # Style
        self.root.configure(bg="#F5F5F5")
        
        # Variables
        self.selected_files = []
        self.is_generating = False
        
        # === Header ===
        header_frame = tk.Frame(root, bg="#0099CC", height=80)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="📊 Générateur de Rapport SSU",
            font=("Calibri", 18, "bold"),
            fg="white",
            bg="#0099CC"
        )
        title_label.pack(pady=20)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Sélectionnez vos fichiers Excel et générez le rapport Word",
            font=("Calibri", 10),
            fg="white",
            bg="#0099CC"
        )
        subtitle_label.pack()
        
        # === Main Content ===
        main_frame = tk.Frame(root, bg="#F5F5F5")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # --- Zone sélection fichiers ---
        file_frame = tk.LabelFrame(
            main_frame,
            text="📁 Fichiers Excel",
            font=("Calibri", 11, "bold"),
            bg="#F5F5F5",
            fg="#0099CC",
            padx=15,
            pady=15
        )
        file_frame.pack(fill="x", pady=10)
        
        self.file_listbox = tk.Listbox(
            file_frame,
            height=6,
            font=("Calibri", 10),
            bg="white",
            relief="solid",
            borderwidth=1
        )
        self.file_listbox.pack(fill="both", expand=True)
        
        # Boutons fichiers
        button_frame = tk.Frame(file_frame, bg="#F5F5F5")
        button_frame.pack(fill="x", pady=10)
        
        self.browse_btn = tk.Button(
            button_frame,
            text="➕ Ajouter fichiers",
            command=self.select_files,
            bg="#0099CC",
            fg="white",
            font=("Calibri", 10, "bold"),
            padx=15,
            pady=8
        )
        self.browse_btn.pack(side="left", padx=5)
        
        self.remove_btn = tk.Button(
            button_frame,
            text="🗑️ Supprimer sélectionné",
            command=self.remove_selected,
            bg="#F44336",
            fg="white",
            font=("Calibri", 10, "bold"),
            padx=15,
            pady=8
        )
        self.remove_btn.pack(side="left", padx=5)
        
        self.clear_btn = tk.Button(
            button_frame,
            text="🔄 Effacer tout",
            command=self.clear_all,
            bg="#FF9800",
            fg="white",
            font=("Calibri", 10, "bold"),
            padx=15,
            pady=8
        )
        self.clear_btn.pack(side="left", padx=5)
        
        # --- Info fichiers ---
        info_frame = tk.Frame(file_frame, bg="#E3F2FD")
        info_frame.pack(fill="x", pady=10)
        
        self.info_label = tk.Label(
            info_frame,
            text="ℹ️ Aucun fichier sélectionné",
            font=("Calibri", 9),
            bg="#E3F2FD",
            fg="#0099CC",
            wraplength=600,
            justify="left"
        )
        self.info_label.pack(anchor="w", padx=10, pady=10)
        
        # --- Bouton Générer ---
        generate_frame = tk.Frame(main_frame, bg="#F5F5F5")
        generate_frame.pack(fill="x", pady=20)
        
        self.generate_btn = tk.Button(
            generate_frame,
            text="📄 GÉNÉRER LE RAPPORT",
            command=self.generate_report,
            bg="#4CAF50",
            fg="white",
            font=("Calibri", 14, "bold"),
            padx=30,
            pady=12,
            cursor="hand2"
        )
        self.generate_btn.pack(fill="x")

        # --- Bouton Aide ---
        help_btn = tk.Button(
            button_frame,
            text="ℹ️ Aide",
            command=self.show_help,
            bg="#2196F3",
            fg="white",
            font=("Calibri", 10, "bold"),
            padx=15,
            pady=8
        )
        help_btn.pack(side="right", padx=5)

   
        
        # --- Barre progression ---
        progress_frame = tk.Frame(main_frame, bg="#F5F5F5")
        progress_frame.pack(fill="x", pady=10)
        
        self.progress_label = tk.Label(
            progress_frame,
            text="",
            font=("Calibri", 10),
            bg="#F5F5F5",
            fg="#666666"
        )
        self.progress_label.pack(anchor="w")
        
        # --- Logs ---
        log_frame = tk.LabelFrame(
            main_frame,
            text="📝 Logs",
            font=("Calibri", 11, "bold"),
            bg="#F5F5F5",
            fg="#0099CC",
            padx=10,
            pady=10
        )
        log_frame.pack(fill="both", expand=True, pady=10)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            height=6,
            font=("Courier", 9),
            bg="white",
            relief="solid",
            borderwidth=1,
            state="disabled"
        )
        self.log_text.pack(fill="both", expand=True)
        
        # === Footer ===
        footer_frame = tk.Frame(root, bg="#F5F5F5", height=40)
        footer_frame.pack(fill="x", padx=20, pady=10)
        footer_frame.pack_propagate(False)
        
        footer_label = tk.Label(
            footer_frame,
            text="Service de Santé Universitaire - Université d'Angers",
            font=("Calibri", 9),
            fg="#666666",
            bg="#F5F5F5"
        )
        footer_label.pack()
    
    def select_files(self):
        """Ouvre la boîte de dialogue pour sélectionner les fichiers"""
        files = filedialog.askopenfilenames(
            title="Sélectionnez les fichiers de données Excel",
            filetypes=[("Fichiers Excel", "*.xlsx *.xls"), ("Tous les fichiers", "*.*")],
            initialdir="data/raw"
        )
        
        if files:
            for file in files:
                if file not in self.selected_files:
                    self.selected_files.append(file)
            self.update_file_list()
    
    def remove_selected(self):
        """Supprime les fichiers sélectionnés de la liste"""
        selection = self.file_listbox.curselection()
        for index in reversed(selection):
            del self.selected_files[index]
        self.update_file_list()
    
    def clear_all(self):
        """Efface tous les fichiers"""
        self.selected_files = []
        self.update_file_list()

    def show_help(self):
        """Affiche l'aide"""
        matcher = FileMatcher()
        
        required = "\n".join([f"  • {f}" for f in matcher.get_required_files()])
        optional = "\n".join([f"  • {f}" for f in matcher.get_optional_files()])
        
        help_text = f"""
    📋 FICHIERS ATTENDUS :

    ✓ OBLIGATOIRES (vous devez en avoir) :
    {required}

    ✓ OPTIONNELS (si vous les avez) :
    {optional}

    💡 Les noms n'importent pas ! 
    L'application reconnaît les fichiers automatiquement.

    Exemple :
    • "effectifs.xlsx" ✓
    • "evolution_etab_conventionnes.xlsx" ✓
    • "données_effectifs_2024.xlsx" ✓
    → Tous sont reconnus !

    ⚠️ Assurez-vous que :
    1. Les fichiers sont dans data/raw
    2. Ce sont des fichiers Excel (.xlsx)
    3. Vous avez tous les fichiers OBLIGATOIRES
    """
        
        messagebox.showinfo("Aide - Fichiers attendus", help_text)
    
    def update_file_list(self):
        """Met à jour l'affichage de la liste des fichiers"""
        self.file_listbox.delete(0, tk.END)
        
        for file in self.selected_files:
            filename = os.path.basename(file)
            self.file_listbox.insert(tk.END, filename)
        
        # Met à jour l'info
        if self.selected_files:
            self.info_label.config(
                text=f"✅ {len(self.selected_files)} fichier(s) sélectionné(s)"
            )
        else:
            self.info_label.config(
                text="ℹ️ Aucun fichier sélectionné"
            )
    
    def log(self, message):
        """Ajoute un message aux logs"""
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")
        self.root.update()
    
    def generate_report(self):
        """Lance la génération du rapport"""
        if not self.selected_files:
            messagebox.showerror(
                "Erreur",
                "❌ Veuillez sélectionner au moins un fichier Excel !"
            )
            return
        
        # Essaie de matcher les fichiers
        try:
            matcher = FileMatcher()
            matched_files = matcher.match_files(self.selected_files)
            
            # Affiche ce qui a été trouvé
            summary = "Fichiers reconnus :\n\n"
            for role, filepath in matched_files.items():
                summary += f"✓ {role}\n   → {os.path.basename(filepath)}\n\n"
            
            if messagebox.askokcancel("Confirmation", summary + "\nContinuer la génération ?"):
                self._start_generation(matched_files)
            else:
                self.log("❌ Génération annulée par l'utilisateur")
            
        except ValueError as e:
            messagebox.showerror("Erreur", f"❌ Erreur dans les fichiers :\n\n{str(e)}")
            self.log(f"❌ Erreur : {str(e)}")

    def _start_generation(self, matched_files):
        """Démarre la génération en thread"""
        if self.is_generating:
            messagebox.showwarning(
                "Attention",
                "⏳ La génération est déjà en cours..."
            )
            return
        
        self.is_generating = True
        self.generate_btn.config(state="disabled")
        self.browse_btn.config(state="disabled")
        self.progress_label.config(text="⏳ Génération en cours...", fg="#FF9800")
        
        # Lance en thread
        thread = threading.Thread(target=self._generate_thread)
        thread.daemon = True
        thread.start()
    
    def _generate_thread(self):
        """Génère le rapport en arrière-plan"""
        try:
            self.log("=" * 60)
            self.log("🚀 Démarrage de la génération du rapport...")
            self.log(f"📁 Fichiers trouvés : {len(self.selected_files)}")
            
            for file in self.selected_files:
                self.log(f"  - {os.path.basename(file)}")
            
            self.log("")
            self.log("⏳ Traitement en cours...")
            
            # Appelle le script principal
            generate_report()
            
            self.log("")
            self.log("✅ Rapport généré avec succès !")
            self.log("📄 Fichier : output/rapport_ssu_2024_2025.docx")
            self.log("=" * 60)
            
            self.progress_label.config(
                text="✅ Rapport généré avec succès !",
                fg="#4CAF50"
            )
            
            messagebox.showinfo(
                "✅ Succès !",
                "Le rapport a été généré avec succès !\n\n"
                "📁 Fichier : output/rapport_ssu_2024_2025.docx"
            )
            
        except Exception as e:
            self.log("")
            self.log(f"❌ ERREUR : {str(e)}")
            self.log("=" * 60)
            
            self.progress_label.config(
                text="❌ Erreur lors de la génération",
                fg="#F44336"
            )
            
            messagebox.showerror(
                "❌ Erreur !",
                f"Erreur lors de la génération :\n\n{str(e)}"
            )
        
        finally:
            self.is_generating = False
            self.generate_btn.config(state="normal")
            self.browse_btn.config(state="normal")


def main():
    """Point d'entrée de l'application"""
    root = tk.Tk()
    app = SSUReportGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()