import shutil
import openai
import os
import json
from dotenv import load_dotenv
from pathlib import Path
import requests
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont
from io import BytesIO
import questionary

# === CONFIG ===
PRESETS_FILE = "presets.json"
FONT_PATH = "uploads/Glitch_Paradise.ttf"

# Couleurs disponibles
COULEURS_RGB = {
    "Rouge": (255, 0, 0),
    "Vert": (0, 255, 0),
    "Bleu": (0, 0, 255),
    "Violet": (148, 0, 211)
}

# Styles visuels
STYLES_VISUELS = {
    "Cyberpunk Hacker": """
High-resolution squared poster (1:1), hacker style in a rainy dark alley lit by red neon.
Show a symbolic rebellion: hidden graffiti '{nom_dev}', glowing Guy Fawkes mask, clenched fist shattering chains,
rich man symbols, cables sliced by a knife, graffiti eye with signal waves. 
Environment: glitch effects, dripping neon paint, QR codes, wires. 
Anonymous, anticapitalist theme. Style: cinematic, dark, underground, Blade Runner-inspired.
""",
    "Futurisme Technologique": """
Minimal futuristic branding poster (1:1), sleek white background with sharp shadows.
Abstract tech symbol for '{nom_dev}' in the center, glowing circuits, geometric particles.
Soft light rays, digital aura, subtle blue glow. Style: Apple meets Tron.
""",
    "Dark Fantasy Hacker": """
Dark fantasy poster (1:1), cryptic magical hacker sigils glowing on an ancient stone wall.
'{nom_dev}' appears as an ethereal rune among mystic graffiti. Neon green magic code particles in the air.
Environment: fog, cracked cyber runes, enchanted tech, torches. Style: dark mystic fantasy, underground.
"""
}

# === INIT ===
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ Clé API manquante.")
    exit()
openai.api_key = api_key

