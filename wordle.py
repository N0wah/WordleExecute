import json

f = open('words.json')
data = json.load(f)
f.close()



alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]



meilleurMot = (data[0],1)
for i in data:
    mostUsedLetter = ["E","A","S","I","T"]
    mot = i
    score = 0
    for j in i:
        if j in mostUsedLetter:
            score+=1
            mostUsedLetter.remove(j)
    if score >= meilleurMot[1]:
        meilleurMot = (mot,score)
print(meilleurMot)