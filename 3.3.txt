import os

ancien_nom = "mon_fichier.txt"
nouveau_nom = "mon_fichier2.txt"

# Renommer le fichier
os.rename(ancien_nom, nouveau_nom)

print(f"Le fichier {ancien_nom} a été renommé en {nouveau_nom}.")
