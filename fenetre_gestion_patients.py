import customtkinter as ctk
from tkinter import messagebox, simpledialog
from gestion_patients import (ajouter_patient, ajouter_un_rappel, effectuer_consultation, afficher_patients_enregistres, rechercher_patient, patients)

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

class FenetreGestionPatients(ctk.CTkToplevel):
    def __init__(self, menu_principal):
        super().__init__()
        self.title("MEDTECH HEALTH MANAGER-Gestion des Patients")
        self.geometry("1000x700")
        self.configure(fg_color="#E0F7FA")
        self.menu_principal = menu_principal

        cadre_ajout = ctk.CTkFrame(self, corner_radius=10)
        cadre_ajout.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        cadre_ajout.columnconfigure(1, weight=1)

        titre_ajout = ctk.CTkLabel(cadre_ajout, text="Ajouter un patient", font=("Arial", 14, "bold"))
        titre_ajout.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        champs = [
            ("Nom:", 1), ("Prénom:", 2), ("Age:", 3), ("Adresse:", 4),
            ("Telephone:", 5), ("Groupe Sanguin:", 6), ("Allergies:", 7),
            ("Antécédents:", 8), ("Sexe:", 9)
        ]
        self.entrees = {}
        for i, (texte, row) in enumerate(champs):
            label = ctk.CTkLabel(cadre_ajout, text=texte)
            label.grid(row=row, column=0, padx=5, pady=5, sticky="w")
            entree = ctk.CTkEntry(cadre_ajout)
            entree.grid(row=row, column=1, padx=5, pady=5, sticky="ew")
            self.entrees[texte] = entree

        bouton_ajouter = ctk.CTkButton(cadre_ajout, text="Ajouter patient", command=self.ajouter_patient)
        bouton_ajouter.grid(row=10, column=0, columnspan=2, pady=10)

        cadre_liste = ctk.CTkFrame(self, corner_radius=10)
        cadre_liste.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        titre_liste = ctk.CTkLabel(cadre_liste, text="Liste des patients enregistrés", font=("Arial", 14, "bold"))
        titre_liste.grid(row=0, column=0, pady=(5, 10))

        self.zone_patients = ctk.CTkTextbox(cadre_liste, height=150, width=250)
        self.zone_patients.grid(row=1, column=0, padx=5, pady=5)

        bouton_actualiser = ctk.CTkButton(cadre_liste, text="Actualiser", command=self.afficher_liste_patients)
        bouton_actualiser.grid(row=2, column=0, pady=10)

        cadre_details = ctk.CTkFrame(self, corner_radius=10)
        cadre_details.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        titre_details = ctk.CTkLabel(cadre_details, text="Détails du Patient", font=("Arial", 14, "bold"))
        titre_details.grid(row=0, column=0, pady=(5, 10))

        self.zone_details = ctk.CTkTextbox(cadre_details, height=400, width=600)
        self.zone_details.grid(row=1, column=0, padx=5, pady=5)

        bouton_details = ctk.CTkButton(cadre_details, text="Afficher les Détails", command=self.afficher_details)
        bouton_details.grid(row=2, column=0, pady=10)

        cadre_actions = ctk.CTkFrame(self, corner_radius=10)
        cadre_actions.grid(row=0, column=2, padx=10, pady=10)
        titre_actions = ctk.CTkLabel(cadre_actions, text="Actions", font=("Arial", 14, "bold"))
        titre_actions.grid(row=0, column=0, pady=(5, 10))

        bouton_consultation = ctk.CTkButton(cadre_actions, text="Ajouter Consultation", command=self.ajouter_consultation)
        bouton_consultation.grid(row=1, column=0, padx=5, pady=5)

        bouton_rappel = ctk.CTkButton(cadre_actions, text="Ajouter Rappel", command=self.ajouter_rappel)
        bouton_rappel.grid(row=2, column=0, padx=5, pady=5)

        bouton_retour = ctk.CTkButton(cadre_actions, text="Retour au menu principal", command=self.retour_menu_principal)
        bouton_retour.grid(row=3, column=0, padx=5, pady=5)

    def ajouter_patient(self):
        nom = self.entrees["Nom:"].get()
        prenom = self.entrees["Prénom:"].get()
        age = self.entrees["Age:"].get()
        sexe = self.entrees["Sexe:"].get()
        adresse = self.entrees["Adresse:"].get()
        telephone = self.entrees["Telephone:"].get()
        groupe_sanguin = self.entrees["Groupe Sanguin:"].get()
        allergies = self.entrees["Allergies:"].get()
        antecedents = self.entrees["Antécédents:"].get()

        if nom and prenom and age:
            ajouter_patient(patients, nom, prenom, int(age), sexe, adresse, telephone, groupe_sanguin, [allergies], [antecedents])
            messagebox.showinfo("Succès", f"Patient {nom} {prenom} enregistré")
            self.afficher_liste_patients()
            for entree in self.entrees.values():
                entree.delete(0, ctk.END)
        else:
            messagebox.showwarning("Erreur", "Remplissez les champs vides")

    def afficher_liste_patients(self):
        self.zone_patients.delete(1.0, ctk.END)
        for patient in patients:
            self.zone_patients.insert(ctk.END, f"ID: {patient['id']}, Nom: {patient['Nom']}, Prénom: {patient['Prenom']}\n")

    def afficher_details(self):
        id_patient = simpledialog.askinteger("Rechercher", "Entrez l'ID du patient:")
        if id_patient:
            patient = rechercher_patient(patients, "id", id_patient)
            if patient:
                self.zone_details.delete(1.0, ctk.END)
                self.zone_details.insert(ctk.END, f"Nom: {patient['Nom']}\n")
                self.zone_details.insert(ctk.END, f"Prénom: {patient['Prenom']}\n")
                self.zone_details.insert(ctk.END, f"Âge: {patient['Age']}\n")
                self.zone_details.insert(ctk.END, f"Sexe: {patient['Sexe']}\n")
                self.zone_details.insert(ctk.END, f"Telephone: {patient['Telephone']}\n")
                self.zone_details.insert(ctk.END, f"Adresse: {patient['Adresse']}\n")
                self.zone_details.insert(ctk.END, f"Allergies: {', '.join(patient['allergies'])}\n")
                self.zone_details.insert(ctk.END, f"Antécédents: {', '.join(patient['antecedents'])}\n")
                self.zone_details.insert(ctk.END, f"Goupe Sanguin: {patient['groupe_sanguin'][0:-1:1]} Rhésus:{' '.join(patient['groupe_sanguin'][-1])}\n")
                self.zone_details.insert(ctk.END, "\nConsultations:\n")
                for consultation in patient["consultations"]:
                    self.zone_details.insert(ctk.END, f"--->{consultation['date']}\n°diagnostic:{consultation['diagnostic']}\n°prescriptions: {consultation['traitement']} \n°médécin traitant:{consultation['medecin_traitant']}\n")
                self.zone_details.insert(ctk.END, "\nRappels:\n")
                for rappel in patient["rappels"]:
                    self.zone_details.insert(ctk.END, f"--->{rappel['heure']} : {rappel['medicament']} ({rappel['posologie']})\n")
            else:
                messagebox.showwarning("Erreur", "Patient non trouvé.")

    def ajouter_consultation(self):
        id_patient = simpledialog.askinteger("Consultation", "Entrez l'ID du patient:")
        if id_patient:
            date = simpledialog.askstring("Consultation", "Date (AAAA-MM-JJ):")
            medecin = simpledialog.askstring("Consultation", "Nom du médecin:")
            diagnostic = simpledialog.askstring("Consultation", "Diagnostic:")
            traitement = simpledialog.askstring("Consultation", "Traitement prescrit:")
            if date and medecin and diagnostic and traitement:
                if effectuer_consultation(patients, id_patient, date, medecin, diagnostic, traitement):
                    messagebox.showinfo("Succès", "Consultation ajoutée !")
                else:
                    messagebox.showwarning("Erreur", "Patient non trouvé.")
            else:
                messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")

    def ajouter_rappel(self):
        id_patient = simpledialog.askinteger("Rappel", "Entrez l'ID du patient:")
        if id_patient:
            medicament = simpledialog.askstring("Rappel", "Médicament:")
            posologie = simpledialog.askstring("Rappel", "Posologie:")
            heure = simpledialog.askstring("Rappel", "Heure (HH:MM):")
            if medicament and posologie and heure:
                if ajouter_un_rappel(patients, id_patient, medicament, posologie, heure):
                    messagebox.showinfo("Succès", "Rappel ajouté !")
                else:
                    messagebox.showwarning("Erreur", "Patient non trouvé.")
            else:
                messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")

    def retour_menu_principal(self):
        self.destroy()
        self.menu_principal.deiconify()