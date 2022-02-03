from urllib.request import Request, urlopen
import ssl
#kathws de mporousa na anoiksw k na kanw access to link tou opap gia na parw ta stoixeia tou kino psaxnontas sto google vrika autin tin lisi de mou doulepse kapoia alli
ssl._create_default_https_context = ssl._create_unverified_context


req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read().decode("utf-8") # kanw to data string k oxi bytes gia na mporw na to kanw edit
result  = data.find('":"') #vriskw tin arxi tou randomness
result2 = data.find('",') #vriskw to telos tou randomness

newdata = data[result+3:result2] #k kanw substring to kommati tou randomness
n = 2	# kathe 2 xaraktires
split_string = [newdata[i:i+n] for i in range(0, len(newdata), n)]
noumera = []
for i in split_string:
    noumero = int(i,base = 16)%80
    noumera.append(noumero)

data2 = urlopen('https://api.opap.gr/draws/v3.0/1100/last-result-and-active').read().decode('utf-8')
result3  = data2.find('"list') #vriskw tin arxi twn noumerwn
result4 = data2.find('],"bo') #vriskw to telos twn noumerwn
newdata2 = data2[257:result4] #k kanw substring to kommati twn noumerwn
x = newdata2.replace(',','')
split_string2= [x[i:i+n] for i in range(0, len(x), n)]
noumera2 = []
count = {}
for i in split_string2:
    noumero = int(i,base = 16)%80
    noumera2.append(noumero)
for i in range(len(noumera)):
    for j in range(len(noumera2)):
        if noumera[i] == noumera2[j]:
            count[noumera[i]] = 1
print("Αριθμοί που ταιριάζουν:" + str(len(count)))
