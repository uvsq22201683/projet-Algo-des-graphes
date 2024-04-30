# projet-Algo-des-graphes

L'objectif de ce projet est de construire une réseau, une table de routage de 100 noeuds. 
Pour cela, il est décomposé en 4 tâches : 

- Création aléatoire d'un réseau réaliste :
Un premier groupe de 10 noeuds appelé backbone a été crée, ces 10 noeuds étant très connectés entre eux. Ce groupe représente le coeur du réseau. Les temps de communication entre tous ces noeuds ont été déterminés entre 5 et 10. Un deuxième groupe de 20 noeuds a été crée. Chacun de ces 20 noeud est connecté à deux ou trois noeuds du backbone et chacun des liens à une valeur comprise entre 10 et 20. Un troisième groupe de 70 noeuds a été crée et ils sont chacun liés à deux noeuds du deuxième groupe.
    
   Pour créer le graphe, ces classes ont été utlisées.

- Vérification de la connexité du réseau : 
    Pour vérifier qu'il existe bien un chemin entre n'importe quelle paire de sommets, une méthode de parcours en profondeur a été utilisée. L'initialisation fonctionne en créant un tableau "visisted", où chaque noeud marqué comme non-visité retourne False. Un sommet(0) a été arbitrairement choisi et ajouté dans une pile "stack". Tant que la pile n'est pas vide, le sommet en haut de la pile est examiné :
        - s'il n'a pas été visité, il est marqué
        - sinon, on ajoute tous ses sommets à la pile 
    Une fois la pile vide, si tous les sommets marqués sont notés "visited", le graphe est connexe et donc retourne True. Si un ou plusieurs sommets restent non visités alors la fonction renvoie False. 

- Détermination de la table de routage de chaque noeud + Reconstitution du chemin de 2 noeuds:
    Afin de déterminer la table de routage, l'algorithme de Floyd warshall a été utilisé. Une matrice des distances a été initialisée avec tous les noeuds du graphe puis la matrice des prececesseurs a été obtenue. Celle-ci contient désormais les données pour extraire les plus courts chemins entre chaque paire de noeuds.
    
- Interface graphique :
     Une interface graphique a été crée, permettant de visualiser notre graphe connexe et permettant à l'utilisateur de saisir deux noeuds et de faire ressortir le plus courts chemin. Pour cela, la matrice des prédécesseurs (matrice des distances) à été utlisisée ainsi que la fontion pour retrouver la table de routage. L'utilisateur a également la possibilité de zoomer sur le graphe, de le bouger, de le recentrer et de faire apparaitre la valeur de chaque lien.
