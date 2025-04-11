#!/bin/bash

# Fichier de presets
PRESETS_FILE="presets.json"

# Fonction pour ajouter un nouveau preset
ajouter_preset() {
  # Demander à l'utilisateur les informations du nouveau preset avec des valeurs par défaut
  read -p "Nom du logo (par défaut 'TRHACKNON') : " nom_logo
  nom_logo=${nom_logo:-"TRHACKNON"}

  read -p "Nombre de logos (par défaut 1) : " nombre_logo
  nombre_logo=${nombre_logo:-1}

  read -p "Couleur (rouge, vert, bleu, par défaut vert) : " couleur
  couleur=${couleur:-"vert"}

  read -p "Texte à afficher (par défaut 'Hack the System') : " texte_overlay
  texte_overlay=${texte_overlay:-"Hack the System"}

  read -p "Style (Cyberpunk Hacker, Futurisme Technologique, Dark Fantasy Hacker, par défaut 'Cyberpunk Hacker') : " style
  style=${style:-"Cyberpunk Hacker"}

  read -p "Effet glitch (true/false, par défaut true) : " glitch
  glitch=${glitch:-"true"}

  read -p "Taille de la police (par défaut 220) : " taille_police
  taille_police=${taille_police:-220}

  # Définir la couleur RGB selon le choix
  case $couleur in
    "rouge")
      couleur_rgb="[255, 0, 0]"
      ;;
    "vert")
      couleur_rgb="[0, 255, 0]"
      ;;
    "bleu")
      couleur_rgb="[0, 0, 255]"
      ;;
    *)
      echo "❌ Couleur invalide, la couleur verte sera utilisée par défaut."
      couleur_rgb="[0, 255, 0]"
      ;;
  esac

  # Créer un nouvel objet preset avec les informations
  nouveau_preset=$(cat <<EOF
{
  "$nom_logo": {
    "nom_logo": "$nom_logo",
    "nombre_logo": $nombre_logo,
    "couleur_rgb": $couleur_rgb,
    "texte_overlay": "$texte_overlay",
    "style": "$style",
    "glitch": $glitch,
    "taille_police": $taille_police
  }
}
EOF
)

  # Vérifier si le fichier presets.json existe déjà
  if [[ ! -f "$PRESETS_FILE" ]]; then
    # Si le fichier n'existe pas, créer un fichier JSON vide et ajouter le preset
    echo "{ $nouveau_preset }" > "$PRESETS_FILE"
    echo "✅ Nouveau preset ajouté au fichier $PRESETS_FILE."
  else
    # Si le fichier existe, ajouter le preset à la fin du fichier
    jq ". + $nouveau_preset" "$PRESETS_FILE" > tmp.json && mv tmp.json "$PRESETS_FILE"
    echo "✅ Nouveau preset ajouté au fichier $PRESETS_FILE."
  fi
}

# Appeler la fonction pour ajouter un nouveau preset
ajouter_preset
