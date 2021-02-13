import random
from os import system
from sys import platform
from time import sleep

print("\n")
prima_scelta = input("Vuoi giocare? Sì/No ")  # asks player if he wants to play
while prima_scelta[0] not in "sSnN" or prima_scelta.isspace():  # checks player input
    print("Inserisci un valore valido!")
    prima_scelta = input("Vuoi giocare? Sì/No ")
if prima_scelta[0] in "nN":
    print("\nAlla prossima!")
    sleep(1)
    exit()
conto, conto_pesca, conto_banco, conto_pesca_banco, conto_nascosto = 0, 0, 0, 0, 0  # variables for card value counting


class Card:  # I don't know how to use classes and I never found a good tutorial :D
    semi = ["♠", "♥", "♦", "♣"]
    numeri = ["Asso", "Due", "Tre", "Quattro", "Cinque", "Sei", "Sette", "Otto", "Nove", "Jack", "Regina", "Re"]
    mazzo = []
    tue_carte = []
    carte_banco = []


carte = Card()


def deck_builder():  # deck building
    for x in carte.semi:
        for y in carte.numeri:
            carte.mazzo.append(y + " di " + x)
    return carte.mazzo


def shuffler(deck):  # deck shuffler
    random.shuffle(deck)
    return deck


def pesca_carta(deck):  # user hit
    try:
        if platform == "linux" or platform == "linux2":
            system("clear")
        else:
            system("cls")
    except:
        pass
    carta_index = random.randint(0, len(deck) - 1)
    global carta
    carta = deck[carta_index]
    deck.remove(carta)
    carte.tue_carte.append(carta)
    return "\nHai pescato: " + carta + "\n"


def pesca_banco(deck):  # dealer hit
    carta_index = random.randint(0, len(deck) - 1)
    carta_banco = deck[carta_index]
    deck.remove(carta_banco)
    carte.carte_banco.append(carta_banco)
    return "Il banco ha pescato: " + carta_banco + "\n"


def seconda_pesca_banco(deck):  # second dealer hit, it is hidden if I remember the rules well
    carta_index = random.randint(0, len(deck) - 1)
    global carta_banco
    global carta_nascosta
    carta_banco_coperta = deck[carta_index]
    deck.remove(carta_banco_coperta)
    carte.carte_banco.append("*Carta Coperta*")
    carta_nascosta = carta_banco_coperta
    return carta_banco_coperta


def rivela_carta(card):  # reveals hidden dealer card
    carte.carte_banco.pop(1)
    carte.carte_banco.insert(1, card)


def conta_carte_banco(card):  # counts dealer cards
    global conto_banco
    global conto_pesca_banco
    conto_pesca_banco += 1
    if conto_pesca_banco != 2:
        if "Asso" in card:
            if (conto_banco + 11) <= 21:
                conto_banco += 11
            else:
                conto_banco += 1
        elif "Due" in card:
            conto_banco += 2
        elif "Tre" in card:
            conto_banco += 3
        elif "Quattro" in card:
            conto_banco += 4
        elif "Cinque" in card:
            conto_banco += 5
        elif "Sei" in card:
            conto_banco += 6
        elif "Sette" in card:
            conto_banco += 7
        elif "Otto" in card:
            conto_banco += 8
        elif "Nove" in card:
            conto_banco += 9
        elif "Jack" in card or "Regina" in card or "Re" in card:
            conto_banco += 10
    else:
        global conto_nascosto
        if "Asso" in card:
            if (conto_banco + 11) <= 21:
                conto_nascosto += 11
            else:
                conto_nascosto += 1
        elif "Due" in card:
            conto_nascosto += 2
        elif "Tre" in card:
            conto_nascosto += 3
        elif "Quattro" in card:
            conto_nascosto += 4
        elif "Cinque" in card:
            conto_nascosto += 5
        elif "Sei" in card:
            conto_nascosto += 6
        elif "Sette" in card:
            conto_nascosto += 7
        elif "Otto" in card:
            conto_nascosto += 8
        elif "Nove" in card:
            conto_nascosto += 9
        elif "Jack" in card or "Regina" in card or "Re" in card:
            conto_nascosto += 1
    if conto_pesca_banco < 2 and (conto_banco + conto_nascosto) < 21:
        return "Il punteggio del banco è: " + str(conto_banco) + "\tCarte banco: " + str(carte.carte_banco) + "\n"
    elif conto_pesca_banco == 21:
        print("Blackjack per il banco!")
        global carta_nascosta
        rivela_carta(carta_nascosta)
        print("Il punteggio del banco è: " + str(conto_banco) + "\tCarte banco: " + str(carte.carte_banco) + "\n")
        if conto < 21:
            print("Mi dispiace, hai perso!")
            exit()
        else:
            print("Pareggio!")
            exit()
    elif conto_pesca_banco == 2:
        print("Il punteggio del banco è: " + str(conto_banco) + "\tCarte banco: " + str(carte.carte_banco) + "\n")
    elif conto_pesca_banco > 2:
        rivela_carta(carta_nascosta)
        print("Il punteggio del banco è: " + str(conto_banco + conto_nascosto) + "\tCarte banco: " + str(
            carte.carte_banco) + "\n")


