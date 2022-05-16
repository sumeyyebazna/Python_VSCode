# isim = "Sumeyye Bazna"

# for harf in isim:
#     if (harf=="y"):
#         break
#     print(harf)






# i = 0

# while (i < 10):
#     i+=1
#     if (i == 5):
#         continue
#     print(i)
# print("döngü bitti")


# 1 ile 100 arasındaki tek sayıları toplayalım

i = 0
toplam = 0

while (i<=100):
    i+=1
    if(i % 2 == 0):
        continue
    toplam += i

print("toplam: ", toplam)