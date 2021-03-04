# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:16:10 2021

@author: Maxime
"""

"""***** Codes Linéaires *****"""
 
 
import numpy as np
from numpy.linalg import solve, inv, eigvals
            
import random 


"""

Retourne la matrice génératrice G du code linéaire C et la matrice de contrôle H

n: nombre de lignes
k: nombre de colones
d_min = distance minimale du code => doit vérifier d_min <= n - k + 1

"""

def Generatrice_controle(n, k, d_min):
    I_k = np.identity(k)    #matrice identité de taille k
    B = []
    for i in range(k):
        M = [random.randint(0,1) for j in range(n-k)]   #liste aléatoire de 0 et de 1 
        B.append(M)
    G = np.concatenate((I_k, B), axis=1)
    if(distance_min(B, d_min)):
        B_t = -(np.transpose(B))%2
        B_t_2 = []
        for x in B_t:
            B_t_2.append(x)
        H = np.concatenate((B_t_2, np.identity(n-k)), axis=1)
        return(G, H)
    else:
        #s'assurer que la condition de distance minimale soit vérifiée
        return(Generatrice_controle(n, k, d_min))

"""

Calcule la distance de Hamming entre 2 lignes consécutives de G

"""
def distance_min(G, d_min):
    nb_lig = len(G)
    nb_col = len(G[0])
    for k in range(nb_lig - 1):
        
        list_diff = [(b_elt - a_elt)%2 for a_elt, b_elt in zip(G[k], G[k+1])]
        d = 0   #distance du code
        for b in list_diff:
            d = d + b
        
        if(d > d_min):
            return False
    return True

"""***** Chiffrement *****"""

"""

Retourne le message chiffré c
m: message à envoyer
G_pub: clef publique 

"""

def c(m, G):
    return(np.dot(m, G)%2)

"""

Ajoute une erreur de poids t au message c

"""

def erreur(c, t):
    n = len(c)
    c_2=[0 for i in range(n)]
    E = [0 for i in range(n)]
    N = [i for i in range(0, n)]
    random.shuffle(N)
    for k in range(t):
        index = N[k]
        E[index] = 1
    for i in range (n):
        c_2[i] = (E[i] + c[i])%2
    print("e = " + str(E))
    return(c_2)

"""***** Déchiffrement *****"""

"""

On recherche la position du vecteur syndrome dans la matrice H.
Cette position correspond à la position de l'erreur dans le message reçu.
Retourne la liste des messages possibles (le vecteur syndrome peut être présent dans plusieurs colonnes de H)

"""
def dechiffrement(H, S):
   
    l = []
    p = len(S)
    s = []
    l_1 = []
    for x in S:
        l_1.append(x)
        s.append(l_1)
        l_1 = []
    for i in range(0, len(H[0])):
        
        if((H[:, [i]] == s).all()):
            
            l.append(i)
            
    return(l)
            


"""***** Décodage *****"""

"""

Après avoir localisé la ou les positions possible de l'erreur, il nous reste à 
décoder pour avoir le ou les messages possible(s). Pour cela, on calcule c à partir de c_prime
et de la liste des possibilités pour la position de la ou des erreurs.

ensuite, on résoud le système c = mG pour obtenir m.

"""

def decodage(l, c_prime, G):
    taille_mssg = len(G)
    res = [0 for i in range(len(l))]
    for k in range(len(l)):
        index = l[k]
        c_1 = np.copy(c_prime)
        y = (c_1[index] + 1)%2
        c_1[index] = y
        res[k] = c_1
    # arrivé ici res contient la ou les possibilité(s) pour c
    # il faut résoudre le systeme c = xG où x sera le mot de code
    liste_sol = []
    for k in range(len(l)):
        sol = []
        for j in range(taille_mssg):
            sol.append(res[k][j])

            
        liste_sol.append(sol)
   
    return(liste_sol)

"""
Créé un message m aléatoirement et essaie de le décoder à l'aide des
codes linéaires


"""
def test(n, k, d):
    m = [random.randint(0,1) for i in range(k)]
    print("Le message est: " + str(m))
    
    x = Generatrice_controle(n, k, d)
    G = x[0]
    print("G = " + str(G))
    H = x[1]
    c = np.dot(m, G)%2
    print("c = " + str(c))
    print()
    c_prime = erreur(c, 1)
    print("c' = " + str(c_prime))
    print()
    
    
    S = np.dot(H, np.transpose(c_prime))%2
    print("Syndrome = " + str(S))
    print()
        
    print("H =" + str(H))
    print()
    dechif = dechiffrement(H, S)
    print(dechif)
    print()
    print(decodage(dechif, c_prime, G))
    print()
    print("Taux d'indormation =" + str(k/n))
    

test(4, 2, 1)
