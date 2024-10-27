# 4. Simulirati igru ”kamen, škare, papir”. Igrač igra protiv kompjutera. Igrač
# bira jedno od ta tri pojma i dobija bod u svakom krugu ukoliko ima jači
# alat. Pravila su:
# · kamen pobjeđuje škare
# · škare pobjeđuju papir
# · papir pobjeđuje kamen
# Koristiti containere za definiranje pravila igre.

import random

def igra():
    pravila = {
        "kamen": "škare",
        "škare": "papir",
        "papir": "kamen",
    }
    igrac_brojac=0
    kompjuter_brojac=0    
    mogucnosti=pravila.keys()
    # print(list(mogucnosti))
    while True:
        print("Trenutni rezultat: IGRAC ",igrac_brojac," - ", kompjuter_brojac," KOMPJUTER")
        igrac_izbor=input("Izaberi: kamen, škare ili papir: ")
        if(igrac_izbor not in list(mogucnosti)):
            print("Pogrešan izbor, pokušajte ponovo")
            continue
        kompjuter_izbor=random.choice(list(mogucnosti))

        if(igrac_izbor==kompjuter_izbor):
            print("Nerješeno")
        elif(pravila[igrac_izbor]==kompjuter_izbor):
            print("VAŠ IZBOR: ",igrac_izbor, " IZBOR KOMPJUTERA: ", kompjuter_izbor)
            print("Pobjedili ste!")
            igrac_brojac+=1
        else:
            kompjuter_brojac+=1

igra()