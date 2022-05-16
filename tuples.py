import this


list1=[1,3,5,13,3]

thistuple=(1,2,"altı",False,False) 
thistuple2=(4,6,78,"elif",True)
print(type(list1))
print(type(thistuple))

print(list1[1])
print(thistuple[2])

print(thistuple.__len__())
print(list1.__len__())

list1[0]=15 #0. indexi 15 yapar
print(list1)

thistuple[1]=45 #type error verir. tuple ların değişkenleri sonradan değiştirilemez
print(thistuple)

list1.append(45) #listenin sonuna 45 ekledik
print(list1)

# thistuple.append diye bir fonksiyon yok.

print(list1.count(3)) #3 sayısının listede kaç kere geçtiğini buluruz
print(thistuple.count(False)) #tuple da kaç tane false olduğunu döner

print(thistuple+thistuple2) #iki tuple ı birleştirir.

list2=tuple([6,8,3,12]) #list2 yi tuple a dönüştürür
print(list2)
print(type(list2))








