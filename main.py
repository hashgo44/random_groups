import click
import random

@click.command()
@click.option('--input-file', '-f', default='names.txt',help='Fichier texte contenant les noms')
@click.option('--num-groups', '-n', type=int, default=3, help='Nombre de groupes à créer (par défaut: 3)')
@click.option('--output-file', '-o', default='groups.txt', help='Fichier de sortie pour les groupes (par défaut: groupes.txt)')
def generate_groups(input_file, num_groups, output_file):
    """Génère un nombre spécifique de groupes aléatoires à partir d'un fichier texte."""
    try:
        with open(input_file, 'r') as f:
            names = [line.strip() for line in f if line.strip()]
        
        random.shuffle(names)
        
        base_size = len(names) // num_groups
        extra = len(names) % num_groups
        
        groups = []
        start = 0
        for i in range(num_groups):
            end = start + base_size + (1 if i < extra else 0)
            groups.append(names[start:end])
            start = end
        
        print(f"Nombre total de noms: {len(names)}")
        print(f"Nombre de groupes créés: {len(groups)}")
        for i, group in enumerate(groups, 1):
            print(f"Groupe {i}: {group}")
        
        with open(output_file, 'w') as f:
            for i, group in enumerate(groups, 1):
                group_str = ", ".join(group)
                f.write(f"Groupe {i}: {group_str}\n")
        
        click.echo(f"Groupes générés et sauvegardés dans {output_file}")
    
    except FileNotFoundError:
        click.echo(f"Erreur: Le fichier {input_file} n'a pas été trouvé.")
    except IOError:
        click.echo(f"Erreur: Problème lors de la lecture ou de l'écriture des fichiers.")
    except ValueError as e:
        click.echo(f"Erreur: {str(e)}")

if __name__ == '__main__':
    generate_groups()