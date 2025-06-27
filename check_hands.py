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