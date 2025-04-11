from presets import (
    afficher_presets,
    supprimer_preset,
    modifier_preset,
    obtenir_personnalisation,
    generer_logo_dalle
)
from rich.console import Console
from rich.text import Text

# Initialisation de la console rich
console = Console()

def afficher_menu():
    # Affichage du titre avec Rich
    console.print("[bold green]TRHACKNON[/bold green] [bold yellow]DALL-E 3 Logo Generator[/bold yellow]\n", style="bold cyan")
    
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
            console.print("[bold red]À bientôt ![/bold red]", style="bold yellow")
            break
        else:
            console.print("[bold red]❌ Choix invalide. Réessaye.[/bold red]", style="bold white")

if __name__ == "__main__":
    afficher_menu()
