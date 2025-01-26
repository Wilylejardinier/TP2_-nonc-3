import os

chemin = "."  # Répertoire de départ (ici, le répertoire courant)

# Parcours récursif du répertoire
for racine, dossiers, fichiers in os.walk(chemin):
    print("Répertoire courant :", racine)
    
    # Affichage des sous-répertoires
    for nom_dossier in dossiers:
        print("  Sous-répertoire :", nom_dossier)
    
    # Affichage des fichiers
    for nom_fichier in fichiers:
        print("  Fichier :", nom_fichier)
    
    print("-" * 40)  # Séparateur visuel
