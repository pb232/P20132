
import re

lekseis=[]
with open('two_cities_ascii.txt', 'r') as inp:
    y = inp.read().lower().replace(".",' ') #vgazw tin telia
    new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', y) #vgazw ta simvola
    new_str = re.sub(" +", " ", new_str) #vgazw ta dipla kena

with open('test.txt', 'a') as out:
    out.truncate(0)
    out.write(new_str)

with open('test.txt','r') as inp:
    for line in inp:
        for word in line.split():
            lekseis.append(word)

metritis = {}
for word in lekseis:
    if word in metritis:
        metritis[word] += 1
    else:
        metritis[word] = 1

toplekseis = sorted(metritis, key = metritis.get, reverse = True)
print("Οι δέκα δημοφηλέστερες λέξεις είναι:" + str(toplekseis[:10]))

diogrammatametritis = {}
for word in lekseis:
    if len(word) >= 2:
        sindiasmos = word[0] + word[1]
    if sindiasmos in diogrammatametritis:
        diogrammatametritis[sindiasmos] += 1
    else:
        diogrammatametritis[sindiasmos] = 1
topsindiasmoidio = sorted(diogrammatametritis, key = diogrammatametritis.get, reverse = True)
print("Οι τρεις πρώτοι συνδυασμοί δύο γραμμάτων είναι:" + str(topsindiasmoidio[:3]))

triagrammatametritis = {}
for word in lekseis:
    if len(word) >= 3:
        sindiasmos = word[0] + word[1] + word[2]
    if sindiasmos in triagrammatametritis:
        triagrammatametritis[sindiasmos] += 1
    else:
        triagrammatametritis[sindiasmos] = 1
topsindiasmoitria = sorted(triagrammatametritis, key = triagrammatametritis.get, reverse = True)
print("Οι τρεις πρώτοι συνδυασμοί τριών γραμμάτων είναι:" + str(topsindiasmoitria[:3]))
