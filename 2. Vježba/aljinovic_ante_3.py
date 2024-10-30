# 3. Napisati funkciju koja u stringu nalazi koliko ima susjednih samoglasnika
string = "BARCELONA je u El Clasicu, koji se igrao u sklopu 11. kola La Lige, deklasirala Real Madrid 4:0 na stadionu Santiago Bernabeu. Ovom pobjedom je momčad Hansija Flicka pobjegla sastavu Carla Ancelottija na šest bodova prednosti na vrhu tablice španjolskog prvenstva.Sva četiri pogotka Barcelona je postigla u drugom poluvremenu. Prvo je nogometaše Reala s dva brza gola šokirao Robert Lewandowski, da bi ih dokrajčili Lamine Yamal, koji je postao najmlađi strijelac u povijesti El Clasica, i Raphinha. Luka Modrić je za Real igrao od 63. minute."
samoglasnici=["a","e","i","o","u"]
parovi=[]
for i in samoglasnici:
    for j in samoglasnici:
        if(i==j):
            continue
        parovi.append(i+j)

print(parovi)
rijeci=string.split(" ")
cnt=0
for rijec in rijeci:
    if any(par in rijec for par in parovi):
        print(rijec)
        cnt+=1
print(cnt)