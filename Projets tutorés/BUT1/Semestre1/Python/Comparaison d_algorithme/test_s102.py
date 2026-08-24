from SAE102Loic_Moussa import *


def test_create_answers_from_text_file (): 
    fichier= "exemple.txt" 
    f=open(fichier, "w") # Création d'un fichier temporaire 
    f.write("Lisa Fischer:7/4/8/5/7/10/3/7/8/5\n") #chaque ligne contient le nom de l'élève suivi de ses 10 réponses au questionnaire 
    f.write("Donna Weiss:4/6/2/10/2/10/4/8/7/9\n") 
    f.write("Justin Sanchez:6/5/9/2/2/7/6/7/8/4\n") 
    f.close() 
    resultat = { "Lisa Fischer" : [7, 4, 8, 5, 7, 10, 3, 7, 8, 5], 
                 "Donna Weiss" : [4, 6, 2,10, 2, 10, 4, 8, 7, 9], 
                 "Justin Sanchez" : [6, 5, 9, 2, 2, 7, 6, 7, 8, 4] } 
    
    assert create_answers_from_text_file(fichier)== resultat #Vérification de si la fonction nous renvoi le bon résultat 
    print("Tout est bon") 
#-----main----------------- 
test_create_answers_from_text_file()






def test_Euclidean_distance ():
    rep1 = [7, 4, 8, 5, 7, 10, 3, 7, 8, 5]
    rep2 = [4, 6, 2, 10, 2, 10, 4, 8, 7, 9]
    assert Euclidean_distance(rep1, rep2)  == 10.862780491200215 #Vérification de si la fonction nous renvoi le bon résultat 
    assert Euclidean_distance([5, 2, 8, 6, 7, 10, 2, 7, 9, 5], [2, 1, 2, 9, 2, 10, 4, 7, 5, 9])==10.770329614269007
    assert Euclidean_distance(rep1, rep1) == 0 #distance identique est égale à 0
    print("Tout est bon")

#-----main-----------------
test_Euclidean_distance ()






def test_Euclidean_house():
    house=[   
    {
        "house": "Serpentard", 
        "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]
    },
    {
        "house": "Poufsouffle", 
        "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
    }, 
    {
        "house": "Serdaigle", 
        "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]
    }, 
    {
        "house": "Gryffondor", 
        "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]
    } 
    ]


    answer= [9, 4, 5, 3, 9, 2, 5, 1, 8, 2]
    answer2 = [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]
    
    assert Euclidean_house(answer,house)=='Gryffondor' #Vérification de si la fonction nous renvoi le bon résultat 
    assert Euclidean_house(answer,house) !='Serdaigle'
    assert Euclidean_house(answer2,house) =='Serdaigle'#réponse identique à celle de Serdaigle
    print("Tout est bon")
#-----main-----------------
test_Euclidean_house()



def test_Euclidean_repartition():
    dico={
    "Lisa Fischer"   : [7, 4, 8, 5, 7, 10, 3, 7, 8, 5],
    "Donna Weiss"    : [4, 6, 2,10, 2, 10, 4, 8, 7, 9],
    "Justin Sanchez" : [6, 5, 9, 2, 2, 7, 6, 7, 8, 4]
    }

    house=[   
    {
        "house": "Serpentard", 
        "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]
    },
    {
        "house": "Poufsouffle", 
        "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
    }, 
    {
        "house": "Serdaigle", 
        "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]
    }, 
    {
        "house": "Gryffondor", 
        "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]
    } 
    ]
    resultat={
    "Lisa Fischer"   : "Serpentard",
    "Donna Weiss"    : "Serpentard",
    "Justin Sanchez" : "Serdaigle"
    }
    faux_resultat={
    "Lisa Fischer"   : "Serpentard",
    "Donna Weiss"    : "Serpentard",
    "Justin Sanchez" : "Serpentard"
    }
    
    assert Euclidean_repartition(dico, house)== resultat #Vérification de si la fonction nous renvoi le bon résultat 
    assert Euclidean_repartition(dico, house)!= faux_resultat
    print("Tout est bon")
#-----main-----------------
test_Euclidean_repartition()




def test_insertion_position_NN():
    neighbors=[   
    {
        "house": "Serpentard", 
        "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]
    },
    {
        "house": "Poufsouffle", 
        "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
    }, 
    {
        "house": "Serdaigle", 
        "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]
    }, 
    {
        "house": "Gryffondor", 
        "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]
    } 
    ]

    answer=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

    ref={
      "house": "Serdaigle",
      "answer": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    }

    
    ref2={
      "house": "Serdaigle",
      "answer": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    }
    #il y a une faute dans l'énoncé on a écrit anwser au lieu de answer (j'ai corrigé je ne sais pas si j'ai le droit)
    
    assert insertion_position_NN(answer, ref, neighbors)==0 #Vérification de si la fonction nous renvoi le bon résultat 
    assert insertion_position_NN(answer, ref, neighbors)!=2
    assert insertion_position_NN(answer, ref2, neighbors)==4
    print("Tout est bon")
                                 
                                 
