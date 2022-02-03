import random

xartia = []
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]
kerdisep1 = 0
kerdisep2 = 0
isopalia = 0


for x in range(100):
    for i in xarti:
        for j in color:
            xartia.append([i, j])
    random.shuffle(xartia)
    player1 = []
    sum1 = 0
    while sum1 < 16:
        sum1 = 0
        player1.append(xartia.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1 = sum1 + 10
            else:
                sum1 = sum1 + card[0]
        print(sum1)
    if sum1 > 21:
        print("P2 wins!")
        kerdisep2+=1
    else:
        '''
        sxolia pollwn
        grammwn
        '''

        print("P2 joins the game")  # let me add one more player
        player2 = []
        sum2 = 0
        while sum2 < 16:
            sum2 = 0
            player2.append(xartia.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2+= 10
                else:
                    sum2+=card[0]
            print(sum2)
        if sum2 > 21:
            sum2 = 0
        if sum1 > sum2:
            print("P1 wins!")
            kerdisep1+=1
        elif sum2 > sum1:
            print("P2 wins!")
            kerdisep2+=1
        else:
            print("draw!")
            isopalia+=1
    xartia.clear()
print("Από τα 100 παιχνίδια ο πρώτος παίχτης κέρδισε "+ str(kerdisep1))
print("Από τα 100 παιχνίδια ο δεύτερος παίχτης κέρδισε "+ str(kerdisep2))
print("Από τα 100 παιχνίδια οι ισοπαλίες ήταν "+ str(isopalia))
#ksanamidenizw
kerdisep1 = 0
kerdisep2 = 0
isopalia = 0

for x in range(100):
    for i in xarti:
        for j in color:
            xartia.append([i, j])
    random.shuffle(xartia)
    indexdeka = 0
    for j in color:
        #pairnw to pio kontino deka
        if indexdeka==0:
            indexdeka = xartia.index([10, j])
        if indexdeka > xartia.index([10,j]):
            indexdeka = xartia.index([10,j])
    indexfigoura = 0
    for i in figures:
        for j in color:
            #pairnw tin pio kontini figoura
            if indexfigoura==0:
                indexfigoura = xartia.index([i,j])
            if indexfigoura > xartia.index([i,j]):
                indexfigoura = xartia.index([i,j])
    #gia na einai dikaio k na tixainei deka i figoura analoga skeftika na pairnw to pio kontino
    telikoindex = 0
    if indexfigoura > indexdeka:
        telikoindex = indexdeka
    else:
        telikoindex = indexfigoura
    player1 = []
    sum1 = 0
    if xartia[-1] == xartia[telikoindex]:
        olaokay = "true"
    else:
        olaokay = "false"
        temp = xartia[-1]
    while sum1 < 16:
        sum1 =0
        if olaokay == "false":
            #allazw thesi ta xartia
            xartia[-1] = xartia[telikoindex]
            xartia[telikoindex] = temp
            olaokay = "true"
        player1.append(xartia.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1 = sum1 + 10
            else:
                sum1 = sum1 + card[0]
        print(sum1)
    if sum1 > 21:
        print("P2 wins!")
        kerdisep2+=1
    else:
        '''
        sxolia pollwn
        grammwn
        '''

        print("P2 joins the game")  # let me add one more player
        player2 = []
        sum2 = 0
        #arxizw apo to 5 row apo to telos kai vriksw xarti pou de einai figoura i 10
        i = -5
        vrethike = "false"
        while vrethike == "false":
            if xartia[i][0] in figures:
                i-=1
            elif xartia[i][0] == 10:
                i-=1
            else:
                index = i
                vrethike = "true"
                temp = xartia[i][0]
        while sum2 < 16:
            sum2 = 0
            #an to prwto xarti einai figoura i deka to antikathistw me to kanoniko arithmo pou vrika prin
            if xartia[-1][0] in figures:
                xartia[index] = xartia[-1]
                xartia[-1][0] = temp
            elif xartia[-1][0] == 10:
                xartia[index] = xartia[-1]
                xartia[-1][0] = temp
            player2.append(xartia.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2 = sum2 + 10
                else:
                    sum2 = sum2 + card[0]
            print(sum2)
        if sum2 > 21:
            sum2 = 0
        if sum1 > sum2:
            print("P1 wins!")
            kerdisep1+=1
        elif sum2 > sum1:
            print("P2 wins!")
            kerdisep2+=1
        else:
            print("draw!")
            isopalia+=1
    xartia.clear()
print("Από τα 100 παιχνίδια ο πρώτος παίχτης κέρδισε " + str(kerdisep1))
print("Από τα 100 παιχνίδια ο δεύτερος παίχτης κέρδισε " + str(kerdisep2))
print("Από τα 100 παιχνίδια οι ισοπαλίες ήταν " + str(isopalia))