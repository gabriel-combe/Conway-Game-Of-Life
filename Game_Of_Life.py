import numpy as np #importation de la librairie numpy pour calcul matricielle

# defintion des cases autour du point p
#   1   2   3     z   y   x
#   4   P   5  =  r   p   w
#   6   7   8     t   u   v

def nombre_voisins(X, Y): #compte le nombre de voisin selon différente configuration

    if X != 0 and X != nb-1 and Y == 0 :
        #print("Flan Gauche")
        listpos = [matrice[X-1,Y], matrice[X-1,Y+1], matrice[X,Y+1], matrice[X+1,Y+1], matrice[X+1,Y]] #dans l'ordre, position 2(y), 3(x), 5(w), 8(v), 7(u)
        voisins = comparaisons(listpos) #utilisation des cellules 2, 3, 5, 7, 8

    elif X != 0 and X != nb-1 and Y == nb-1 :
        #print("Flan Droit")
        listpos = [matrice[X-1,Y-1], matrice[X-1,Y], matrice[X+1,Y], matrice[X+1,Y-1], matrice[X,Y-1]] #dans l'ordre, position 1(z), 2(y), 7(u), 6(t), 4(r)
        voisins = comparaisons(listpos) #utilisation des cellules 1, 2, 4, 6, 7

    elif X == 0 and Y != 0 and Y != nb-1  :
        #print("Flan Haut")
        listpos = [matrice[X,Y+1], matrice[X+1,Y+1], matrice[X+1,Y], matrice[X+1,Y-1], matrice[X,Y-1]] #dans l'ordre, position 5(w), 8(v), 7(u), 6(t), 4(r)
        voisins = comparaisons(listpos) #utilisation des cellules 4, 5, 6, 7, 8

    elif X == nb-1 and Y != 0 and Y != nb-1 :
        #print("Flan Bas")
        listpos = [matrice[X-1,Y-1], matrice[X-1,Y], matrice[X-1,Y+1], matrice[X,Y+1], matrice[X,Y-1]] #dans l'ordre, position 1(z), 2(y), 3(x), 5(w), 4(r)
        voisins = comparaisons(listpos) #utilisation des cellules 1, 2, 3, 4, 5

    elif X == 0 and Y == 0 :  # angle en haut a gauche
        #print("Position Angle Bas Droite")
        listpos = [matrice[X,Y+1], matrice[X+1,Y+1], matrice[X+1,Y]] #dans l'ordre, position 5(w), 8(v), 7(u)
        voisins = comparaisons(listpos) #utilisation des cellules 5, 8, 7

    elif X == 0 and Y == nb-1 :  # angle en haut a droite
        #print("Position Angle Bas Gauche")
        listpos = [matrice[X+1,Y], matrice[X+1,Y-1], matrice[X,Y-1]] #dans l'ordre, position 7(u), 6(t), 4(r)
        voisins = comparaisons(listpos) #utilisation des cellules 7, 6, 4

    elif X == nb-1 and Y == 0:  # angle en bas a gauche
        #print("Position Angle Haut Droite")
        listpos = [matrice[X-1,Y], matrice[X-1,Y+1], matrice[X,Y+1]] #dans l'ordre, position 2(y), 3(x), 5(w)
        voisins = comparaisons(listpos) #utilisation des cellules 2, 3, 5

    elif X == nb - 1 and Y == nb - 1 :  # angle en bas a droite
        #print("Position Angle Haut Gauche")
        listpos = [matrice[X-1,Y-1], matrice[X-1,Y], matrice[X,Y-1]] #dans l'ordre, position 1(z), 2(y), 4(r)
        voisins = comparaisons(listpos) #utilisation des cellules 1, 2, 4

    elif X != 0 or Y != 0 or X != nb-1 or Y != nb-1:
        #print("position centrale")
        listpos = [matrice[X-1,Y-1], matrice[X-1,Y], matrice[X-1,Y+1], matrice[X,Y+1], matrice[X+1,Y+1], matrice[X+1,Y], matrice[X+1,Y-1], matrice[X,Y-1]] #dans l'ordre, position 1(z), 2(y), 3(x), 5(w), 8(v), 7(u), 6(t), 4(r)
        voisins = comparaisons(listpos) #utilisation de toutes les positions

    return voisins

