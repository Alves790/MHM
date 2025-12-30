Salles = []

def ajouter_salle(Salles, nom, categorie,capacite_max=None, statut="", equipements=[]):
    for salle in Salles:
        if salle["nom"] == nom:
            return "Erreur, la salle existe déjà!"
    nouvelle_salle = {
        "nom": nom,
        "type": categorie,
        "capacite_actuelle":0,
        "capacite_max": capacite_max,
        "statut": statut,
        "equipements": equipements,
        "patients": []
    }
    Salles.append(nouvelle_salle)
    return f"Salle {nom} de catégorie {categorie} ajoutée."

def rechercher_salle(Salles, nom):
    for salle in Salles:
        if salle["nom"] == nom:
            return salle
    return "Erreur: Salle inexistante."

def attribuer_salle(Salles, nom,patient):
    for salle in Salles:
        if salle["nom"] == nom:
            if salle["statut"] =="pleine":
                return "Erreur: La salle est pleine."
            else:
                salle["patients"].append(patient)
                cap_res=salle['capacite_max']-len(salle['patients'])
                if len(salle['patients'])==salle['capacite_max']:
                    salle["statut"] = "pleine"
            return f"Salle {nom} attribuée. Capacité restante: {cap_res}"
            
    return "Erreur: Salle inexistante."

def liberer_salle(Salles, nom,patient):
    for salle in Salles:
        if salle["nom"] == nom:
            if patient in salle["patients"]:
                salle["patients"].remove(patient)
                salle["capacite_actuelle"] -= 1
                if salle["statut"] == "pleine":
                    salle["statut"] = "Disponible"
                cap_res=salle['capacite_max']-len(salle['patients'])
                return f"Salle {nom} libérée, capacité restante: {cap_res}"
            else:
                return "Erreur: Patient non présent."
    return "Erreur: Salle inexistante."

def modifier_salle(Salles, nom, nouvelle_categorie=None, nouvelle_capacite_max=None, nouveaux_equipements=None):
    for salle in Salles:
        if salle["nom"] == nom:
            if nouvelle_categorie:
                salle["type"] = nouvelle_categorie
            if nouvelle_capacite_max is not None:
                salle["capacite_max"] = nouvelle_capacite_max
                salle["capacite_actuelle"] = nouvelle_capacite_max - len(salle["patients"])
                salle["statut"] = "pleine" if salle["capacite_actuelle"] == 0 else "disponible"
            if nouveaux_equipements is not None:
                salle["equipements"] = nouveaux_equipements
            return f"Salle {nom} modifiée avec succès!"
    return "Erreur: Salle non trouvée."

def afficher_salles(Salles):
    if not Salles:
        return "Aucune salle n'a été enregistrée."
    for salle in Salles:
        print(f"---> Nom: {salle['nom']}, Type: {salle['type']}, Capacité actuelle: {len(salle['patients'])}, "
              f"Capacité maximale: {salle['capacite_max']}, Statut: {salle['statut']}, "
              f"Patients: {salle['patients']}, Equipements: {', '.join(salle['equipements'])}\n")
    return Salles

def tri_salles(Salles, statut):
    Salles_triees = [salle for salle in Salles if salle["statut"] == statut]
    return Salles_triees if Salles_triees else f"Aucune salle n'est '{statut}'."

def supprimer_salle(Salles, nom):
    for salle in Salles:
        if salle["nom"] == nom:
            Salles.remove(salle)
            return f"Salle {nom} supprimée avec succès."
    return "Erreur: Salle non présente."

print(ajouter_salle(Salles,"Salle1", "Consultation",6,"disponible",["Lit", "Table"]))
print()
afficher_salles(Salles)
print()
print(attribuer_salle(Salles,"Salle1", (1,"Jean Dupont")))  
print(attribuer_salle(Salles,"Salle1", (2,"Marie Curie")))
print(liberer_salle(Salles,"Salle1", (1,"Jean Dupont")))
print(modifier_salle(Salles,"Salle1", nouvelle_capacite_max=3))
afficher_salles(Salles)
