import xml.etree.ElementTree as ET
import graphviz
import sys
import re

def extraire_transitions(fichier_xml):
    # Charger et analyser le fichier XML
    arbre = ET.parse(fichier_xml)
    racine = arbre.getroot()

    # Liste pour stocker les transitions
    transitions = []

    matrice_valeurs = racine.find('.//valmatrix')
    for element_donnees in matrice_valeurs.findall('data'):
        texte_donnees = element_donnees.text
        valeurs = [int(valeur) for valeur in texte_donnees.split()]
        milieu = len(valeurs) // 2
        etat_source = tuple(valeurs[:milieu])
        etat_destination = tuple(valeurs[milieu:])
        transitions.append((etat_source, etat_destination))

    return transitions

def transitions_vers_dot(transitions):
    dot_sortie = 'digraph G {\n'
    for (src, dest) in transitions:
        dot_sortie += f'    "{src}" -> "{dest}";\n'
    dot_sortie += '}'
    with open('graph.dot', 'w') as fic:
        fic.writelines(dot_sortie)

    print("Le fichier dot à été créer avec succès !")
    return dot_sortie

def dot_to_transitions(dot_input):
    transitions = []
    lignes = dot_input.splitlines()
    for ligne in lignes:
        if '->' in ligne:
            parts = ligne.split('->')
            src = parts[0].strip().strip('"')
            dest = parts[1].strip().strip('";')
            # pour extraire les nombres
            src_nums = re.findall(r'\d+', src)
            dest_nums = re.findall(r'\d+', dest)
            # en tuples d'entiers
            src_tuple = tuple(map(int, src_nums))
            dest_tuple = tuple(map(int, dest_nums))
            
            transitions.append((src_tuple, dest_tuple))
    return transitions


def generate_png_from_dot(dot_input, fic_sortie):
    graph = graphviz.Source(dot_input)
    graph.format = 'png'
    graph.render(filename=fic_sortie, cleanup=True)

# Se placer dans le repertoire où se trouvent les fichiers xml et les programmes py 
# Exemple d'utilisation : > python3 program.py 'LoupChevreSaladeEtudiant.xml' ou python3 program.py 'DieHard.xml'
# Génère le fichier .dot avec les transitions; et affiche les transitions depuis le dot
# projet jusqu'à partie 2 terminé

def main():
    xml = sys.argv[1]
    transitions = extraire_transitions(xml)
    dotOutput = transitions_vers_dot(transitions)
    dotTransitions = dot_to_transitions(dotOutput)
    print(dotOutput)
    print(dotTransitions)
    generate_png_from_dot(dotOutput, 'state_diagram')

if __name__ == "__main__":
    main()