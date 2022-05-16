#int
#float
#string
#bool

from unittest import result


age = 31
weight = 91.7
name= 'Elif'
isStudent = True

print(type(age))
print(type(weight))
print(type(name))
print(type(isStudent))


#int to float
result = float(age)
print(result)



#float to int
result = int(weight)
print(result)


#bool to str
result=str(isStudent)
print(result)


#bool to int 
result=int(isStudent)
print(result)
print(type(result))