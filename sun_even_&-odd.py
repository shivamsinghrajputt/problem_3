# write a python program that accepts a word from the user and reverse it.


from asyncio import events
from lib2to3.pytree import convert


num1=(1,2,3,4,5,6,7,8,9)
even_num= 0
odd_num= 0
for i in num1:
   if i%2==0:
    even_num+=1
   else:
    odd_num+=1
print("even number: ",even_num)
print("odd number: ",odd_num)