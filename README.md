# 🖥️ logo-generator-cli

![logo généré](https://github.com/trh4ckn0n/trkn-dalletxt/blob/main/file-UETRhDsEArgP4nvX2cuFBF.WEBP)

![screenshot](https://l.top4top.io/p_3387zre6b0.jpg)


Générateur de logos automatisés en ligne de commande via DALL·E 3 & Python.


![Python](https://img.shields.io/badge/python-3.10+-blue?style=flat-square)
![DALL·E](https://img.shields.io/badge/DALL·E-3-purple?style=flat-square)
![Style](https://img.shields.io/badge/style-cyberpunk-red?style=flat-square)
![Statut](https://img.shields.io/badge/status-en%20développement-orange?style=flat-square)

---

## 🚀 À propos

`logo-generator-cli` est un outil Python en ligne de commande permettant de générer automatiquement des logos stylés via l’API **DALL·E 3**.  
Il ajoute un **texte personnalisé avec glitch** et vous permet de créer des modèles réutilisables (presets).

---

<details>
<summary><strong>Fonctionnalités principales</strong></summary>

- Génération d’images DALL·E 3 en 1:1
- Ajout de texte stylisé (police, taille, couleur, glitch)
- Interface CLI interactive
- Enregistrement & rechargement de modèles
- Gestion des presets (afficher, modifier, supprimer)
- Copie automatique vers `/var/www/html/` si besoin

</details>

---

## ⚙️ Prérequis

```bash
Python 3.10+
pip install -r requirements.txt
```

**Contenu du fichier `.env` :**

```env
OPENAI_API_KEY=sk-votre-clé-openai
```

---

# Facultatifs :
<details>
<summary><strong>Facultatif (compile, install fonts, generate preset, ...)</strong></summary>

**Fonts:**
```
bash installfont.sh
```

**Add a Preset dans `presets.json` :** 
```
bash add-preset.sh
```

### Compiler (facultatif)

```bash
pyinstaller --onefile menu.py --add-data "presets.json:." --add-data ".env:."
```
</details>

---

## 🧠 Exemple d'utilisation

```bash
python menu.py
```

## Utilisation compilé

```
./dist/menu
```

> Utilisez les flèches pour naviguer dans le menu, choisissez un style, un texte, une couleur... et laissez faire la magie.

---

<details>
<summary><strong>📁 Structure du projet</strong></summary>

```
logo-generator-cli/
│
├── menu.py                 # Menu principal
├── presets.py              # Logique de génération + gestion
├── presets.json            # Modèles sauvegardés (auto)
├── uploads/
│   └── Glitch_Paradise.ttf # Police glitch personnalisée
├── .env                    # Clé API OpenAI
├── README.md               # Ce fichier
```

</details>

---

## ✨ Exemple visuel

![logo généré](https://github.com/trh4ckn0n/trkn-dalletxt/blob/main/trknlog_1%20(2).png)

---

## 🧩 Exemples de presets enregistrés

```json
{
  "cyber_banger": {
    "nom_logo": "BANG3R",
    "texte_overlay": "Hack The Logo",
    "style": "Cyberpunk Hacker",
    "taille_police": 120,
    "glitch": true,
    "couleur_rgb": [255, 0, 0],
    "nombre_logo": 1
  }
}
```

---

## 🛠️ Personnalisation à venir ?

- [ ] Génération batch avec variations
- [ ] Export ZIP automatique
- [ ] Aperçu graphique local
- [ ] Interface web Flask / Gradio

---

## 🤖 Crédit IA

Les images sont générées avec **DALL·E 3** via l’API OpenAI.  
Le design de ce projet a été assisté par [ChatGPT](https://openai.com/chatgpt).

---

## ❤️ Merci

Si ce projet t’a aidé à créer des logos stylés sans te ruiner :  
**[Soutiens le développeur ici](https://buy.stripe.com/eVa6ptg4efka8wgcMM)**
