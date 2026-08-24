#Question n°1

def create_answers_from_text_file (nom_fichier):
    
    """Cette fonction lit un fichier contenant les réponses aux questionnaires ( 10 réponses), 
    prenant en paramètre un nom de fichier contenant les réponses aux questionnaires des élèves. 
    Et elle retourne un dictionnaire dont les clés sont les noms des élèves et
    les valeurs sont les listes des 10 réponses du questionnaires"""
    
    
    dico_rep={}
    f=open(nom_fichier) #ouverture du fichier (lecture)

    for ligne in f : #parcours chaque ligne du fichier
        answer=[]
        ligne=ligne.strip() #suppression des sauts de lignes et espaces inutiles
        nom_rep= ligne.split(":") #sépare nom et réponses
        nom= nom_rep[0] #nom de l'élève
        reponses= nom_rep[1].split("/") #liste des réponses
        i=0
        while i < len(reponses):
            answer.append(int(reponses[i]))#conversion des réponses en entier
            i+=1
        dico_rep[nom]=answer #l'ajoute dans le dictionnaire 
    f.close()
    return dico_rep

#-----main-----------------

create_answers_from_text_file("questionnaire_premiere_annee_10q.txt")

#Question n°2

from math import sqrt

def Euclidean_distance (rep1, rep2):
    """Cette fonction calcule la distance euclidienne entre deux réponses au questionnaire, 
    prenant en paramètre deux réponses et retournant la différence entre ces deux réponses 
    en utilisant la formule de la distance Euclidienne."""

    
    calcul=0 #somme de la différence entre les carrés
    i=0
    while i < len(rep1): #parcourt toute les réponses
        calcul+=(rep1[i]-rep2[i])**2 #différence entre les réponses à la question i
        i+=1
        
    return sqrt(calcul) #racine carré de la somme pour avoir la distance euclidienne




#Question n°3


def Euclidean_house(answer,house):
    """Cette fonction détermine la maison à laquelle affecter un élève grâce à la distance euclidienne,
    prenant en paramètre une réponse et un ensemble de références, 
    et retournant la maison à laquelle affecter l'élève qui a donné cette réponse"""

    
    mini= Euclidean_distance (answer, house[0]["answer"]) #distance minimale initialisée avec la première référence
    maison=[]#liste des maisons
    indice=0 #indice de la maison la plus proche 
    i=0

    while i < len(house): #parcourt toute les réferences
        maison.append(house[i]["house"]) #ajoute le nom des maisons
        distance= Euclidean_distance (answer, house[i]["answer"]) #calcul de la distance entre l'élève et la réference i
        if distance <= mini:#mets à jour si la distance est la plus petite ou égale
            mini= distance
            indice=i
        i+=1

    return maison[indice] #retourne la maison ayant la distance minimale



#Question n°4

from s101 import nb_erreurs

def Euclidean_repartition (dico, house):
    """Cette fonction affecte chaque élève à une maison avec la méthode euclidienne, 
    prenant un dictionnaire de réponses et un ensemble de références.
    La fonction doit retourner un dictionnaire dont les clés sont les noms des élèves 
    et les valeurs la maison(affectés avec la méthode de la distance Euclidienne)"""
    

    d={}
    for cle, valeur in dico.items(): #parcourt chaque élève et ses réponses
        d[cle]= Euclidean_house(valeur,house)#maison du plus proche voisin parmi les références
    return d
    
    
#Question n°6

def insertion_position_NN (answer, ref, neighbors):

    
    """Cette fonction détermine la position d'insertion d'une référence dans un tableau
    de voisins déjà trié du plus proche au moins proche,
    prenant en paramètre: la réponse d'un élève answer, une référence ref,
    un tableau de références trié du plus proche au moins proche neighbors 
    et retourne 'indice auquel insérer ref dans le tableau neighbors pour que ce dernier reste trié du plus proche au moins proche"""

    
    reference= Euclidean_distance (answer, ref["answer"])#distance entre l'élève et la réference à insérer
    position = 0
    while position < len(neighbors):#parcourt les voisins qui existent déjà
        if  Euclidean_distance (answer, neighbors[position]["answer"]) >= reference: #si la réference est plus proche que le voisin existant
            return position #retourne la position d'insertion
        position+=1
        
    return position
    
    
    
    