#-----main-----------------
test_insertion_position_NN()                                 




def test_insertion_NN():
    neighbors=[   
    {
        "house": "Serpentard", 
        "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]
    },
    {
        "house": "Poufsouffle", 
        "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
    }, 
    {
        "house": "Serdaigle", 
        "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]
    }, 
    {
        "house": "Gryffondor", 
        "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]
    } 
    ]

    answer=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

    ref=  {
        "house": "Serdaigle",
        "answer": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
      }
    #il y a une faute dans l'énoncé on a écrit anwser au lieu de answer (j'ai corrigé je ne sais pas si j'ai le droit)

    resultat= [
        {'house': 'Serpentard', 'answer': [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]},
        {'house': 'Poufsouffle', 'answer': [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]},
        {'house': 'Serdaigle', 'answer': [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]},
        {'house': 'Gryffondor', 'answer': [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]},
        {'house': 'Serdaigle', 'answer': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}]

    assert insertion_NN(answer, ref, neighbors, 4)==neighbors #k = 4 (taille déjà 4), ref est trop loin, il ne doit pas être ajoutée
    assert insertion_NN(answer, ref, neighbors, 5)==resultat
    print("Tout est bon")


#-----main-----------------
test_insertion_NN()







def test_NN():
    answer=[2, 1, 5, 6, 8, 2, 4, 3, 5, 9]

    
    ref=[   
    {
        "house": "Serpentard", 
        "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]
    },
    {
        "house": "Poufsouffle", 
        "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
    }, 
    {
        "house": "Serdaigle", 
        "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]
    }, 
    {
        "house": "Gryffondor", 
        "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]
    } 
    ]

    

    resultat=[
    {
        'house': 'Poufsouffle', 
        'answer': [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
    }, 
    {
        'house': 'Gryffondor', 
        'answer': [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]
    }
    ]

    faux_resultat=[
    {
        'house': 'Poufsouffle', 
        'answer': [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
    }
    ]

    assert NN(answer,ref, 2)== resultat #Vérification de si la fonction nous renvoi le bon résultat 
    assert NN(answer,ref, 2)!= faux_resultat
    print("Tout est bon")


#-----main-----------------
test_NN()





def test_NN_house():

    
    neighbors1=[   
  {
      "house": "Serpentard", 
      "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]
  },
  {
      "house": "Gryffondor", 
      "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
  }, 
  {
      "house": "Serdaigle", 
      "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]
  }, 
  {
      "house": "Gryffondor", 
      "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]
  } 
    ]

    neighbors2=[   
  {
      "house": "Serpentard", 
      "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]
  },
  {
      "house": "Gryffondor", 
      "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
  }, 
  {
      "house": "Serdaigle", 
      "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]
  }, 
  {
      "house": "Gryffondor", 
      "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]
  },
  {
      "house": "Serpentard", 
      "answer": [8, 6, 6, 10, 8, 5, 5, 6, 7, 8]
  } 
    ]


    assert NN_house(neighbors1) == "Gryffondor" #Vérification de si la fonction nous renvoi le bon résultat 
    assert NN_house(neighbors1) != "Serpentard"
    assert NN_house(neighbors2) == "Serpentard"
    print("Tout est bon")


#-----main-----------------
test_NN_house()





def test_NN_repartition():
    dico = {
        "Lisa Fischer":   [7, 4, 8, 5, 7, 10, 3, 7, 8, 5],
        "Donna Weiss":    [4, 6, 2, 10, 2, 10, 4, 8, 7, 9],
        "Justin Sanchez": [6, 5, 9, 2, 2, 7, 6, 7, 8, 4]
    }

    ref=[   
    {
        "house": "Serpentard", 
        "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]
    },
    {
        "house": "Poufsouffle", 
        "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
    }, 
    {
        "house": "Serdaigle", 
        "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]
    }, 
    {
        "house": "Gryffondor", 
        "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]
    } 
    ]

    resultat = {
        "Lisa Fischer": "Serpentard",
        "Donna Weiss": "Serpentard",
        "Justin Sanchez": "Serdaigle"
    }

    
    faux_resultat = {
        "Lisa Fischer": "Gryffondor",
        "Donna Weiss": "Serpentard",
        "Justin Sanchez": "Serdaigle"
    }

    assert NN_repartition(dico, ref, 1) == resultat #Vérification de si la fonction nous renvoi le bon résultat 
    assert NN_repartition(dico, ref, 1) != faux_resultat
    print("Tout est bon")



#-----main-----------------
test_NN_repartition()
