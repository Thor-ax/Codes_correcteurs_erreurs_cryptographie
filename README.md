# Codes_correcteurs_erreurs_cryptographie

Projet consistant à appliquer les codes correcteurs d'erreur à la cryptographie.

En cryptographie, on va chercher à chiffrer un message avant de l'envoyer afin d'éviter qu'une autre personne que le destinataire ne puisse le lire.

Cependant, le canal utilisé pour envoyer le message peut générer des erreurs (principalement à cause du bruit) et il faut être en mesure de décoder le message malgré les erreurs.

Pour cela, nous avons étudié deux types de code: les codes binaires et les codes linéaires.

Les codes correspondants au code binaire sont dans le fichier code_binaire.py

Pour effectuer un test simple de décodage, lancer tests(n, c, t) où n représente le nombre de répétition de chaque bit (cf explications ci-dessous), c est le message (sous forme de chaine de caractère) à coder puis décoder (avec erreur pour comparer) et t est le poids de l'erreur. On peut par exemple appeler tests(3, "010", 1) pour décoder le message "010" en répétant chaque bit 3 fois puis en ajoutant une erreur avant d'essayer de décoder le message.

Ces codes sont basés sur la redondance (répéter n fois chaque bit = codes en bloc). Par exemple, "010" donnera "000111000" en répétant chaque bit 3 fois. Ils sont appelés code à répétitions.

Ainsi, si une erreur est transmise, on pourra la détecter en comparant les bits n par n.

Par exemple, si au lieu de recevoir "000111000", on reçoit "010111000", l'erreur au second bit est détectée en comparant la valeur des 3 premiers bits. Ils doivent être égaux (issus de la redondance).

Toutefois, ces codes sont limités (E((n-1)/2) erreurs détéctées et corrigées. De plus, ils sont lourds et on un taux d'information de 1/n (Taux qu'on cherche à maximiser).


C'est pourquoi nous avons aussi étudié les codes linéaires.

Les codes correspondand au code linéaire sont dans le fichier codes_linéaires.py

Pour effectuer un test de décodage, appeler test(n, k, d) ou n représente la taille du message une fois codé, k la taille du message d'origine et d la distance minimale du code C. 

Ces codes sont des codes systématiques. La première étape consiste à construire la matrice génératrice du code linéaire C : G = (Ik \ B) où Ik est la matrice identité de taille k et B une matrice aléatoire composée de 0 et de 1 (fonction Generatrice_controle(n, k, d_min)). Puis, on chiffre le message m: c = m.G (c représente le message chiffré). On introduit une erreur e de poids t (= 1 ici, le code pour une erreur de poids t > 1 n'est pas encore fonctionnel) avec l'algo erreur(c, t) qui retourne c_prime, le message chiffré avec une erreur. Pour décoder ce message, il faut construire la matrice H = (-B^T \ In-k) (appelée matrice de contrôle) où -B^t est l'opposé de la transposé de la matrice B (celle définie pour G) et In-k est la matrice identité de taille n-k. L'étape suivante consiste à localiser l'erreur. Pour cela, on calcule le syndrome S : S = H.(c_prime)^T. On recherche les colonnes de H égales au vecteur syndrome S. Ces colonnes représentes les positions possible de l'erreur. On décode toutes ces possibilités pour obtenir une liste de messages possibles pour m. Plus n est grand et plus le nombre de possibilités sera faible, donc le décodage en sera plus précis.



TODO: Améliorer les algo pour détecter plus d'une erreur (Goppa).