def boucle(phase): #boucle de passage de toutes les coordonnées des matrices
    X = 0
    Y = 0
    
    while X < nb :
        while Y < nb :

            if phase == 1:
                voisins_matrice(nombre_voisins(X, Y), X, Y) #remplit une matrice du nombre de voisins correspondant à chaque cellule
            if phase == 2:
                dead_or_alive(X, Y) #détermine si une cellule doit vivre ou mourir (dead or alive)

            Y += 1
            voisins = 0

        X += 1
        Y = 0

def request(string, etat):
    demande = 1
    if etat == "nb":
        demande = input(string)
        if demande.isdecimal() :
            return demande
        else:
            print("Error : veuillez entre un nombre entier naturel")
            request(string, "nb")
    if etat == "bin":
        demande = input(string)
        if demande == "0" or demande == "1":
            return demande
        else:
            print("Error : veuillez entrer 0 ou 1")
            request(string, "bin")

def dead_or_alive(X,Y): #fonction de décision de vie ou de mort d'une cellule
    if matrice_voisins[X, Y] == 3 and matrice[X, Y] == 0 : #conditions de vie
        matrice[X, Y] = 1 #la cellule vie
    if matrice_voisins[X, Y] != 3 and matrice_voisins[X, Y] != 2 and matrice[X, Y] == 1 : #conditions de mort
        matrice[X, Y] = 0 #la cellule meurt

def voisins_matrice(voisins, X, Y): #fonction qui assigne à chaque cellule sont nombre de voisins dans une matrice
    matrice_voisins[X,Y] = voisins #assignation du nombre de voisins dans la cellule correspondant à la position actuel dans notre matrice principale
    #print (voisins)
    #print ("matrice voisins = \n" + str(matrice_voisins))

def comparaisons(listpos): #fonction de comparaison des cellules aux allantours de la cellule visée afin de déterminer le nombvre de voisins 
    voisins = 0
    for i in listpos: #passage dans les éléments de la liste de cellule voisines
        if i == 1 :
            voisins += 1 
    return voisins

def affichage_et_init(): #affichage et initialisation de la matrice principale
    X = 0
    Y = 0

    print("Voici la grille vierge : ")
    print(matrice)
    while (X < nb):
        while (Y < nb):
            matrice[X,Y] = int(request(("Cellule morte 0 ou Vivante 1 pour la cellule à (" + str(X) + " ; " + str(Y) + ") : "), "bin"))
            Y += 1
            print(matrice)

        Y = 0
        X += 1
    print("Initialization Completed...")
    X = 0
    Y = 0

    print(matrice)
    return matrice


def start(Gene): #fonction de lancement du jeu de la vie
    matrice = affichage_et_init() #assignation de la matrice initialisé à la variable matrice
    B_un = 0

    while B_un < Gene : #boucle de génération

        boucle(1) #utilisation de la fonction boucle en phase 1
        boucle(2) #utilisation de la fonction boucle en phase 2

        B_un += 1

        print("\n \n Génération " + str(B_un) + " Matrice finale : ")
        print (matrice) #matrice finale après chaque génération

while True: #répétition indfinie du processus
    nb = int(request(("Entre la taille de la grille vous souhaitez avoir : "), "nb")) #demande de la taille de la matrice carrée
    Gene = int(request(("Entre le nombre de generation que vous souhaitez afficher : "), "nb")) #demande du nombre de génération

    matrice = np.zeros((nb,nb)) #remplissage de la matrice principale par des zeros selon la taille donnée
    matrice_voisins = np.zeros((nb,nb)) #remplissage de la matrice des voisins par des zeros selon la taille donnée

    start(Gene) #lancement du processus du jeu de la vie

    print("\n \n \n \n \n")
