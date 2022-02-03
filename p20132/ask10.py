import re
lekseis=[]
with open('two_cities_ascii.txt', 'r') as inp:
    y = inp.read().replace(".",' ') #vgazw tin telia
    new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', y) #vgazw ta simvola
    new_str = re.sub(" +", " ", new_str) #vgazw ta dipla kena
with open('test.txt', 'a') as out:
    out.truncate(0)
    out.write(new_str)

with open('test.txt','r') as inp:
    for line in inp:
        for word in line.split():
            lekseis.append(word)
m,a = [],[]
for i in lekseis:
    for k in range(len(i)):
        m.append(ord(i[k]))
for i in m:
    a.append((bin(i)))
omada1 = []
for i in a:
    x1 = i[2:4]
    x2 = i[5:7]
    omada1.append(x1+x2)

metritis = 0
omada2 = []
for i in omada1:
        n = int(i,base= 16)
        omada2.append(n)
print(omada1)
#ta kanw arithmous
count = 0
for i in omada2:
    if i%2 == 0:
        count +=1
print("Οι αριθμοί που είναι ζυγοί:" + str(count))
count = 0
for i in omada2:
    if i%3 == 0:
        count+=1
pososto = (count/len(omada2))*100
print("Το ποσοστό αριθμών που διαιρούνται ακριβώς με το 3 είναι:"+ str(pososto)+"%")
count = 0
for i in omada2:
    if i%5 == 0:
        count+=1
pososto = (count/len(omada2))*100
print("Το ποσοστό αριθμών που διαιρούνται ακριβώς με το 5 είναι:"+ str(pososto)+"%")
count = 0
for i in omada2:
    if i%7 ==0:
        count+=1
pososto = (count/len(omada2))*100
print("Το ποσοστό αριθμών που διαιρούνται ακριβώς με το 7 είναι:"+ str(pososto)+"%")
