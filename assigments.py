# a=10
# b=20
# c=30

# a,b,c = 10,20,30



# a,b=b,a 


# a=a+5
# a+=5


# print(a,b,c,)

#tuple da işlemler




sayilar = (1,2,3,4,5,6)

# a,b,*c=sayilar #a =1, b=2 ve c = [3,4,5,6] çıktı verir.
# print(a,b,c)


a,*b,c=sayilar #1.elemanı a, sonuncu elamını c ye, ortadaki elemanları b ye atar

print(a,b,c)


