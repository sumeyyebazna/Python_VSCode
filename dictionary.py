#34 istanbul
#35 izmir

# sehirler=["istanbul","izmir"]
# plaka=[34,35]

# print(plaka[0],sehirler[0])
# print(plaka[1],sehirler[1])

# print(sehirler.index("istanbul")) #istanbulun kaçıncı indexte olduğunu söyler

# print(plaka[sehirler.index("istanbul")]) #34 verir
# print(plaka[sehirler.index("izmir")]) #35 verir

#sözlüklerde key ve value değerleri var. bu şekilde listeler eşleştirilir.

# plakalar={"izmir":35,"istanbul":34}
# print(plakalar)

# print(plakalar["izmir"]) #izmiir in değeri olan 35 i verir

# plakalar["eskişehir"] =26 #sözlüğe eskişehir eklendi
# plakalar["bursa"]=16 #sözlüğe bursa eklendi
# print(plakalar)

urunler={
100: { "urunAdi" : "monitor",
"urun acıklaması":"16 inc",
"garanti suresi" : 3,
"fiyat":[800, 944]

},
101: { "urunAdi" : "ssd harddisk",
"urun acıklaması":"256 gb",
"garanti suresi" : 2,
"fiyat":[1500,1800]
}

}

# sonuc=urunler[100] #ürün kodu 100 olan ürünün bilgilerini getirir
# print(sonuc)

sonuc=urunler[100]["urunAdi"] #ürün kodu 100 olan ürünün ürün adını getirir.
print(sonuc)

tutar=urunler[100]["fiyat"][1]+urunler[101]["fiyat"][1] #iki tane fiyat bilgisi var biz 1. indeextekilerin toplamını istedik.
print(tutar)