def conta_carte(card):  # counts user cards
    global conto
    global conto_pesca
    conto_pesca += 1
    if "Asso" in card:
        valore_asso = (input("Hai pescato un asso. Che valore gli vuoi far avere? 1/11: "))
        if valore_asso == "11":
            conto += 11
        elif valore_asso == "1":
            conto += 1
        else:
            conto += 1
    elif "Due" in card:
        conto += 2
    elif "Tre" in card:
        conto += 3
    elif "Quattro" in card:
        conto += 4
    elif "Cinque" in card:
        conto += 5
    elif "Sei" in card:
        conto += 6
    elif "Sette" in card:
        conto += 7
    elif "Otto" in card:
        conto += 8
    elif "Nove" in card:
        conto += 9
    elif "Jack" in card or "Regina" in card or "Re" in card:
        conto += 10
    if conto < 21:
        print("Il tuo punteggio totale è: " + str(conto) + "\tLe tue carte: " + str(carte.tue_carte) + "\n")
    else:
        print("Le tue carte: " + str(carte.tue_carte) + "\n")


shuffler((deck_builder()))  # shuffles deck
carta_pescata = (pesca_carta(carte.mazzo))  # picks card
print(carta_pescata)
sleep(1)
(conta_carte(carta_pescata))  # counts user card value
carta_pescata_banco = pesca_banco(carte.mazzo)
conta_carte_banco(carta_pescata_banco)
carta_pescata = (pesca_carta(carte.mazzo))  # picks card
print(carta_pescata)
sleep(1)
(conta_carte(carta_pescata))  # counts user card value
seconda_pescata_banco = seconda_pesca_banco(carte.mazzo)  # hidden card
conta_carte_banco(seconda_pescata_banco)  # counts hidden card
while conto < 21:
    scelta_player = input("Stare o Pescare? \"S\" per stare, \"P\" per pescare: ")  # asks user hit or stand
    while scelta_player not in "sSpP":
        print("Inserisci un input valido!")
        scelta_player = input("Stare o Pescare? \"S\" per stare, \"P\" per pescare: ")
    if scelta_player in "pP":  # hit
        carta_pescata = (pesca_carta(carte.mazzo))
        print(carta_pescata)
        sleep(1)
        (conta_carte(carta_pescata))
    else:  # stand
        while (conto_banco + conto_nascosto) < 17:
            carta_pescata_banco = pesca_banco(carte.mazzo)
            conta_carte_banco(carta_pescata_banco)
            sleep(1)
        else:
            if conto < (conto_banco + conto_nascosto) <= 21: #loss because dealer is higher
                print("Mi dispiace, hai perso!")
                print("\nIl tuo punteggio finale è: " + str(conto) + "\tLe tue carte: " + str(carte.tue_carte))
                print(
                    "\nIl punteggio finale del banco è: " + str(conto_banco + conto_nascosto) + "\tCarte banco: " + str(
                        carte.carte_banco) + "\n")
                exit()
            if (conto_banco + conto_nascosto) == conto: # draw
                print("Pareggio!")
                print("\nIl tuo punteggio finale è: " + str(conto) + "\tLe tue carte: " + str(carte.tue_carte))
                print("\nIl punteggio finale del banco è: " + str(
                    conto_banco + conto_nascosto) + "\tCarte banco: " + str(carte.carte_banco) + "\n")
                exit()
            else:
                print("Complimenti, hai vinto!") # win
                print("\nIl tuo punteggio finale è: " + str(conto) + "\tLe tue carte: " + str(carte.tue_carte))
                print("\nIl punteggio finale del banco è: " + str(
                    conto_banco + conto_nascosto) + "\tCarte banco: " + str(carte.carte_banco) + "\n")
                exit()
        print("\nIl tuo punteggio finale è: " + str(conto) + "\tLe tue carte: " + str(carte.tue_carte))
        break
else:
    if conto == 21:
        if conto_pesca == 2: # blackjack
            print("Complimenti, Blackjack!")
        else:
            print("Complimenti, il tuo punteggio finale è 21!")
    elif conto > 21: #loss because over 21
        while (conto_banco + conto_nascosto) < 17:
            carta_pescata_banco = pesca_banco(carte.mazzo)
            conta_carte_banco(carta_pescata_banco)
        print("\nPeccato...Magari vincerai la prossima volta!")
        print("\nIl tuo punteggio finale è: " + str(conto) + "\tLe tue carte: " + str(carte.tue_carte))
        print("\nIl punteggio finale del banco è: " + str(conto_banco + conto_nascosto) + "\tCarte banco: " + str(
            carte.carte_banco) + "\n")
        exit()
