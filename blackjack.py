#silly important stuff

from random import  Random
import time

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
playerHand = []
dealerHand = []

def getCard():
    return Random().choice(deck)

def calcScore(playerHand):
    playerScore = 0
    for i in range(playerHand.__len__()):
        if playerHand[i] == "J" or playerHand[i] == "Q" or playerHand[i] == "K":
            playerScore += 10
        elif playerHand[i] == "A":
            playerScore += 11
        else:
            playerScore += int(playerHand[i])
    return playerScore

def calcDealerScore(dealerHand):
    dealerScore = 0
    for i in range(dealerHand.__len__()):
        if dealerHand[i] == "J" or dealerHand[i] == "Q" or dealerHand[i] == "K":
            dealerScore += 10
        elif dealerHand[i] == "A":
            dealerScore += 11
        else:
            dealerScore += int(dealerHand[i])
    return dealerScore

def checkWin(playerScore):
    if playerScore == 21:
        print("You won!")
        return True
    elif playerScore > 21:
        print("You lost!")
        return True
    else:
        return False

def checkWinDealer(dealerScore):
    if dealerScore == 21:
        print("Dealer won!")
        return True
    elif dealerScore > 21:
        print("Dealer lost! You won!")
        return True
    else:
        return False

def checkWinFinal(playerScore, dealerScore):
    if currentDealerScore > currentPlayerScore:
        print("Dealer won! You lost!")
        return True
    elif currentDealerScore == currentPlayerScore:
        print("draw!")
        return True
    else:
        print("You lost!")
        return True


#the game itself

for _ in range(2):
    playerHand.append(getCard())
    dealerHand.append(getCard())
print("Here's your hand:\n", playerHand); time.sleep(1.5)
print("Here's the dealer's hand:\n", dealerHand)

gameOver = False

while not gameOver:
    currentPlayerScore = calcScore(playerHand)
    currentDealerScore = calcDealerScore(dealerHand)

    gameOver = checkWin(currentPlayerScore)
    gameOverDealer = checkWinDealer(currentDealerScore)
    if gameOver or gameOverDealer:
        break

    hitOrStand = input("Hit or stand? (H/S)")

    if hitOrStand.upper() == "H":
        newCard = getCard()
        playerHand.append(newCard)
        print("Here's your hand:\n", playerHand)
    elif hitOrStand.upper() == "S":
        if currentDealerScore < 17:
            print("Dealer's hand is lower then 17, dealer draws a card"); time.sleep(1.5)
            newDealerCard = getCard()
            dealerHand.append(newDealerCard)
            print("Here's the dealer's new hand:\n", dealerHand)
        else:
            checkWinFinal(currentPlayerScore, currentDealerScore)
    else:
        print("Sorry, that's not a valid choice. Please type H or S. Silly")

