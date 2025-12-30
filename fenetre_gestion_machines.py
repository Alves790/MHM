import customtkinter as ctk
from tkinter import messagebox, simpledialog
from gestion_machines import (ajouter_machine, modifier_etat_machine, supprimer_machine, afficher_machines, rechercher_machine, attribuer_machine, liberer_machine, equipements, machines)

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

class FenetreGestionMachines(ctk.CTkToplevel):
    def __init__(self, menu_principal):
        super().__init__()
        self.title("MEDTECH HEALTH MANAGER-Gestion des Machines")
        self.geometry("700x640")
        self.configure(fg_color="#E0F7FA")
        self.menu_principal = menu_principal

        cadre_ajout = ctk.CTkFrame(self, corner_radius=10)
        cadre_ajout.grid(row=0, column=0, padx=0, pady=2, sticky="ew")
        cadre_ajout.columnconfigure(1, weight=1)

        titre_ajout = ctk.CTkLabel(cadre_ajout, text="Ajouter une Machine", font=("Arial", 14, "bold"))
        titre_ajout.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        champs = [
            ("ID de la machine:", 1), ("Nom de la machine:", 2), ("Etat de la machine (Disponible/Occupée/Maintenance):", 3)
        ]
        self.entrees = {}
        for i, (texte, row) in enumerate(champs):
            label = ctk.CTkLabel(cadre_ajout, text=texte)
            label.grid(row=row, column=0, padx=5, pady=5, sticky="w")
            entree = ctk.CTkEntry(cadre_ajout)
            entree.grid(row=row, column=1, padx=5, pady=5, sticky="ew")
            self.entrees[texte] = entree

        bouton_ajouter = ctk.CTkButton(cadre_ajout, text="Ajouter Machine", command=self.ajouter_machine)
        bouton_ajouter.grid(row=4, column=0, columnspan=2, pady=10)

        cadre_liste = ctk.CTkFrame(self, corner_radius=10)
        cadre_liste.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        titre_liste = ctk.CTkLabel(cadre_liste, text="Liste des machines enregistrées", font=("Arial", 14, "bold"))
        titre_liste.grid(row=0, column=0, pady=(5, 10))

        self.zone_machines = ctk.CTkTextbox(cadre_liste, height=350, width=450)
        self.zone_machines.grid(row=1, column=0, padx=5, pady=5)

        bouton_actualiser = ctk.CTkButton(cadre_liste, text="Actualiser", command=self.afficher_liste_machines)
        bouton_actualiser.grid(row=2, column=0, pady=10)

        cadre_actions = ctk.CTkFrame(self, corner_radius=10)
        cadre_actions.grid(row=0, column=4, pady=10)
        titre_actions = ctk.CTkLabel(cadre_actions, text="Actions", font=("Arial", 14, "bold"))
        titre_actions.grid(row=0, column=0, pady=(5, 10))

        bouton_changer_etat = ctk.CTkButton(cadre_actions, text="Mise à jour de l'etat d'une machine", command=self.changer_etat)
        bouton_changer_etat.grid(row=1, column=0, padx=5, pady=5)

        bouton_rechercher_machine = ctk.CTkButton(cadre_actions, text="Rechercher une machine", command=self.rechercher_machine)
        bouton_rechercher_machine.grid(row=2, column=0, padx=5, pady=5)

        bouton_supprimer_machine = ctk.CTkButton(cadre_actions, text="Supprimer une machine", command=self.supprimer_machine)
        bouton_supprimer_machine.grid(row=3, column=0, padx=5, pady=5)

        bouton_attribuer_machine = ctk.CTkButton(cadre_actions, text="Attribuer une machine", command=self.attribuer_machine)
        bouton_attribuer_machine.grid(row=4, column=0, padx=5, pady=5)

        bouton_liberer_machine = ctk.CTkButton(cadre_actions, text="Liberer une machine", command=self.liberer_machine)
        bouton_liberer_machine.grid(row=5, column=0, padx=5, pady=5)

        bouton_retour = ctk.CTkButton(cadre_actions, text="Retour au menu principal", command=self.retour_menu_principal)
        bouton_retour.grid(row=6, column=0, padx=5, pady=5)

    def ajouter_machine(self):
        id_machine = self.entrees["ID de la machine:"].get()
        nom = self.entrees["Nom de la machine:"].get()
        etat = self.entrees["Etat de la machine (Disponible/Occupée/Maintenance):"].get()
        if id_machine and nom:
            ajouter_machine(machines, id_machine, nom, etat)
            messagebox.showinfo("Succès", f"Machine {nom} identifiée {id_machine} enregistrée")
            self.afficher_liste_machines()
            for entree in self.entrees.values():
                entree.delete(0, ctk.END)
        else:
            messagebox.showwarning("Erreur", "Remplissez les champs vides")

    def afficher_liste_machines(self):
        self.zone_machines.delete(1.0, ctk.END)
        for machine in machines:
            self.zone_machines.insert(ctk.END, f"--->ID: {machine['id_machine']}, Nom: {machine['nom']}, Etat: {machine['etat']}\n")

    def changer_etat(self):
        id_machine = simpledialog.askstring("Mise à jour", "ID de la machine")
        if id_machine:
            nouvel_etat = simpledialog.askstring("Mise à jour", "Nouvel état de la machine")
            if nouvel_etat:
                resultat = modifier_etat_machine(machines, id_machine, nouvel_etat)
                messagebox.showinfo("Résultat", resultat)
            else:
                messagebox.showwarning("Erreur", "Remplissez les champs")
        self.afficher_liste_machines()

    def rechercher_machine(self):
        id_machine = simpledialog.askstring("Rechercher", "ID de la machine")
        if id_machine:
            lieu = simpledialog.askstring("Rechercher", "Vous cherchez la machine dans les équipements(1) ou dans la liste des machines(2)?")
            if lieu == "1":
                resultat = rechercher_machine(equipements, "id_machine", id_machine)
                messagebox.showinfo("Résultat", resultat)
            elif lieu == "2":
                resultat = rechercher_machine(machines, "id_machine", id_machine)
                messagebox.showinfo("Résultat", resultat)
            else:
                messagebox.showwarning("Erreur", "Choix invalide")
        else:
            messagebox.showwarning("Erreur", "Entrer l'ID")

    def supprimer_machine(self):
        id_machine = simpledialog.askstring("Suppression", "ID de la machine")
        if id_machine:
            resultat = supprimer_machine(machines, id_machine)
            messagebox.showinfo("Résultat", resultat)
            self.afficher_liste_machines()
        else:
            messagebox.showwarning("Erreur", "Saisissez l'ID de la machine")

    def attribuer_machine(self):
        id_machine = simpledialog.askstring("Affectation", "ID de la machine")
        if id_machine:
            resultat = attribuer_machine(equipements, id_machine)
            messagebox.showinfo("Resultat", resultat)
            self.afficher_liste_machines()
        else:
            messagebox.showwarning("Erreur", "Entrez l'ID")

    def liberer_machine(self):
        id_machine = simpledialog.askstring("Libération", "ID de la machine")
        if id_machine:
            resultat = liberer_machine(equipements, id_machine)
            messagebox.showinfo("Résultat", resultat)
            self.afficher_liste_machines()
        else:
            messagebox.showwarning("Erreur", "Entrez l'ID")

    def retour_menu_principal(self):
        self.destroy()
        self.menu_principal.deiconify()