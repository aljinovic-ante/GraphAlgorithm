# 3. Napisati funkciju koja u stringu nalazi koliko ima susjednih samoglasnika.
string = "BARCELONA je u El Clasicu, koji se igrao u sklopu 11. kola La Lige, deklasirala Real Madrid 4:0 na stadionu Santiago Bernabeu. Ovom pobjedom je momčad Hansija Flicka pobjegla sastavu Carla Ancelottija na šest bodova prednosti na vrhu tablice španjolskog prvenstva.Sva četiri pogotka Barcelona je postigla u drugom poluvremenu. Prvo je nogometaše Reala s dva brza gola šokirao Robert Lewandowski, da bi ih dokrajčili Lamine Yamal, koji je postao najmlađi strijelac u povijesti El Clasica, i Raphinha. Luka Modrić je za Real igrao od 63. minute."
susjedi=["ae", "ea", "ei", "ie", "io", "oi", "ou", "uo"]
rijeci=string.split(" ")
# print(rijeci)
for rijec in rijeci:
    if any(par in rijec for par in susjedi):
        print(rijec)