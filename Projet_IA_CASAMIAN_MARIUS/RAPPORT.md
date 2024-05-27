Projet Resolution de problèmes à base de graphes d'états
Cours: Concepts d'IA

Avoir graphviz d'installer sur le pc

Nom: Casamian
Prénom: Marius



Remarque importante: Tous les fichiers python ont été transformés en .txt pour éviter d'être rejetés par les maileurs. Il faut donc modifier l'extension en .py au lieu de .txt pour qu'ils puissent s'éxécuter.

Rapport:
Pour les deux premières parties du projet:
Au début je me suis occupé de remplir le fichier LoupChevreSaladeEtudiant.xml afin d'obtenir toutes les transitions possibles ainsi que les variables génériques. Puis j'ai fait de même pour le fichier des sceaux de DieHard.xml.
Le programme python program.py extrait les transitions puis génère un fichier dot depuis ces transitions et vice versa, et enfin grâce à graphviz (librairie python) je visualise un graphique (state_diagram.png) depuis le fichier dot.
Afin d'y parvenir voici comment éxécuter ce programmme:

Le fichier program.py s'éxécute en premier de la manière suivante:
> python3 program.py 'LoupChevreSaladeEtudiant.xml'
                ou
> python3 program.py 'DieHard.xml'

Pour la troisième partie du projet:
J'ai rencontré beaucoup plus de difficultés notamment avec le solver dans un premier temps puis une fois les solutions extraites à faire le lien avec mes transitions dans le fichier .dot précédement obtenu. Il me manque donc à mettre en gras les transitions et les noeuds dont le chemin est celui de la solution extraite.
Je visualise très bien le problème mais j'ai eu du mal pour l'implémenter donc plûtot que de rendre un code faux j'ai préféré juste extraire les bonnes solutions du solver.

Le fichier program3.py s'éxécute de la sorte:

> python3 program3.py /home/m1000/Bureau/talosExamples-0.4.1-SNAPSHOT-jar-with-dependencies.jar /home/m1000/Bureau/Projet_IA/LoupChevreSaladeEtudiant.xml 1

                    ou
> python3 program3.py /home/m1000/Bureau/talosExamples-0.4.1-SNAPSHOT-jar-with-dependencies.jar /home/m1000/Bureau/Projet_IA/DieHard.xml 2

Cette fois ci il faut veiller à respecter les 3 arguments du programme et bien renseigner les chemins de l'éxécutable dans un premier temps puis du fichier xml souhaité et enfin du code, à savoir, 1 pour le problème LoupChevreSaladeEtudiant.xml et 2 pour DieHard.xml.
Si ces trois arguments sont bien respectés alors le programme devrait générer une solution pour chaque problème.
Une solution qui est juste car par exemple pour le problème des sceaux on obtient:

[[[0, 0, 0, 5, 3, 2, 0, 2, 2, 0, 2, 5, 3, 4]]]

qui correspond à (0,0) -> (0,5) -> (3,2) -> (0,2) -> (2,0) -> (2,5) -> (3,4) le chemin le plus court.

J'ai donc finis les trois étapes du projet et essayer de résoudre le problème des wagons mais en vain car j'ai trouvé trop de transitions.

Merci beaucoup pour ce projet qui m'as appris beaucoup de choses, pour toutes questions ou retours n'hésitez pas.
Cordialement, Marius Casamian

FIN


