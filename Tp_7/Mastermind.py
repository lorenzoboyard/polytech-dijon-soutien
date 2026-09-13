import random

tentatives = 12
couleurs = ["R", "B", "G", "Y", "M"]
code_secret = random.choices(couleurs, k=4)
print("Le code secret creer est: ", code_secret)

while tentatives > 0:
    proposition = input("Entrez votre proposition (4 lettres parmi R, B, G, Y, M): ")

    if list(proposition) == code_secret:
        print("Félicitations ! Vous avez trouvé le code secret.")
        break
    else:
        tentatives -= 1
        corect = 0
        for i in range(4):
            if proposition[i] == code_secret[i]:
                corect += 1
        partiel = 4 - corect
        print("Mauvaise proposition. Vous avez", corect, " couleurs correctes et", partiel, "couleurs partiellement correctes." "il vous reste", tentatives, "tentatives.")
        if tentatives == 0:
            print("Vous avez épuisé toutes vos tentatives. Le code secret était:", code_secret)
