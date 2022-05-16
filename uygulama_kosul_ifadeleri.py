#1. girilen sayının pozitif tek sayı olup olmadığını yazdır

# sayi = int(input("Sayinizi giriniz:"))

# if(sayi>0 and sayi%2==0):
#     print("sayınız pozitif çift sayı")

# elif(sayi>0 and sayi%2 != 0):
#     print("sayiniz pozitif tek sayı")

# elif(sayi<0 and sayi%2 == 0):
#     print("sayınız negatif çift sayı")

# else:
#     print("sayınız negatif tek sayı")


#2. girilen 3 sayının karşılaştırmasını yap ve büyük olanı yazdır 

# x = int(input("x i giriniz"))
# y = int(input("y yi giriniz"))
# z = int(input("z yi giriniz"))

# if(x>y and x>z):
#     print("x en büyük sayıdır.")
# elif(y>x and y>z):
#     print("y en büyük sayıdır.")
# else:
#     print("z en büyük sayıdır.")

#3. Kullanıcının isim yaş ve eğitim durumunu al ve ehliyet almaya hak kazanıp kazanmadığını belirle

isim = input("isminizi giriniz.")
yas = int(input("Yasınızı giriniz."))
egitim = input("eğitim durumu")

if(yas > 18):
    if(egitim=="lise" or egitim== "üniversite"):
        print(f'{isim}ehliyet alabilirsiniz.')
    else:
        print(f'{isim} ehliyet alamazsınız çünkü yaşınız tutmuyor.')
else:
    print(f'{isim} ehliyet alamazsınız eğitim durumunuz tutmuyor.')
