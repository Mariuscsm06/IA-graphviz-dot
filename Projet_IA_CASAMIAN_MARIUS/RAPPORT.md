# Projet : Résolution de Problèmes à Base de Graphes d'États
## Cours : Concepts d'Intelligence Artificielle

### Prérequis
- **Graphviz** doit être installé sur le PC.

### Auteur
- **Nom** : Casamian
- **Prénom** : Marius

### Remarque Importante
Tous les fichiers Python ont été transformés en .txt pour éviter d'être rejetés par les maileurs. Il faut donc modifier l'extension en .py pour qu'ils puissent s'exécuter.

---

## Rapport

### Partie 1 & 2 : Création et Visualisation des Graphes
1. **Préparation des fichiers XML** :
    - Remplissage du fichier `LoupChevreSaladeEtudiant.xml` avec toutes les transitions possibles et les variables génériques.
    - Remplissage du fichier `DieHard.xml` de la même manière.

2. **Génération des fichiers DOT et visualisation** :
    - Le programme `program.py` extrait les transitions, génère un fichier DOT à partir de ces transitions et inversement.
    - Utilisation de Graphviz (librairie Python) pour visualiser un graphique (state_diagram.png) à partir du fichier DOT.

#### Exécution du programme :

> python3 program.py 'LoupChevreSaladeEtudiant.xml'
ou
> python3 program.py 'DieHard.xml'

Partie 3 : Résolution des Problèmes avec Solver
J'ai rencontré plus de difficultés, notamment avec le solver et l'intégration des solutions extraites avec mes transitions dans le fichier .dot. J'ai visualisé le problème, mais j'ai eu du mal à l'implémenter. J'ai préféré extraire uniquement les solutions correctes du solver plutôt que de rendre un code incorrect.

Exécution du programme program3.py :

> python3 program3.py /home/m1000/Bureau/talosExamples-0.4.1-SNAPSHOT-jar-with-dependencies.jar /home/m1000/Bureau/Projet_IA/LoupChevreSaladeEtudiant.xml 1
ou
> python3 program3.py /home/m1000/Bureau/talosExamples-0.4.1-SNAPSHOT-jar-with-dependencies.jar /home/m1000/Bureau/Projet_IA/DieHard.xml 2

Arguments du programme :
Chemin de l'exécutable : /home/m1000/Bureau/talosExamples-0.4.1-SNAPSHOT-jar-with-dependencies.jar
Chemin du fichier XML : /home/m1000/Bureau/Projet_IA/LoupChevreSaladeEtudiant.xml ou /home/m1000/Bureau/Projet_IA/DieHard.xml
Code du problème : 1 pour LoupChevreSaladeEtudiant.xml, 2 pour DieHard.xml
Exemple de solution générée (problème des sceaux) :
> [[[0, 0, 0, 5, 3, 2, 0, 2, 2, 0, 2, 5, 3, 4]]]

Conclusion
J'ai terminé les trois étapes du projet et tenté de résoudre le problème des wagons, mais en vain car il y avait trop de transitions. Ce projet m'a beaucoup appris et je vous remercie pour cette opportunité. Pour toute question ou retour, n'hésitez pas.

Cordialement,
Marius 
