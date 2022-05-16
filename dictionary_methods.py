from string import printable


arabaAudi ={ 
    "marka": "Audi",
    "model" : "A5",
    "yil" : 2015
}

#Değerlere erişim

# sonuc = arabaAudi.get("marka")
# print(sonuc)


#sorgulama işlemi
# sonuc = "marka" in arabaAudi
# print(sonuc)

# sonuc2="mmmmodel" in arabaAudi
# print(sonuc2)

# sonuc3=len(arabaAudi)
# print(sonuc3)

#ekleme işlemleri
# arabaAudi["renk"] = "siyah"
# print(arabaAudi)


#silme işlemleri
# arabaAudi.pop("marka")
# print(arabaAudi)

# arabaAudi.popitem()
# print(arabaAudi) #son elemanı siler

# del arabaAudi["marka"]
# print(arabaAudi)

# del arabaAudi
# print(arabaAudi) #arabaaudi objesini sildiğimiz için yazdırdığımızda sıkıntı çıkıyor 


# arabaAudi.clear() #obje değil içindeki değerleri sileriz
# print(arabaAudi)

#objeyi kopyalama
# araba = arabaAudi.copy()
# araba["marka"]="mercedes" #kopyaladığımız metodun değerini değiştirdik.

# print(araba)

#değer güncelleme

arabaAudi.update ({
    "marka" : "citroen",
"renk" : "beyaz"

})
print(arabaAudi)


