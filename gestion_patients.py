patients=[]
def ajouter_patient(patients,nom,prenom,age,sexe,adresse,telephone,groupe_sanguin,allergies,antecedents):
    nouveau_patient={
        "id":len(patients)+1 ,
        "Nom":nom,
        "Prenom":prenom,
        "Age":age,
        "Sexe":sexe,
        "Adresse":adresse,
        "Telephone":telephone,
        "groupe_sanguin": groupe_sanguin,
        "allergies": allergies,
        "antecedents": antecedents,
        "consultations": [],
        "traitements": [],
        "rappels": []}
    patients.append(nouveau_patient)
    return nouveau_patient
patient1 = ajouter_patient(patients, "Abena", "Jean", 35, "M", "Ndokoti", "655435678", "A+", ["pollen"], ["asthme","cholera"])
print(patients)

def afficher_patients_enregistres(patients):
    for patient in patients:
        print(f"ID: {patient["id"]}, Nom:{patient["Nom"]}, Prénom:{patient["Prenom"]}, Âge:{patient["Age"]}ans")
afficher_patients_enregistres(patients)

def rechercher_patient(patients,critere,valeur):
    patient_present=False
    for patient in patients:
        if patient[critere]==valeur:
            patient_present=True
            pt=patient
    if patient_present:
        return pt
    else:
        return f"Patient non trouvé,essayez d'autres criteres"
print(rechercher_patient(patients,"Age",35))

def effectuer_consultation(patients,id_patient,date,medecin,diagnostic,traitement):
    for patient in patients:
        if patient["id"]==id_patient:
            consultation={
                "date":date,
                "medecin_traitant":medecin,
                "diagnostic":diagnostic,
                "traitement":traitement,
            }
            patient["consultations"].append(consultation)
            return consultation
    return None
effectuer_consultation(patients,patient1["id"],"2025-10-01","Dr.Angon","Grippe","Doliprane")
print(patient1["consultations"])

def ajouter_un_rappel(patients,id_patient,medicament,posologie,heure):
    for patient in patients:
        if patient["id"]==id_patient:
            rappel={
                "medicament":medicament,
                "posologie":posologie,
                "heure":heure,
            }
            patient["rappels"].append(rappel)
            return rappel
    return None
ajouter_un_rappel(patients,patient1["id"],"Doliprane","1000Mg","12H30")
print(patient1['rappels'])


#PS:rajouter 3 patients et supprimer les informations de P1 et tester dans jupyter
#Toutes les tester en ordre ajout de patients
#consultations et rappels
#affichage de la liste