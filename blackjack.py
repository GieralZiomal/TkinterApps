import random

def endGame(playerDeck, croupierDeck, Cards, playerBet, Balance):
    playerSum = []
    for x in range(len(playerDeck)):
        playerSum.append(Cards[playerDeck[x]])
    playerSum = sum(playerSum)
    croupierSum = []
    for x in range(len(croupierDeck)):
        croupierSum.append(Cards[croupierDeck[x]])
    croupierSum = sum(croupierSum)

    if playerSum > 21:
        print("Przegrałeś!")
        New_Balance = Balance - playerBet
        setupGame(New_Balance)

    else:
        print(f"Krupier Odkrywa Karty. \n {croupierDeck} a wartość to: {croupierSum}")
        if croupierSum <= 16: 
            pass
        elif croupierSum >= 17:
            croupierDeck.append(random.choice(list(Cards)))
            croupierSum += int(Cards[croupierDeck[-1]])
            print(f"Krupier Musiał Dobrać Kartę! \n {croupierDeck} a wartość to: {croupierSum}")
    
    twoDeck = {croupierSum:"Krupier", playerSum:"Gracz"}
    croupierSum = abs(croupierSum-21)
    playerSum = abs(playerSum-21)
    if croupierSum < playerSum:
        print("Przegrałeś!")
        New_Balance = Balance - playerBet
        setupGame(New_Balance)
    else:
        print("Brawo wygrałeś!")
        New_Balance = Balance + playerBet + playerBet/2
        setupGame(New_Balance)

def setupGame(Balance):
    Balance = Balance
    if Balance <= 0:
        print("Nie masz już pieniędzy! Spróbuj od nowa!")
        firstGame()
    else:
        pass
    print(f"Masz {Balance} Złoty")
    playerBet = input("Ile chcesz obstawić?: ")
    playerBet = int(playerBet)
    Cards = {"Dwójka":2,"Trójka":3,"Czwórka":4,
             "Piątka":5,"Szóstka":6,"Siódemka":7,
             "Ósemka":8,"Dziewiątka":9,"Dziesiątka":10,
             "Walet":10,"Dama":10,"Król":10, "As":11}
    playerDeck = []
    croupierDeck = []
    for x in range (2):
        playerDeck.append(random.choice(list(Cards)))
        croupierDeck.append(random.choice(list(Cards)))
    print(f'Twoje Karty to {playerDeck}\nKarta Krupiera to {croupierDeck[0]}')
    print("Co chcesz zrobić? \n1.Hit 2.Stand 3.Double Down 4.Split 5.Insurance")
    odp = input("Twój wybór to: ")
    print(odp)
    if odp == "Hit":
       playerDeck.append(random.choice(list(Cards)))
       print(f"Dobrano Kartę! Masz : {playerDeck}")
       endGame(playerDeck, croupierDeck, Cards, playerBet, Balance)
    elif odp == "Stand":
        endGame(playerDeck, croupierDeck, Cards, playerBet, Balance)
    elif odp == "Double Down":
        pass
    elif odp == "Split":
        pass
    elif odp == "Insurance":
        pass


def firstGame():
    startingBalance = 100
    print("Witaj w Kasynie Jakuba\nPamiętaj ,że 99% przerywa grę przed wielką wygraną\nRozgrywka BlackJack:")
    inp = input("Czy chcesz zacząć grę T/N?\n")
    inp = inp.upper()
    if inp == "T":
        setupGame(startingBalance)


firstGame()