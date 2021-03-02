# Codes_correcteurs_erreurs_cryptographie

Projet consistant à appliquer les codes correcteurs d'erreur à la cryptographie.

En cryptographie, on va chercher à chiffrer un message avant de l'envoyer afin d'éviter qu'une autre personne que le destinataire ne puisse le lire.

Cependant, le canal utilisé pour envoyer le message peut générer des erreurs (principalement à cause du bruit) et il faut être en mesure de décoder le message malgré les erreurs.

Pour cela, nous avons étudié deux types de code: les codes binaires et les codes linéaires.

Les codes correspondants au code binaire sont dans le fichier code_binaire.py

Pour effectuer un test simple de décodage, lancer tests(n, c, t) où n représente le nombre de répétition de chaque bit (cf explications ci-dessous), c est le message (sous forme de chaine de caractère) à coder puis décoder (avec erreur pour comparer) et t est le poids de l'erreur. On peut par exemple appeler tests(3, "010", 1) pour décoder le message "010" en répétant chaque bit 3 fois puis en ajoutant une erreur avant d'essayer de décoder le message.

Ces codes sont basés sur la redondance (répéter n fois chaque bit). Par exemple, "010" donnera "000111000" en répétant chaque bit 3 fois.

Ainsi, si une erreur est transmise, on pourra la détecter en comparant les bits n par n.

Par exemple, si au lieu de recevoir "000111000", on reçoit "010111000", l'erreur au second bit est détectée en comparant la valeur des 3 premiers bits. Ils doivent être égaux (issus de la redondance).

Toutefois, ces codes sont limités (E((n-1)/2) erreurs détéctées et corrigées. De plus, ils sont lourds et on au taux d'information de 1/n (Taux qu'on cherche à maximiser).


C'est pourquoi nous avons aussi étudié les codes linéaires.

Les codes correspondand au code linéaire sont dans le fichier cryptosystème_McEliece.py

