machines = []
equipements = []

def ajouter_machine(machines, id_machine, nom, etat=None):
    for machine in machines:
        if machine["id_machine"] == id_machine:
            return "Erreur : cette machine déjà enregistrée!"
    machine = {
        "id_machine": id_machine,
        "nom": nom,
        "etat": etat
    }
    machines.append(machine)
    return machine

def modifier_etat_machine(machines, id_machine, nouvel_etat):
    for machine in machines:
        if machine["id_machine"] == id_machine:
            machine["etat"] = nouvel_etat
            return "État mis à jour!"
    return "Erreur : machine introuvable"

def supprimer_machine(machines, id_machine):
    for machine in machines:
        if machine["id_machine"] == id_machine:
            machines.remove(machine)
            return "Machine supprimée!"
    return "Erreur : machine non trouvée"

def afficher_machines(machines):
    if len(machines)!=0:
        for machine in machines:
            print(f"---> id_machine: {machine['id_machine']}, Nom: {machine['nom']}, État: {machine['etat']}")
    else:
        return "Aucune machine enregistrée"

def rechercher_machine(machines,critere,valeur):
    machine_present=False
    for machine in machines:
        if machine[critere]==valeur:
            machine_present=True
            m=machine
    if machine_present:
       print(f"---> id_machine: {m['id_machine']}, Nom: {m['nom']}, État: {m['etat']}")
       return m
    else:
        return f"machine non trouvée,essayez d'autres criteres"

def attribuer_machine(equipements,id_machine):
    m=rechercher_machine(machines,"id_machine",id_machine)
    if isinstance(m,dict):
        if m in equipements:
            return f"Machine déjà présente"
        else:
            if m['etat']=='Disponible':
                m['etat']="Occupée"
            elif m['etat']=='Occupée':
                return "Machine occupée"
            else:
                return f"Ajout impossible, la machine '{m['nom']}' identifiée '{m['id_machine']}' est actuellement en maintenance"
            equipements.append(m)
            return f"La machine {m['nom']}' identifiée '{m['id_machine']}' est désormais en service"         
    else:
        return f"Erreur,Veuillez recommencer"

def liberer_machine(equipements,id_machine):
    m=rechercher_machine(machines,'id_machine',id_machine)    
    if m in equipements:
            equipements.remove(m)
            m['etat']="Maintenance"
            return f"Machine liberée et dirigée en maintenance pour analyse éventuelle"
    else:
        return f"Machine non présente ici"

ajouter_machine(machines,"SUOO76","Scalp","Disponible")
afficher_machines(machines)
print()
attribuer_machine(equipements,'SUOO76')
afficher_machines(machines)
print()
attribuer_machine(equipements,'SUOO76')
print()
print(machines)
print(equipements)
liberer_machine(equipements,"SUOO76")
print()
afficher_machines(machines)
print()
print(afficher_machines(equipements))
print(attribuer_machine(equipements,'SUOO76'))
print()
rechercher_machine(machines,"id_machine","SUOO76")