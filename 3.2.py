nom_fichier = "mon_fichier.txt"

# Ouverture du fichier
with open(nom_fichier, "r", encoding="utf-8") as f:
    # Lecture de tout le contenu puis découpage en mots
    contenu = f.read()
    mots = contenu.split()

# Affichage de la liste de mots
print("Voici la liste des mots trouvés :")
print(mots)

# Affichage un mot par ligne (optionnel)
for mot in mots:
    print(mot)
