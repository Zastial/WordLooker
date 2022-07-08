
import random
from re import A
import unidecode
import string

def open_the_list(fich):
    with open(f'{fich}.txt') as f:
        lines = f.readlines()
        for mot in lines:
            lines[lines.index(mot)] = unidecode.unidecode(mot.replace("\n",""))
    return lines


def game(namefich, maxHitCount):
    liste_mots = open_the_list(namefich) # Create the list with the words

    motRand = liste_mots[random.randint(0,len(liste_mots)-1)]
    motRand = motRand.lower()
    print(motRand) # Choose and display a random word

    score = ["_ " for i in range(len(motRand))]
    print("".join(score), '\n') # Create the score which will be the correct letters entered

    hitCount = 0
    print(f'number of max moves : {maxHitCount} | number of bad moves made : {hitCount}', '\n')

    alreadySeen = []

    notfind = True
    while(notfind): # While every letter as not been found, the game continue

        notAlpha = True
        while(notAlpha): # Check if the input is a letter
            ask = input("Give a letter to see if it's in the word : ")
            if ask in string.ascii_lowercase and ask not in alreadySeen:
                notAlpha = False

        for i in range(len(motRand)):
            if(ask == motRand[i]): # If the letter entered is in the word chose a the start, it'll be displayed
                score[i] = motRand[i]
        alreadySeen.append(ask)

        if ask not in motRand:
            hitCount += 1

        print("".join(score), '\n') # Display the score each time the player enters a letter
        print(f'number of max moves : {maxHitCount} | number of bad moves made : {hitCount}', '\n')
        print(f'Letters already entered : {", ".join(alreadySeen)}')

        if hitCount == maxHitCount:
            print("Sorry you loose !")
            break

        cpt = 0
        for v in score: #Check if the game is finished
            if v != "_ ":
                cpt+=1
        if cpt == len(motRand):
            notfind = False

    if notfind == False:
        print("Good job ! You found the word !!")


game("liste_francais",5)