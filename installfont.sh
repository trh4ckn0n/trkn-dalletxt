#!/bin/bash

# Chemin du fichier zip
ZIP_FILE="uploads.zip"

# Dossier de destination pour extraire les fichiers
DEST_DIR="uploads"

# Vérifier si le fichier zip existe
if [[ ! -f "$ZIP_FILE" ]]; then
  echo "❌ Le fichier $ZIP_FILE n'existe pas."
  exit 1
fi

# Décompresser le fichier zip
echo "Décompression du fichier $ZIP_FILE..."
unzip -o "$ZIP_FILE" -d "$DEST_DIR"

# Vérifier si l'extraction a réussi
if [[ $? -eq 0 ]]; then
  echo "✅ Fichier décompressé avec succès dans le dossier $DEST_DIR."
else
  echo "❌ Erreur lors de la décompression."
  exit 1
fi
