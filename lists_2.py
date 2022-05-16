iller =["istanbul", "ankara", "izmir", "bursa"]
sonuc=iller

sonuc = iller[2]

sonuc=iller[0:2] #başlangıç indexi dahil ama bitiş indexi dahil değil

sonuc=iller[2:] #2. indexten bitiş indexine kadar yazdırır.

sonuc=iller[:3] #ilk indexten başlar, 3. indexe kadar yazdırır ama 3. indexi yazdırmaz

sonuc=iller[-1] #son indexi yazdırır

sonuc=iller[-3:-1] #

iller[0]="Elazığ"

iller[-1]="balıkesir"

sonuc=len(iller)

sonuc=iller+["adana","antalya"]

print(sonuc)

del sonuc[0]

print(sonuc)


