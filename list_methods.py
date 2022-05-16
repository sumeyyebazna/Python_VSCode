sayilar=[100,3,9,14,280,36,36]

harfler = ["z","a","f","k","s","v","s"]

sonuc=min(sayilar)
print(sonuc)

sonuc2=max(sayilar)
print(sonuc2)

sonuc3=min(harfler)
print(sonuc3)

sonuc4=max(harfler)
print(sonuc4)

sayilar.append(20) #listenin sonuna 20yi ekler.
print(sayilar)


harfler.append("r") #listenin sonuna r harfini ekler
print(harfler)

sayilar.insert(3,12)#3. indexe 12 yi ekler
print(sayilar)

harfler.insert(5,"e") #5. indexe e harfini ekler
print(harfler)

#silme islemleri

sayilar.pop()#listenin sonundaki elemanı siler
print(sayilar)

harfler.pop()
print(harfler)

sayilar.remove(14) #listedeki 14 ü siler
print(sayilar)

harfler.remove("f") #listedeki r harfini siler
print(harfler)

#sıralama işlemleri

sayilar.sort() #sayıları küçükten büyüğe sıralar
print(sayilar)

harfler.sort() #harfleri alfabetik sıralar
print(harfler)

sayilar.reverse() #sayıları ters çevirir. 
print(sayilar)

harfler.reverse() #harfleri sondan başa sıralar.
print(harfler)

print(sayilar.count(36)) #dizide kaç tane 36 varsa o sayıyı yazar.

print(harfler.count("s")) #dizide kaç tane s harfi olduğunu bulur.

print(sayilar.index(9)) #9 un kaçıncı indexte olduğunu bulur.

print(harfler.index("a")) #a nın kaçıncı ibndexte olduğunu verir.

sayilar.clear() #listeyi boşaltır
print(sayilar) 

harfler.clear() #harfler listesini boşaltır.
print(harfler)
