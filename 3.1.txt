# 3.1 - Lire le contenu d'un fichier dans un buffer

nom_fichier = "mon_fichier.txt"  # Nom du fichier à lire

# Ouverture du fichier en lecture
f = open(nom_fichier, "r", encoding="utf-8")

# Lecture du contenu du fichier
buffer = f.read()

# Fermeture du fichier
f.close()

# Affichage du contenu
print("Contenu du fichier :")
print(buffer)
