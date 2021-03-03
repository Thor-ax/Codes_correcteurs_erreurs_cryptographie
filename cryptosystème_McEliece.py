import numpy as np
from numpy.linalg import solve, inv
            
import random 


"""

Retourne la matrice génératrice du code linéaire C

n: nombre de lignes
k: nombre de colones
d_min = distance minimale du code => doit vérifier d_min <= n - k + 1

"""

def Goppa(n, k, d_min):
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
        return(Goppa(n, k, d_min))

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

"""

Retourne la matrice de Permutation P

"""
def perm(nb_col):
  M = [i for i in range(nb_col)]  #Indices à changer en 1
  random.shuffle(M) #Melange le tableau M

  P = [[0]*nb_col for i in range(nb_col)] #Matrice nulle
  for i in range(nb_col):
    for j in range(len(M)):
      n = M[j]
    P[i][n] = 1
    M.pop()

  return(P)

"""

Retourne une matrice aléatoire (0 et 1) inversible

"""
def matriceAleatoireInversible(nb_lig):
  inverse = [[0]*nb_lig for i in range(nb_lig)] 
  Q = [[0]*nb_lig for i in range(nb_lig)] 
  M = [[0]*nb_lig for i in range(nb_lig)] 
  
  while (np.array(inverse) == np.array(M)).all():
    Q = aleatoire(nb_lig, nb_lig)
    try:
        #essaie d'inverser la matrice
        inverse = inv(np.array(Q))   
    except:
        # si inversion impossible, on remet les coef à 01 pour rester dans la boucle while
        inverse = [[0]*nb_lig for i in range(nb_lig)] 
    
  return Q

"""

créer une matrice aléatoire (0 et 1) de taille n * m

"""
def aleatoire(n, m):
    #initialise la matrice à 0
    M = [[0]*m for i in range(n)] 
    for i in range(n):
        for j in range(m):
            M[i][j] = random.randint(0,1)
    return M


"""

Retourne la clef publique G_pub

Q: Matrice aléatoire inversible
P: Matrice de permutation
G: Matrice génératrice

"""
def ClefPublique(Q, G, P):
    prod = np.dot(Q, G)
    return( np.dot(prod, P)%2)


"""***** Chiffrement *****"""

"""

Retourne le message chiffré c
m: message à envoyer
G_pub: clef publique 

"""

def c(m, G_pub):
    return(np.dot(m, G_pub)%2)

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



#print(erreur([0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1], 3 ))

#G_pub = np.array([[0,1,0,0,1,1,1,1,1,0,0,1,0,1,0], [1,1,1,0,0,1,1,0,1,1,0,0,1,1,0], [1,0,0,1,1,1,0,1,0,0,1,1,0,0,1]])
#m = np.array([1,1,1])
#print(c(m, G_pub))



"""***** Déchiffrement *****"""

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
        print("i = " + str(i))
        print("H = " + str((H[:, [i]])))
        
        if((H[:, [i]] == s).all()):
            l.append(i)
    return(l)
            


"""***** Decodage *****"""

def decodage(l, c_prime, G):
    res = [0 for i in range(len(l))]
    for k in range(len(l)):
        index = l[k]
        c_1 = np.copy(c_prime)
        y = (c_1[index] + 1)%2
        c_1[index] = y
        res[k] = c_1
    # arrivé ici res contient la ou les possibilité pour c
    # il faut résoudre le systeme c = xG où x sera le mot de code
    liste_sol = []
    print(len(l))
    for k in range(len(l)):
        A = np.matrix(G)
        B = np.matrix(np.transpose(res[k]))
        solution = (B * A.I)
        
        liste_sol.append(np.array(solution[0]))
   
    return(liste_sol)

"""
Créé un message m aléatoirement et essaie de le décoder à l'aide des
codes linéaires


"""
def test(n, k, d):
    m = [random.randint(0,1) for i in range(k)]
    print("Le message est: " + str(m))
    Q = matriceAleatoireInversible(k)
    P = perm(n)
    x = Goppa(n, k, d)
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
        
    print(H)
    dechif = dechiffrement(H, S)
    print(dechif)
    print()
    print(decodage(dechif, c_prime, G))
    

    


test(4, 2, 1)

