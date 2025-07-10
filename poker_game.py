import random
from check_hands import *

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
    playerslist = []
    buyIns = {}
    while True:
        try:
            numPlayers = int(input("Enter number of players (3–10): "))
            if 3 <= numPlayers <= 10:
                break
            else:
                print("Please enter a number between 2 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    for i in range(numPlayers):
        while True:
            try:
                player = input("Enter playername: ")
                if len(player) <= 10 or player not in playerslist:
                    while True:
                        try:
                            buyin = int(input("Enter buyin for {players[i]}: "))
                            if 10 <= buyin <= 99999:
                                buyIns[player] = buyin
                                break
                            else:
                                print("Please enter a number between 2 and 10.")
                        except ValueError:
                            print("Invalid input. Please enter a valid integer.")
                    playerslist.append(player)
                    break
                elif len(player) > 10:
                    print("Please enter a name less than 11 characters.")
                else:
                    print("Please use a unique playername")
            except ValueError:
                print("Invalid input. Please enter a valid name.")
    return numPlayers, playerslist, buyIns

def getWinner(handlist):
    handranking = ["R", "SF", "Q", "FH", "F", "S", "T", "TP", "P", "H"]
    rank = "AKQJT98765432"
    tie = []
    best = None
    besthand = None
    for hand in range(len(handlist)):
        replacehigh = False
        if best == None:
            best = handranking.index(handlist[hand][0])
            besthand = handlist[hand]
            tie = [besthand]
        elif handranking.index(handlist[hand][0]) < best:
            best =  handranking.index(handlist[hand][0])
            besthand = handlist[hand]
            tie = [besthand]
        elif handranking.index(handlist[hand][0]) == best:
            if handranking[best] != "H":
                tie.append(handlist[hand])
            else:
                for i in range(len(handlist[hand][1])):
                    #print(handlist[hand][1][i][0], besthand[1][i][0], rank.find(handlist[hand][1][i][0]), rank.find(besthand[1][i][0]))
                    if rank.find(handlist[hand][1][i][0]) < rank.find(besthand[1][i][0]):
                        besthand = handlist[hand]
                        tie = [besthand]
                        replacehigh = True
                        break
                if replacehigh == False:
                    tie.append(handlist[hand])
                    #print(tie)

    #CHECK TIES
    #returns index of winning hands
    if len(tie) == 1:
        return [handlist.index(tie[0])]
    else:
        #IDEA HERE IS TO CHECK THE RANK OF EACH CARD IN EACH BEST 5 AND COMPARE TO SEE IF ITS LESS. BEST HAND IS GONNA BE THE MINIMUM
        bestlist = []
        ranklist = []
        for item in range(len(tie)):
            bestlist.append(tie[item][1])
            #testing print bestlist
        for i in range(len(bestlist)):
            ranks = ""
            for j in range(len(bestlist[i])):
                ranks += bestlist[i][j][0]
            ranklist.append(ranks)
        #print(ranklist)
        sortedrank = sorted(ranklist, key=lambda hand: [rank.index(c) for c in hand])
        if sortedrank.count(sortedrank[0]) == 1:
            #print(sortedrank, "just 1")
            return [handlist.index(tie[ranklist.index(sortedrank[0])])]
        else:
            ilist = []
            for i in range(len(ranklist)):
                if ranklist[i] == sortedrank[0]:
                    ilist.append(i)
            retlist = []
            for i in range(len(ilist)):
                #print("chop here i think", ilist)
                for j in range(len(handlist)):
                    if handlist[j] == tie[ilist[i]]:
                        if j not in retlist:
                            retlist.append(j)

                #retlist.append(handlist.index(tie[ilist[i]]))    
            return retlist

def determineWinner(playerlist, board):
    sevencard = []
    rank = "AKQJT98765432"
    best5 = []
    checker = False
    determinewinner = []
    for player in playerlist:
        best5 = []
        sevencard = player + board
        sevencard = sorted(sevencard, key=lambda card: rank.index(card[0]))
        #print("seven cards", sevencard)
        checker, best5 = checkstraightflush(sevencard[:], [])
        if checker == True:
            if best5[1][0] == "K":
                determinewinner.append(["R", best5])
                #print("Royal Flush!", best5)
            else:
                #print("Straight Flush!", best5)
                determinewinner.append(["SF", best5])
        else:
            checker, best5 = checkquads(sevencard[:], [])
            if checker == True:
                #print("Quads!", best5)
                determinewinner.append(["Q", best5])
            else:
                checker, best5 = checkfullhouse(sevencard[:], [])
                if checker == True:
                    #print("Full House", best5)
                    determinewinner.append(["FH", best5])
                else:
                    checker, best5 = checkflush(sevencard, best5)
                    if checker == True:
                        #print("Flush!", best5[:5])
                        determinewinner.append(["F", best5])
                    else:
                        checker, best5 = checkstraight(sevencard, best5)
                        if checker == True:
                            #print("Straight", best5)
                            determinewinner.append(["S", best5])
                        else:
                            checker, best5 = checktrips(sevencard, best5)
                            if checker == True:
                                #print("Trips!", best5)
                                determinewinner.append(["T", best5])
                            else:
                                checker, best5 = checktwopair(sevencard, best5)
                                if checker == True:
                                    #print("Two Pair!", best5)
                                    determinewinner.append(["TP", best5])
                                else:
                                    checker, best5 = checkpair(sevencard, best5)
                                    if checker == True:
                                        #print("Pair!", best5)
                                        determinewinner.append(["P", best5])
                                    else:
                                        best5 = sevencard[:5]
                                        #print("High Card!", best5)
                                        determinewinner.append(["H", best5])
    playerdex = getWinner(determinewinner)
    #for winner in range(len(playerdex)):
        #if len(playerdex) == 1:
            #print("Player", playerdex[winner], "Wins with", determinewinner[playerdex[winner]][1])
        #else:
            #print("Chop! Player", playerdex[winner], "chops pot with", determinewinner[playerdex[winner]][1])
    return playerdex
        
def main():
    numPlayers, playerlist, buyIns = getPlayers()
    button = 0
    sb = 1
    bb = 2
     
    for i in range(2):
        cardList = ["Ac", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc",
            "Ah", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh",
            "Ad", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd",
            "As", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks"]
        dealtcards = []
        board = []
        undealtcards = len(cardList)
        #numPlayers, namelist = getBuyin()  
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
        if bb == numPlayers - 1:
            bb = 0
            sb += 1
            button +=1
        elif sb == numPlayers - 1:
            bb += 1
            sb = 0
            button +=1
        elif bb == numPlayers - 1:
            bb += 1
            sb += 1
            button = 0
        else:
            bb += 1
            sb += 1
            button += 1


    



if __name__ == "__main__":
    main()