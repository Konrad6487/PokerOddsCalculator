import random

#In this file I implement a simple poker game
#plan on implementing betting rounds, and switch action from one player to another
def dealCards(numPlayers, mode, playerlist, cardList, undealtcards, dealtcards):
    for i in range(mode):
        for j in range(numPlayers):
            card = random.randint(0, undealtcards - 1)
            undealtcards -= 1
            dealtcards.append(cardList[card])
            playerlist[j].append(cardList[card])
            cardList.remove(cardList[card])
    return playerlist, cardList, undealtcards, dealtcards

def burncard(cardList, undealtcards, dealtcards):
    card = random.randint(0, undealtcards - 1)
    undealtcards -= 1
    dealtcards.append(cardList[card])
    cardList.remove(cardList[card])
    return cardList, undealtcards, dealtcards

def flop(cardList, undealtcards, board, dealtcards):
    for i in range(3):
        card = random.randint(0, undealtcards - 1)
        undealtcards -= 1
        board.append(cardList[card])
        dealtcards.append(cardList[card])
        cardList.remove(cardList[card])
    return cardList, undealtcards, board, dealtcards

def turn(cardList, undealtcards, board, dealtcards):
    card = random.randint(0, undealtcards - 1)
    undealtcards -= 1
    board.append(cardList[card])
    dealtcards.append(cardList[card])
    cardList.remove(cardList[card])
    return cardList, undealtcards, board, dealtcards
            
def getPlayers():
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
def checkroyal(sevencard, best5):
    if "Ac" in sevencard and "Kc" in sevencard and "Qc" in sevencard and "Jc" in sevencard and "Tc" in sevencard:
        best5 = ["Ac", "Kc", "Qc", "Jc", "Tc"]
        return True, best5
    elif "Ah" in sevencard and "Kh" in sevencard and "Qh" in sevencard and "Jh" in sevencard and "Th" in sevencard:
        best5 = ["Ah", "Kh", "Qh", "Jh", "Th"]
        return True, best5
    elif "Ad" in sevencard and "Kd" in sevencard and "Qd" in sevencard and "Jd" in sevencard and "Td" in sevencard:
        best5 = ["Ad", "Kd", "Qd", "Jd", "Td"]
        return True, best5
    elif "As" in sevencard and "Ks" in sevencard and "Qs" in sevencard and "Js" in sevencard and "Ts" in sevencard:
        best5 = ["As", "Ks", "Qs", "Js", "Ts"]
        return True, best5
    return False, best5
def checkstraightflush(sevencard, best5):
    checker, newbest5 = checkflush(sevencard[:], best5[:])
    if checker == True:
        newchecker, fin = checkstraight(newbest5[:], [])
        return newchecker, fin
    return False, best5
def checkquads(sevencard, best5):
    for i in range(4):
        if sevencard[i][0] == sevencard[i+1][0] and sevencard[i][0] == sevencard[i+2][0] and sevencard[i][0] == sevencard[i+3][0]:
            quads = sevencard[i:i+4]
            newsevencard = sevencard[:]
            newsevencard.remove(newsevencard[i+3])
            newsevencard.remove(newsevencard[i+2])
            newsevencard.remove(newsevencard[i+1])
            newsevencard.remove(newsevencard[i])
            best5 = quads + [newsevencard[0]]
            return True, best5
    return False, best5
def checkfullhouse(sevencard, best5):
    for i in range(5):
        if sevencard[i][0] == sevencard[i+1][0] and sevencard[i][0] == sevencard[i+2][0]:
            trips = sevencard[i:i+3]
            newsevencard = sevencard[:]
            newsevencard.remove(newsevencard[i+2])
            newsevencard.remove(newsevencard[i+1])
            newsevencard.remove(newsevencard[i])
            for j in range(0, len(newsevencard) - 2):
                if newsevencard[j][0] == newsevencard[j + 1][0]:
                    pair = newsevencard[j:j+2]
                    best5 = trips + pair
                    return True, best5
    return False, []

def checkflush(sevencard, best5):
    if sum(1 for card in sevencard if card[1] == 'c') >= 5:
        for i in range(len(sevencard)):
            if "c" in sevencard[i]:
                best5.append(sevencard[i])
                #print("flush", best5)
        return True, best5
    if sum(1 for card in sevencard if card[1] == 'h') >= 5:
        for i in range(len(sevencard)):
            if "h" in sevencard[i]:
                best5.append(sevencard[i])
                #print("flush", best5)
        return True, best5
    if sum(1 for card in sevencard if card[1] == 'd') >= 5:
        for i in range(len(sevencard)):
            if "d" in sevencard[i]:
                best5.append(sevencard[i])
                #print("flush", best5)
        return True, best5
    if sum(1 for card in sevencard if card[1] == 's') >= 5:
        for i in range(len(sevencard)):
            if "s" in sevencard[i]:
                best5.append(sevencard[i])
                #print("flush", best5)
        return True, best5
    return False, best5
    #MAKE SURE TO SLICES [:5] IN DETERMINE


