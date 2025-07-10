from poker_game import *
from check_hands import *
from itertools import combinations

cardList = ["Ac", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc",
            "Ah", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh",
            "Ad", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd",
            "As", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks"]

def getNumPlayers():
    while True:
        try:
            numPlayers = int(input("Enter number of players (2–10): "))
            if 2 <= numPlayers <= 10:
                break
            else:
                print("Please enter a number between 2 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return numPlayers

def selectCards(cardList):
    while True:
        try:
            cardInput = input("Select both cards: (Ex: Ac Ad) ")
            cards = cardInput.split(" ")
            if cards[0] in cardList and cards[1] in cardList:
                cardList.remove(cards[0])
                cardList.remove(cards[1])
                break
            else:
                print("Please enter two valid cards")
        except ValueError:
            print("Invalid input. Please enter a valid hand.")
    return cards

def selectMode():
    while True:
        try:
            mode = input("Enter what mode you want: (Pre, Flop, Turn) ")
            if mode in ["Pre", "Flop", "Turn"]:
                break
            else:
                print("Enter valid mode")
        except ValueError:
            print("Invalid input. Please enter a valid mode.")
    return mode

def everyBoard(cardList):
    #return list(combinations(cardList, 5))
    boards = []
    board = []
    for i in range(len(cardList)-4):
        for j in range(i + 1, len(cardList) - 3):
            for k in range(j + 1, len(cardList) - 2):
                for l in range(k + 1, len(cardList) - 1):
                    for m in range(l + 1, len(cardList)):
                        board = [cardList[i], cardList[j], cardList[k], cardList[l], cardList[m]]
                        boards.append(board)
    return boards

def selectFlop(cardList):
    while True:
        try:
            cardInput = input("Select flop: (Ex: Ac Ad Ah) ")
            cards = cardInput.split(" ")
            #print(cards)
            print(cards[0] in cardList and cards[1] in cardList and cards[2] in cardList)
            if cards[0] in cardList and cards[1] in cardList and cards[2] in cardList:
                cardList.remove(cards[0])
                cardList.remove(cards[1])
                cardList.remove(cards[2])
                break
            else:
                print("Please enter three valid cards")
        except ValueError:
            print("Invalid input. Please enter a valid flop.")
    return cards

def flopBoards(cardList, flop):
    boards = []
    for i in range(len(cardList) - 1):
        for j in range(i + 1, len(cardList)):
            boards.append(flop + [cardList[i], cardList[j]])
    return boards

def selectTurn(cardList):
    while True:
        try:
            cardInput = input("Select 4: (Ex: Ac Ad Ah As) ")
            cards = cardInput.split(" ")
            #print(cards)
            print(cards[0] in cardList and cards[1] in cardList and cards[2] in cardList and cards[3] in cardList)
            if cards[0] in cardList and cards[1] in cardList and cards[2] in cardList and cards[3] in cardList:
                cardList.remove(cards[0])
                cardList.remove(cards[1])
                cardList.remove(cards[2])
                cardList.remove(cards[3])
                break
            else:
                print("Please enter four valid cards")
        except ValueError:
            print("Invalid input. Please enter a valid four cards.")
    return cards

def turnBoards(cardList, turn):
    boards = []
    for i in range(len(cardList)):
        boards.append(turn + [cardList[i]])
    return boards


def main():
    countwins = {}
    countchops = {}
    board = []
    playerlist = []
    currentcards = cardList.copy()
    numPlayers = getNumPlayers()
    for i in range(numPlayers):
        countwins[str(i)] = 0
        countchops[str(i)] = 0
        playerhand = selectCards(currentcards)
        playerlist.append(playerhand)
    mode = selectMode()
    if mode == "Pre":
        boards = everyBoard(currentcards)
        combinations = len(boards)
    elif mode == "Flop":
        flop = selectFlop(currentcards)
        boards = flopBoards(currentcards, flop)
        combinations = len(boards)
    else:
        turn = selectTurn(currentcards)
        boards = turnBoards(currentcards, turn)
        combinations = len(boards)
        #print(boards)
        #2print(combinations)
    for board in boards:
        #print(board)
        winners = determineWinner(playerlist, board)
        if len(winners) == 1:
            countwins[str(winners[0])] += 1
        else:
            for chop in winners:
                countchops[str(chop)] += 1
    for i in range(numPlayers):
        print("Player", i, "odds:")
        print("To win:", countwins[str(i)] / combinations)
        print("To chop:", countchops[str(i)] / combinations)
                
if __name__ == "__main__":
    main()


