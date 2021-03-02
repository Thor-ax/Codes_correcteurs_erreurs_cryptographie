import numpy as np
from numpy.linalg import solve, inv
            
import random 


"""
Retourne la matrice génératrice du code linéaire C

n: nombre de lignes
k: nombre de colones
d = distance minimale du code

"""

def Goppa(n, k, d_min):
    I_k = np.identity(k)    #matrice identité de taille k
    P = []
    for i in range(k):
        M = [random.randint(0,1) for j in range(n-k)]   #liste aléatoire de 0 et de 1 
        P.append(M)
    G = np.concatenate((I_k, P), axis=1)
    if(distance_min(G, d_min)):
        return(G)
    else:
        #s'assurer que la condition de distance minimale soit vérifiée
        return(Goppa(n, k, d_min))


def distance_min(G, d_min):
    nb_lig = len(G)
    nb_col = len(G[0])
    for k in range(nb_lig - 1):
        
        list_diff = [(b_elt - a_elt)%2 for a_elt, b_elt in zip(G[k], G[k+1])]
        d = 0   #distance du code
        for b in list_diff:
            d = d + b
        print(d)
        if(d > d_min):
            return False
    return True


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


def matriceAleatoireInversible(nb_lig):
  inverse = [[0]*nb_lig for i in range(nb_lig)] 
  Q = [[0]*nb_lig for i in range(nb_lig)] 
  M = [[0]*nb_lig for i in range(nb_lig)] 
  
  while (np.array(inverse) == np.array(M)).all():
    Q = aleatoire(nb_lig, nb_lig)
    try:
      inverse = inv(np.array(Q))
    except:
      inverse = [[0]*nb_lig for i in range(nb_lig)] 
      print("Matrice non inversible")
    
  return Q


def aleatoire(n, m):
  M = [[0]*m for i in range(n)] # matrice de n lignes et m colonnes
  for i in range(n):
    for j in range(m):
      M[i][j] = random.randint(0,1)
  return M



def ClefPublique(Q, G, P):
  prod = np.dot(Q, G)
  return( np.dot(prod, P)%2)


# Chiffrement

def c(m, G_pub):
    return(np.dot(m, G_pub)%2)

#Ajout d'une erreur

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
    return(c_2)



#print(erreur([0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1], 3 ))

#G_pub = np.array([[0,1,0,0,1,1,1,1,1,0,0,1,0,1,0], [1,1,1,0,0,1,1,0,1,1,0,0,1,1,0], [1,0,0,1,1,1,0,1,0,0,1,1,0,0,1]])
#m = np.array([1,1,1])
#print(c(m, G_pub))



#Déchiffrement

def dechif(Q, P, G, c_prime):
    G_pub = ClefPublique(Q, G, P) #clef publique
    
    #Inverses de P et Q
    P_1 = inv(np.array(P))
    Q_1 = inv(np.array(Q))
    
    d = np.dot(c_prime, P_1)
    
    N = np.dot(Q, G)%2
    S = np.dot(d, np.transpose(N))%2
    print("syndrome = " + str(S))
    print()
   
    
Q = matriceAleatoireInversible(3)
P = perm(15)
G = Goppa(15, 3, 7)
m = (1, 1, 1)
print(m)
print()
G_pub = ClefPublique(Q, G, P)
c = c(m, G_pub)
print("c = " + str(c))
print()
c_prime = erreur(c, 1)
print("c' = " + str(c_prime))
print()
dechif(Q, P, G, c_prime)
    
    
