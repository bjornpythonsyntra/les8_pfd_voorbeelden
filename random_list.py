import random as rd
data = [[],[],[],[]]
#vullen van de lijst
for i in range(100):
    getal = rd.randint(10,200)
    if i%4==0:
        data[0].append(getal)
    elif i%4==1:
        data[1].append(getal)
    elif i%4==2:
        data[2].append(getal)
    else:
        data[3].append(getal)
#afdrukken van de lijst
for rij in data:
    for item in rij:
        print(item,end=" ")
   # print(sum(rij),end=" ") extra som per rij
   # print(sum(rij)/len(rij)) extra gemiddelde per rij
    print("")
