import numpy as np
from numpy.linalg import solve, inv
import matplotlib.pyplot as plt
            
import random 

"""

converti un str en liste
ex: conv("001") => [0, 0, 1]
"""

def conv(c):
    liste = []
    for i in c:
        liste.append(int(i))
    return(liste)
    
"""
ajoute de la redondance dans le mots de code
répète n fois chaque bits

exemple: redondance(3, [0,1,0]) => [0,0,0,1,1,1,0,0,0]
"""

def redondance(n, l):
    res = []
    for i in range(len(l)):
        for k in range(n):
            res.append(l[i])
    return(res)

"""
Ajoute une erreur de poid t au message

exemple1: erreur([1,1,1,0,0,0,1,1,1], 2) => [1, 1, 0, 0, 0, 1, 1, 1, 1]

exemple2:erreur([1,1,1,0,0,0,1,1,1], 4) => [1, 1, 0, 1, 0, 1, 1, 1, 0]
"""
def erreur(l, t):
    l_1 = l
    E = [i for i in range(len(l))]
    random.shuffle(E)
    for k in range(t):
        p = E[k]
        x = (l_1[p] + 1)%2
        l_1[p] = x
    return(l_1)

"""
Algorithme de décodage

par exemple, si il y a 3 répétition de chaque bit, on va comparer chaque groupe 
de 3 bits (ils doivent être tous égaux, sinon c'est qu'il y a une erreur)

"""
def decodage(n, l_1):
    m = []  #mots de code
    for i in range(0, len(l_1), n):
        l = []
        for j in range(n):
            l.append(l_1[i+j])
        nb_zeros = l.count(0)
        nb_uns = l.count(1)
        if(nb_zeros != n and nb_uns != n):
            if(nb_zeros > nb_uns):
                #changer les uns en 0
                for j in range (n):
                    if(l_1[i + j] == 1):
                            l_1[i + j] = 0
            else:
                #changer les zeros en un
                #changer les uns en 0
                for j in range (n):
                    if(l_1[i + j] == 0):
                            l_1[i + j] = 1
        #reconstruction du message
        m.append(l_1[i])
    return(m)

"""
Pour effectuer un test simple, retourne le message décodé 

n: nombre de répétition de chaque bit
c : mot de code sous forme de chaine de caractères
t: nombre d'erreurs

"""
def tests(n, c, t):
    l = conv(c) 
    
    message = redondance(n, l)  #ajout de redondance au message à envoyer
    
    message_recu = erreur(message, t)   #ajout d'une erreur de poids t

    message_decode = decodage(n, message_recu)
    
    return(message_decode)
    
    
    
"""
effectuer N tests et comparer les résultats du décodage au message de départ
afin de faire des statistique sur le taux de réussite de ce décodage
en fonction du nombre de répétition n et du nombre d'erreurs t'

exemple 1: 
    
dans cet exemple on fait la moyenne sur 1000 décodage
(chaque bit est répété 3 fois) avec 2 erreurs
x = tests_multiples([0,1,1,1], 1000, 3, "0111", 2) 
print(x) => 0.82
            
exemple 2:
    
dans cet exemple on fait la moyenne sur 1000 décodage 
(chaque bit est répété 4 fois) avec 5 erreurs
print(tests_multiples([0,1,1,1], 1000, 4, "0111", 5)) => 0.457
"""
def tests_multiples(m, N, n, c, t):
    s = 0
    for k in range(N):
        decode = tests(n, c, t)
        if(decode == m):
            s += 1
    return(s/N)
        

"""
Pour que les statistiques soient plus visuels, tracer les courbes pour différentes valeurs
de n (nombre de répétition de chaque bit) et de t (à n fixé on augmentent le nombre d'erreur)
"""

def trace_tests(m, N, c):
    
    for n in range(3, 10):
        p = n * len(m)
        X = np.arange(1, p, 1)
        Y = []
        for i in range(1, p):
            Y.append(tests_multiples(m, N, n, c, i))
        plt.plot(X, Y)
    plt.show()
    

trace_tests([0,1,1,1], 1000, "0111") 
        