#Question n°7

def insertion_NN (answer, ref, neighbors, k):
    
    """Cette fonction insère une référence dans un tableau de voisins trié du plus proche
    au moins proche, en conservant au plus k voisins, 
    prenant en paramètre: la réponse d'un élève answer, une référence ref, 
    un tableau de références trié du plus proche au moins proche neighbors, et un entier k tel que len(neighbors) <= k.
    Et retournant la liste neighbors mise à jour"""

    
    position=insertion_position_NN (answer, ref, neighbors)#détermine la postion d'insertion
    if position >= k:#si la réference n'appartient pas aux k plus proche voisins
        return neighbors
        
    neighbors.append(ref)#on ajoute temporairement la réference à la fin de liste
    j=len(neighbors)-1
    while j> position:#on décale les éléments vers la droite
        neighbors[j] = neighbors[j-1]
        j -= 1
    neighbors[position] = ref #insertion de la réference à la bonne position
    
    if len(neighbors)>k:#suppression du voisin le plus éloigné si la taille dépasse k
        neighbors.pop()
            
    return neighbors


#Question n°8

def NN (answer,ref, k):
    """Cette fonction détermine les k plus proches voisins d'un élève à partir
    d'un ensemble de références, en utilisant la distance euclidienne,
    prenant en paramètre la réponse d'un élève, un tableau de références et un entier k 
    et retournant un tableau des k plus proches voisins triés du plus proche au moins proche"""


    
    proche=[] #liste des k voisins les plus proches
    j=0
    while j < len(ref):#parcourt toutes les références
        insertion_NN (answer, ref[j], proche, k)#insertion de la réfrence à la bonne position dans la liste proche
        j+=1
        
        
    return proche



#Question n°9
def NN_house (neighbors):

    """Cette fonction détermine la maison d'affectation d'un élève à partir
    de ses k plus proches voisins, prenant en paramètre un tableau de voisins neighbors 
    et retournant la maison d'affectation de l'élève dont neighbors représente les plus proches voisins"""
    
    
    Serpentard=[]#les listes contenant les indices des voisins par maison
    Serdaigle=[]
    Gryffondor=[]
    Poufsouffle=[]
    
    i=0
    while i < len(neighbors):#parcourt tout les voisins
        if neighbors[i]["house"]=="Poufsouffle":
            Poufsouffle.append(i)
        elif neighbors[i]["house"]=="Serpentard":
            Serpentard.append(i)
            
        elif neighbors[i]["house"]=="Gryffondor":
            Gryffondor.append(i)

        else:
            Serdaigle.append(i)

        i+=1
    nom=["Serpentard", "Serdaigle", "Gryffondor", "Poufsouffle"]  #noms des maisons dans le même ordre que dans la liste house  
    house=[Serpentard, Serdaigle, Gryffondor, Poufsouffle]
    i=0
    maxi=0 #nombre maximal de voisins pour une maison
    indmax=0 #indice de cette maison 
    while i < len(house):
        
        if maxi< len(house[i]):
            maxi=len(house[i])
            maison=house[i]
            indmax=i
            
        elif maxi==len(house[i]) and maxi > 0: # si c'est égale on choisit la maison où le voisin est le plus proche (car liste déjà triée)
            if  house[i][0]<house[indmax][0]:
                maxi=len(house[i])
                maison=house[i]
                indmax=i
        i+=1

    return nom[indmax] #retourne le nom de la maison
            



#Question n°10
def NN_repartition(dico, ref, k):

    """cette fonction affecte chaque élève à une maison en utilisant la méthode
    des k plus proches voisins, 
    prenant en paramètre : un dictionnaire de réponses, un ensemble de références et un entier k
    et retournantun dictionnaire dont les clés sont les noms des élèves et les valeurs la maison (avec la méthode des k plus proches voisins)"""

    
    d={}
    for cle, valeur in dico.items():#parcourt chaque élève et ses réponses
      
        val=NN(valeur,ref,k)#recherche des k plus proches voisins de l'élève
        maison= NN_house(val)
        d[cle]= maison
        
    return d