def checkstraight(sevencard, best5):
    rank = "AKQJT98765432A"
    for i in range(3):
        best5 = [sevencard[i]]
        curr = sevencard[i][0]
        rankdex = rank.find(curr)
        currdex = rankdex
        j = i + 1
        while j < len(sevencard) and currdex < len(rank) - 1:
            if rank[currdex + 1] in sevencard[j]:
                currdex += 1
                best5.append(sevencard[j])
            elif currdex == 0:
                if rank[9] in sevencard[j]:
                    currdex = 9
                    best5.append(sevencard[j])
            j += 1
        if len(best5) >= 5:
            #print("straight", best5)
            return True, best5[:5]
    return False, []

def checktrips(sevencard, best5):
    for i in range(5):
        if sevencard[i][0] == sevencard[i+1][0] and sevencard[i][0] == sevencard[i+2][0]:
            trips = sevencard[i:i+3]
            newsevencard = sevencard[:]
            newsevencard.remove(sevencard[i+2])
            newsevencard.remove(sevencard[i+1])
            newsevencard.remove(sevencard[i])
            best5 = trips + newsevencard[:2]
            return True, best5
    return False, best5
            

def checktwopair(sevencard, best5):
    firstpair = []
    for i in range(0, 4):
        if sevencard[i][0] == sevencard[i + 1][0]:
            newsevencard = sevencard[:]
            firstpair = sevencard[i:i+2]
            newsevencard.remove(sevencard[i+1])
            newsevencard.remove(sevencard[i])
            if len(firstpair) == 2:
                for j in range(0, 4):
                    if newsevencard[j][0] == newsevencard[j+1][0]:
                        secondpair = newsevencard[j:j+2]
                        newsevencard.remove(newsevencard[j+1])
                        newsevencard.remove(newsevencard[j])
                        best5 = firstpair + secondpair + [newsevencard[0]]
                        return True, best5
    return False, best5

def checkpair(sevencard, best5):
    for i in range(0, 5):
        if sevencard[i][0] == sevencard[i + 1][0]:
            firstpair = sevencard[i:i+2]
            newsevencard = sevencard[:]
            newsevencard.remove(sevencard[i+1])
            newsevencard.remove(sevencard[i])
            best5 = firstpair + newsevencard[:3]
            return True, best5
    return False, best5
def determineWinner(playerlist, board):
    sevencard = []
    rank = "AKQJT98765432"
    best5 = []
    checker = False
    for player in playerlist:
        best5 = []
        sevencard = player + board
        sevencard = sorted(sevencard, key=lambda card: rank.index(card[0]))
        checker, best5 = checkstraightflush(sevencard[:], [])
        if checker == True:
            if best5[1][0] == "K":
                print("Royal Flush!", best5)
            else:
                print("Straight Flush!", best5)
        else:
            checker, best5 = checkquads(sevencard[:], [])
            if checker == True:
                print("Quads!", best5)
            else:
                checker, best5 = checkfullhouse(sevencard[:], [])
                if checker == True:
                    print("Full House", best5)
                else:
                    checker, best5 = checkflush(sevencard, best5)
                    if checker == True:
                        print("Flush!", best5[:5])
                    else:
                        checker, best5 = checkstraight(sevencard, best5)
                        if checker == True:
                            print("Straight", best5)
                        else:
                            checker, best5 = checktrips(sevencard, best5)
                            if checker == True:
                                print("Trips!", best5)
                            else:
                                checker, best5 = checktwopair(sevencard, best5)
                                if checker == True:
                                    print("Two Pair!", best5)
                                else:
                                    checker, best5 = checkpair(sevencard, best5)
                                    if checker == True:
                                        print("Pair!", best5)
                                    else:
                                        best5 = sevencard[:5]
                                        print("High Card!", best5)
        
def main():
    for i in range(10000):
        cardList = ["Ac", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc",
            "Ah", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh",
            "Ad", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd",
            "As", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks"]
        dealtcards = []
        board = []
        undealtcards = len(cardList)
        numPlayers = 10  
        playerlist = [[] for _ in range(numPlayers)]
        mode = 2
        playerlist, cardList, undealtcards, dealtcards = dealCards(numPlayers, mode, playerlist, cardList, undealtcards, dealtcards)
        #print(undealtcards)
        cardList, undealtcards, dealtcards = burncard(cardList, undealtcards, dealtcards)
        cardList, undealtcards, board, dealtcards = flop(cardList, undealtcards, board, dealtcards)
        cardList, undealtcards, dealtcards = burncard(cardList, undealtcards, dealtcards)
        cardList, undealtcards, board, dealtcards = turn(cardList, undealtcards, board, dealtcards)
        cardList, undealtcards, dealtcards = burncard(cardList, undealtcards, dealtcards)
        cardList, undealtcards, board, dealtcards = turn(cardList, undealtcards, board, dealtcards)
        #print(board)
        #print(playerlist)
        determineWinner(playerlist, board)

    



if __name__ == "__main__":
    main()