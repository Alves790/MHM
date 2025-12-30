import customtkinter as ctk
from fenetre_gestion_patients import FenetreGestionPatients
from fenetre_gestion_machines import FenetreGestionMachines
from fenetre_gestion_salles import FenetreGestionSalles

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

class MenuPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("MEDTECH HEALTH MANAGER")
        self.geometry("400x300")
        self.configure(fg_color="#E0F7FA")

        self.titre = ctk.CTkLabel(self, text="Menu Principal", font=("Arial", 20))
        self.titre.pack(pady=20)

        self.bouton_gestion_patients = ctk.CTkButton(self, text="Gestion des Patients", command=self.ouvrir_gestion_patients)
        self.bouton_gestion_patients.pack(pady=10)

        self.bouton_gestion_machines = ctk.CTkButton(self, text="Gestion des Machines", command=self.ouvrir_gestion_machines)
        self.bouton_gestion_machines.pack(pady=10)

        self.bouton_gestion_salles = ctk.CTkButton(self, text="Gestion des Salles", command=self.ouvrir_gestion_salles)
        self.bouton_gestion_salles.pack(pady=10)

        self.bouton_quitter = ctk.CTkButton(self, text="Quitter", command=self.destroy)
        self.bouton_quitter.pack(pady=20)

    def ouvrir_gestion_patients(self):
        self.withdraw()
        FenetreGestionPatients(self)

    def ouvrir_gestion_machines(self):
        self.withdraw()
        FenetreGestionMachines(self)

    def ouvrir_gestion_salles(self):
        self.withdraw()
        FenetreGestionSalles(self)

if __name__ == "__main__":
    app = MenuPrincipal()
    app.mainloop()