import random
rejouer = True
tentatives = 12
couleurs = ["R", "B", "G", "Y", "M"]
code_secret = random.choices(couleurs, k=4)
print("Le code secret creer est: ", code_secret)
print("debut du jeu")

while rejouer == True:
    fichier = open("C:/Users/loren/Desktop/Polytech_dijon/Soutien info/Tp_7/Score.txt", "a")
    fichier.write("Debut de partie" + "\n")
    fichier.close()
    while tentatives > 0:
        proposition = input("Entrez votre proposition (4 lettres parmi R, B, G, Y, M): ").upper()

        if list(proposition) == code_secret:
            print("Félicitations ! Vous avez trouvé le code secret.")
            fichier = open("C:/Users/loren/Desktop/Polytech_dijon/Soutien info/Tp_7/Score.txt", "a")
            fichier.write("Le nb de tentatives était: " + str(12 - tentatives) + "\n")
            fichier.close()
            break     
        else:
            tentatives -= 1
            corect = 0
            for i in range(4):
                if proposition[i] == code_secret[i]:
                    corect += 1
            partiel = 4 - corect
            print("Mauvaise proposition. Vous avez", corect, " couleurs correctes et", partiel, "couleurs Incorect." "il vous reste", tentatives, "tentatives.")
            if tentatives == 0:
                print("Vous avez épuisé toutes vos tentatives. Le code secret était:", code_secret)
    print("Voulez-vous rejouer ? (oui/non)")
    reponse = input()
    if reponse == "non":
        rejouer = False
        print("Merci d'avoir joué !")
        fichier = open("C:/Users/loren/Desktop/Polytech_dijon/Soutien info/Tp_7/Score.txt", "a")
        fichier.write("Fin de partie" + "\n")
        fichier.close()
        reinstialisation = input("Voulez-vous réinitialiser le fichier de score ? (oui/non) : ")
        if reinstialisation == "oui":
            fichier = open("C:/Users/loren/Desktop/Polytech_dijon/Soutien info/Tp_7/Score.txt", "w")
            fichier.write("") 
            print("Le fichier de score a été réinitialisé.")

        print("Merci d'avoir joué !")