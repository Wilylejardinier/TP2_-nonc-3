import os

repertoire = "."         # Ici, "." correspond au répertoire courant
extension_recherche = ".txt"  # Extension à rechercher

# Liste tous les fichiers dans le répertoire
fichiers = os.listdir(repertoire)

print(f"Fichiers se terminant par {extension_recherche} dans {repertoire} :")
for fichier in fichiers:
    if fichier.endswith(extension_recherche):
        print(fichier)
