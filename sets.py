#set tipinde indexleme yapılamaz.
#eleman değiştirilmez ama ekleme yapılır.


from string import printable
from traceback import print_tb


markalar = {"Audi", "Mercedes", "BMW", "Honda"

}


markalar2 = {"citroen", "peugeot"}
# sonuc=markalar[0] #hata verir çünkü indexleme yok.
# print(sonuc)

# sonuc = "BMW" in markalar
# print(sonuc)

# markalar.add("Opel") #sıralı olmak zorunda değil.
# print(markalar)


# markalar.update(["toyota", "Skoda"])
# print(markalar)

# sonuc2 = len(markalar)
# print(sonuc2)

# markalar.remove("Mercedes") #mercedes i siler
# print(markalar)


# markalar.pop() #rasgele bir elemanı siler
# print(markalar)


# markalar.clear() #listenin içini boşaltır
# print(markalar)

sonuc=markalar.union(markalar2) # 2 set i birleştirir.
print(sonuc)
