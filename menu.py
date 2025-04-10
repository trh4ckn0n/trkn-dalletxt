from presets import (
    afficher_presets,
    supprimer_preset,
    modifier_preset,
    obtenir_personnalisation,
    generer_logo_dalle
)

def afficher_menu():
    while True:
        choix = input(
            "\n=== MENU PRINCIPAL ===\n"
            "1. Générer un logo\n"
            "2. Visualiser les modèles enregistrés\n"
            "3. Modifier un modèle\n"
            "4. Supprimer un modèle\n"
            "5. Quitter\n"
            "Choix : "
        )

        if choix == "1":
            config = obtenir_personnalisation()
            generer_logo_dalle(config)
        elif choix == "2":
            afficher_presets()
        elif choix == "3":
            modifier_preset()
        elif choix == "4":
            supprimer_preset()
        elif choix == "5":
            print("À bientôt !")
            break
        else:
            print("❌ Choix invalide. Réessaye.")

if __name__ == "__main__":
    afficher_menu()
