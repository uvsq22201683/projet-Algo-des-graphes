# projet-Algo-des-graphes

L'objectif de ce projet est de construire une réseau, une table de routage de 100 noeuds. 
Pour cela, il est décomposé en 5 tâches : 

- création aléatoire d'un réseau réaliste

- vérification de la connexité du réseau : 
    Pour vérifier qu'il existe bien un chemin entre n'importe quelle paire de sommets, j'ai utilisé la méthode de parcours en profondeur (DFS). Pour initialiser, cela fonctionne en créant un tableau "visisted", ou chaque noeud marqué comme non-visité retourne False. On choisit un sommet(0) arbitraire et on l'ajoute dans une pile "stack". Ensuite, tant que la pile n'est pas vide, le sommet en haut de la pile est examiné :
        - si il n'etait pas visité, il est marqué
        - sinon, on ajoute tous ses sommets à la pile 
    Après que la pile soit vide, si tous les sommets marqués sont notés "visited", le graphe est connexe et donc retourne True. Si un ou plusieurs sommets restent non visités alors la fonction renvoie False. 

- détermination de la table de routage de chaque noeud

- reconstitution du chemin de 2 noeuds / une interface graphique
