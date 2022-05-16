
import enum
from operator import index


diller = ["Python", "Javascript", "Flutter"]


# index=0
# for i in diller:
#     print(f"{index} - {diller[index]}")
#     index+=1



#enumarate metodu

# obje = enumerate(diller)

# print(type(obje))

# print(list(obje))

# for i in enumerate(diller):
#     print(i)

for index, value in enumerate(diller, 10):
    print(f"{index}--{value}" )