# === PRESETS ===
def sauvegarder_preset(nom, preset):
    data = charger_presets()
    data[nom] = preset
    with open(PRESETS_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print(f"✅ Modèle '{nom}' sauvegardé.")

def charger_presets():
    if not Path(PRESETS_FILE).exists():
        return {}
    with open(PRESETS_FILE, "r") as f:
        return json.load(f)

def afficher_presets():
    presets = charger_presets()
    if not presets:
        print("Aucun modèle enregistré.")
        return
    print("\n=== Modèles enregistrés ===")
    for nom, config in presets.items():
        print(f"- {nom} : {config['style']} | Texte : '{config['texte_overlay']}' | Glitch : {config['glitch']} | Taille : {config['taille_police']}")

def supprimer_preset():
    presets = charger_presets()
    if not presets:
        print("Aucun modèle à supprimer.")
        return
    nom = questionary.select("Quel modèle supprimer ?", choices=list(presets.keys())).ask()
    if questionary.confirm(f"Supprimer le modèle '{nom}' ?").ask():
        del presets[nom]
        with open(PRESETS_FILE, "w") as f:
            json.dump(presets, f, indent=4)
        print(f"✅ Supprimé.")

def modifier_preset():
    presets = charger_presets()
    if not presets:
        print("Aucun modèle à modifier.")
        return
    nom = questionary.select("Quel modèle modifier ?", choices=list(presets.keys())).ask()
    ancien = presets[nom]
    nouveau_nom_logo = questionary.text("Nom de logo ?", default=ancien["nom_logo"]).ask()
    nouveau_texte = questionary.text("Texte à afficher ?", default=ancien["texte_overlay"]).ask()
    nouveau_style = questionary.select("Style ?", choices=list(STYLES_VISUELS.keys()), default=ancien["style"]).ask()
    nouvelle_taille = questionary.text("Taille police ?", default=str(ancien["taille_police"])).ask()
    nouvelle_couleur = questionary.select("Couleur ?", choices=list(COULEURS_RGB.keys())).ask()
    nouveau_glitch = questionary.confirm("Effet glitch ?", default=ancien["glitch"]).ask()

    presets[nom] = {
        "nom_logo": nouveau_nom_logo,
        "texte_overlay": nouveau_texte,
        "style": nouveau_style,
        "taille_police": int(nouvelle_taille),
        "couleur_rgb": COULEURS_RGB[nouvelle_couleur],
        "glitch": nouveau_glitch,
        "nombre_logo": ancien.get("nombre_logo", 1)
    }

    with open(PRESETS_FILE, "w") as f:
        json.dump(presets, f, indent=4)
    print(f"✅ Modifié.")

def choisir_ou_creer_preset():
    if questionary.confirm("Utiliser un modèle existant ?").ask():
        presets = charger_presets()
        if not presets:
            print("❌ Aucun modèle.")
            return None
        choix = questionary.select("Choisir un modèle :", choices=list(presets.keys())).ask()
        return presets[choix]
    return None

def obtenir_personnalisation():
    preset = choisir_ou_creer_preset()
    if preset:
        return preset

    nom_logo = questionary.text("Nom du logo ?").ask()
    nombre_logo = int(questionary.text("Combien de logos ? (1-10)", default="1").ask())
    couleur = questionary.select("Couleur texte :", choices=list(COULEURS_RGB.keys())).ask()
    texte = questionary.text("Texte à afficher ?", default="Benga !").ask()
    style = questionary.select("Style visuel :", choices=list(STYLES_VISUELS.keys())).ask()
    glitch = questionary.confirm("Effet glitch ?").ask()
    taille_police = int(questionary.text("Taille police ?", default="120").ask())

    if questionary.confirm("Sauvegarder ce modèle ?").ask():
        nom_preset = questionary.text("Nom du modèle ?").ask()
        preset_data = {
            "nom_logo": nom_logo,
            "nombre_logo": nombre_logo,
            "couleur_rgb": COULEURS_RGB[couleur],
            "texte_overlay": texte,
            "style": style,
            "glitch": glitch,
            "taille_police": taille_police
        }
        sauvegarder_preset(nom_preset, preset_data)

    return {
        "nom_logo": nom_logo,
        "nombre_logo": nombre_logo,
        "couleur_rgb": COULEURS_RGB[couleur],
        "texte_overlay": texte,
        "style": style,
        "glitch": glitch,
        "taille_police": taille_police
    }

# === GÉNÉRATION ===
def generer_logo_dalle(preset):
    prompt = STYLES_VISUELS[preset["style"]].replace("{nom_dev}", preset["nom_logo"])
    for i in range(preset["nombre_logo"]):
        try:
            response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
            image_url = response["data"][0]["url"]
            image = Image.open(BytesIO(requests.get(image_url).content))

            if preset["glitch"]:
                image = appliquer_effets(image, preset["couleur_rgb"], preset["texte_overlay"], preset["taille_police"])
            else:
                image = ajouter_texte(image, preset["couleur_rgb"], preset["texte_overlay"], preset["taille_police"])

            filename = f"trknlogotxt_{i+1}.png"
            image.save(filename)
            shutil.copy(filename, f"/var/www/html/trknlog_{i+1}.png")
            print(f"✅ Logo généré : {filename}")
        except Exception as e:
            print(f"❌ Erreur : {e}")

def appliquer_effets(image, couleur, texte, taille):
    image = ImageEnhance.Contrast(image).enhance(1.8)
    image = ajouter_texte(image, couleur, texte, taille)
    image = image.filter(ImageFilter.GaussianBlur(0.5))  # Améliorer le flou pour un meilleur effet glitch
    return image

def ajouter_texte(image, couleur, texte, taille_police):
    image = image.convert("RGB")
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype(FONT_PATH, taille_police)
    except IOError:
        print("⚠️ Police manquante, police par défaut utilisée.")
        font = ImageFont.load_default()

    # Assurez-vous que la couleur est un tuple, même si c'est une liste
    if isinstance(couleur, list):
        couleur = tuple(couleur)

    bbox = draw.textbbox((0, 0), texte, font=font)
    position = ((image.width - (bbox[2] - bbox[0])) // 2, int(image.height - (bbox[3] - bbox[1]) * 1.1))

    # Appliquer un effet de "glitch" en décalant le texte
    for offset in range(-6, 7, 2):
        draw.text((position[0] + offset, position[1] + offset), texte, font=font, fill=(255, 255, 255))
    draw.text(position, texte, font=font, fill=couleur)
    return image
