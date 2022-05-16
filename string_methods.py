
from importlib.metadata import PathDistribution


yazi = "benim adım sümeyye bazna. Ankara'da yaşıyorum."

sonuc = yazi.upper() #yazılanları büyük yapar
print(sonuc)

sonuc2=yazi.lower() #yazılanları küçük yapar
print(sonuc2)

sonuc3=yazi.title() #yazılanların sadece ilk harflerini büyük yapar
print(sonuc3)

sonuc4=yazi.capitalize() #sadece ilk harfi büyük yapar
print(sonuc4)

sonuc5=yazi.islower() #yazıların hepsi küçük mü? true ya da false döner
print(sonuc5)

sonuc6=yazi.isupper() #yazıların hepsi büyük mü? true ya da false döner
print(sonuc6)

sonuc7=yazi.strip() #yazının başında yada sonunda boşlıkları siler
print(sonuc7)

sonuc8=yazi.split() #dizi oluşturur ve her kelimeyi diziye atar.(bu bölme işlemini default olarak boşluğa göre yapar.)
print(sonuc8)

sonuc9=yazi.split(".") #noktadan itibaren böler ve diziye atar.
print(sonuc9)

sonuc10="-".join(yazi) #her harfin arasına - koyar 
print(sonuc10)

sonuc11=yazi.index("bazna") # verdiğin kelime kaçıncı indexten itibaren başlıyor
print(sonuc11)

sonuc12 = yazi.startswith("b") #b ile mi başlıyor. true ya da false döner
print(sonuc12)

sonuc13=yazi.startswith("1") #1 ile mi başlıyor. true ya da false döner
print(sonuc13)

sonuc14=yazi.replace("Ankara", "Elazığ") #ankarayı elazığ ile değiştirdik
print(sonuc14)

sonuc15=yazi.replace("ı","i").replace("ü","u") #ı ları i, ü leri u yaptık
print(sonuc15)
