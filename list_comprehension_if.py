
# [expresiion for item in liste if koşul]

sayilar = [1,3,7,12,22,34]

# sonuc= []

# for sayi in sayilar:
#     if (sayi %2 ==0):
#         sonuc.append(sayi)

# print(sonuc)


# sonuc2= [sayi for sayi in sayilar if sayi%2 == 0]

# print(sonuc2)


sonuc3 = [sayi if sayi%2==1 else "çift sayi" for sayi in sayilar]
print(sonuc3)