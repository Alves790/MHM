import customtkinter as ctk
from tkinter import messagebox, simpledialog
from gestion_salles import (ajouter_salle, rechercher_salle, attribuer_salle, liberer_salle, modifier_salle, afficher_salles, tri_salles, supprimer_salle, Salles)

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

class FenetreGestionSalles(ctk.CTkToplevel):
    def __init__(self, menu_principal):
        super().__init__()
        self.title("MEDTECH HEALTH MANAGER-Gestion des Salles")
        self.geometry("800x600")
        self.configure(fg_color="#E0F7FA")
        self.menu_principal = menu_principal

        cadre_ajout = ctk.CTkFrame(self, corner_radius=10)
        cadre_ajout.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        cadre_ajout.columnconfigure(1, weight=1)

        titre_ajout = ctk.CTkLabel(cadre_ajout, text="Ajouter une salle", font=("Arial", 14, "bold"))
        titre_ajout.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        champs = [
            ("Nom de la salle:", 1), ("Type de salle:", 2), ("Capacité maximale:", 3),
            ("Équipements (séparés par des virgules):", 4)
        ]
        self.entrees = {}
        for i, (texte, row) in enumerate(champs):
            label = ctk.CTkLabel(cadre_ajout, text=texte)
            label.grid(row=row, column=0, padx=5, pady=5, sticky="w")
            entree = ctk.CTkEntry(cadre_ajout)
            entree.grid(row=row, column=1, padx=5, pady=5, sticky="ew")
            self.entrees[texte] = entree

        bouton_ajouter = ctk.CTkButton(cadre_ajout, text="Ajouter une salle", command=self.ajouter_salle)
        bouton_ajouter.grid(row=5, column=0, columnspan=2, pady=10)

        cadre_liste = ctk.CTkFrame(self, corner_radius=10)
        cadre_liste.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        titre_liste = ctk.CTkLabel(cadre_liste, text="Liste des salles enregistrées", font=("Arial", 14, "bold"))
        titre_liste.grid(row=0, column=0, pady=(5, 10))

        self.zone_salles = ctk.CTkTextbox(cadre_liste, height=350, width=500)
        self.zone_salles.grid(row=1, column=0, padx=5, pady=5)

        bouton_actualiser = ctk.CTkButton(cadre_liste, text="Actualiser", command=self.afficher_liste_salles)
        bouton_actualiser.grid(row=2, column=0, pady=10)

        cadre_details = ctk.CTkFrame(self, corner_radius=10)
        cadre_details.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        titre_details = ctk.CTkLabel(cadre_details, text="Détails de la salle", font=("Arial", 14, "bold"))
        titre_details.grid(row=0, column=0, pady=(5, 10))

        self.zone_details = ctk.CTkTextbox(cadre_details, height=300, width=450)
        self.zone_details.grid(row=1, column=0, padx=5, pady=5)

        bouton_details = ctk.CTkButton(cadre_details, text="Afficher les détails", command=self.afficher_details)
        bouton_details.grid(row=2, column=0, pady=10)

        cadre_actions = ctk.CTkFrame(self, corner_radius=10)
        cadre_actions.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        titre_actions = ctk.CTkLabel(cadre_actions, text="Actions", font=("Arial", 14, "bold"))
        titre_actions.grid(row=0, column=0, pady=(5, 10))

        bouton_attribuer = ctk.CTkButton(cadre_actions, text="Attribuer une salle", command=self.attribuer_salle)
        bouton_attribuer.grid(row=1, column=0, padx=5, pady=5)

        bouton_liberer = ctk.CTkButton(cadre_actions, text="Libérer une salle", command=self.liberer_salle)
        bouton_liberer.grid(row=2, column=0, padx=5, pady=5)

        bouton_modifier = ctk.CTkButton(cadre_actions, text="Modifier une salle", command=self.modifier_salle)
        bouton_modifier.grid(row=3, column=0, padx=5, pady=5)

        bouton_supprimer = ctk.CTkButton(cadre_actions, text="Supprimer une salle", command=self.supprimer_salle)
        bouton_supprimer.grid(row=4, column=0, padx=5, pady=5)

        bouton_retour = ctk.CTkButton(cadre_actions, text="Retour au menu principal", command=self.retour_menu_principal)
        bouton_retour.grid(row=5, column=0, padx=5, pady=5)

    def ajouter_salle(self):
        nom = self.entrees["Nom de la salle:"].get()
        type_salle = self.entrees["Type de salle:"].get()
        capacite_max = self.entrees["Capacité maximale:"].get()
        equipements = self.entrees["Équipements (séparés par des virgules):"].get().split(",")
        if nom and type_salle and capacite_max:
            try:
                capacite_max = int(capacite_max)
                resultat = ajouter_salle(Salles, nom, type_salle, capacite_max, capacite_max, "disponible", equipements)
                messagebox.showinfo("Succès", resultat)
                self.afficher_liste_salles()
                for entree in self.entrees.values():
                    entree.delete(0, ctk.END)
            except ValueError:
                messagebox.showwarning("Erreur", "La capacité maximale doit être un nombre entier.")
        else:
            messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")

    def afficher_liste_salles(self):
        self.zone_salles.delete(1.0, ctk.END)
        salles = afficher_salles(Salles)
        if isinstance(salles, list):
            for salle in salles:
                self.zone_salles.insert(ctk.END, f"Nom: {salle['nom']}, Type: {salle['type']}, Statut: {salle['statut']}\n")
        else:
            self.zone_salles.insert(ctk.END, salles)

    def afficher_details(self):
        nom_salle = simpledialog.askstring("Rechercher", "Entrez le nom de la salle:")
        if nom_salle:
            salle = rechercher_salle(Salles, nom_salle)
            if isinstance(salle, dict):
                self.zone_details.delete(1.0, ctk.END)
                self.zone_details.insert(ctk.END, f"Nom: {salle['nom']}\n")
                self.zone_details.insert(ctk.END, f"Type: {salle['type']}\n")
                self.zone_details.insert(ctk.END, f"Capacité max: {salle['capacite_max']}\n")
                self.zone_details.insert(ctk.END, f"Capacité actuelle: {len(salle['patients'])}\n")
                self.zone_details.insert(ctk.END, f"Statut: {salle['statut']}\n")
                self.zone_details.insert(ctk.END, f"Équipements: {', '.join(salle['equipements'])}\n")
                self.zone_details.insert(ctk.END, f"Patients: {(salle['patients'])}\n")
            else:
                messagebox.showwarning("Erreur", salle)

    def attribuer_salle(self):
        nom_salle = simpledialog.askstring("Attribuer", "Entrez le nom de la salle")
        patient_id = simpledialog.askinteger("Attribuer", "Entrez l'ID du patient:")
        patient_nom = simpledialog.askstring("Attribuer", "Entrez le nom du patient:")
        if nom_salle and patient_id and patient_nom:
            patient = (patient_id, patient_nom)
            resultat = attribuer_salle(Salles, nom_salle, patient)
            messagebox.showinfo("Résultat", resultat)
            self.afficher_liste_salles()
        else:
            messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")

    def liberer_salle(self):
        nom_salle = simpledialog.askstring("Libérer", "Entrez le nom de la salle")
        patient_id = simpledialog.askinteger("Libérer", "Entrez l'ID du patient:")
        patient_nom = simpledialog.askstring("Libérer", "Entrez le nom du patient:")
        if nom_salle and patient_id and patient_nom:
            patient = (patient_id, patient_nom)
            resultat = liberer_salle(Salles, nom_salle, patient)
            messagebox.showinfo("Résultat", resultat)
            self.afficher_liste_salles()
        else:
            messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")

    def modifier_salle(self):
        nom_salle = simpledialog.askstring("Modifier", "Entrez le nom de la salle")
        nouveau_type = simpledialog.askstring("Modifier", "Nouveau type de salle:")
        nouvelle_capacite_max = simpledialog.askstring("Modifier", "Nouvelle capacité maximale:")
        nouveaux_equipements = simpledialog.askstring("Modifier", "Nouveaux équipements (séparés par des virgules):")
        if nom_salle:
            try:
                nouvelle_capacite_max = int(nouvelle_capacite_max) if nouvelle_capacite_max else None
                nouveaux_equipements = nouveaux_equipements.split(",") if nouveaux_equipements else None
                resultat = modifier_salle(Salles, nom_salle, nouveau_type, nouvelle_capacite_max, nouveaux_equipements)
                messagebox.showinfo("Résultat", resultat)
                self.afficher_liste_salles()
            except ValueError:
                messagebox.showwarning("Erreur", "La capacité maximale doit être un nombre entier.")
        else:
            messagebox.showwarning("Erreur", "Veuillez entrer le nom de la salle.")

    def supprimer_salle(self):
        nom_salle = simpledialog.askstring("Supprimer", "Entrez le nom de la salle")
        if nom_salle:
            resultat = supprimer_salle(Salles, nom_salle)
            messagebox.showinfo("Résultat", resultat)
            self.afficher_liste_salles()
        else:
            messagebox.showwarning("Erreur", "Veuillez entrer le nom de la salle.")

    def retour_menu_principal(self):
        self.destroy()
        self.menu_principal.deiconify()