from random import randint

def inputUserNbr(nbLoop) -> int:
    print("Veuillez entrer un nombre entre 0 et 100 (", nbLoop, "/ 20) : ")
    userNbr = int(input("$> "))
    while (userNbr < 0 or userNbr > 100) :
            print("Veuillez entrer un nombre entre 0 et 100 (", nbLoop, "/ 20) : ")
            userNbr = int(input("$> "))
    return userNbr

def loop(aleatNbr):
    condition = True
    nbLoop = 1
    while (condition == True) :
        userNbr = inputUserNbr(nbLoop)
        if (userNbr > aleatNbr) :
            print("C'est moins")
        else :
            print("C'est plus")
        nbLoop += 1
        if (userNbr == aleatNbr or nbLoop > 20) :
            condition = False
    if (userNbr == aleatNbr) :
        print("Vous avez gagné !")
    else :
        print("Vous avez perdu !")

def game():
    play = "oui"
    while (play.lower() == "oui") :
        aleatNbr = randint(0, 100)
        loop(aleatNbr)
        play = input("Voulez-vous rejouer ? (Oui/Non)")
    print("Vous allez nous manquer")

def main():
    print("Bienvenue dans le jeu du plus ou moins")
    game()

main()