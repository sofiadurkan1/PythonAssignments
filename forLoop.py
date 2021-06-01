# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'asal sayı değil. çarpanlar:', x, '*', int(n/x))
#             break
#     else: 
# # çarpan bulunmadan döngü biter ise
#         print(n, 'asal sayıdır')


# #While dongusu
# a =1
# b=10
# while a<b:
#     print(a)
#     a += 1

#exercise1
# x = 0 
# while x<5:
#     print("sofia")
#     x += 1
# #exercise2

# x= 0
# while x<6:
#     print(x)
#     x += 1

#exercise3  Using a while loop, print odd numbers from 1 to 99.
# x = 1
# while x<100:
#     print(x)
#     x += 2
    
#exercise 4 Print the sum of the first 10 numbers.  For example: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# x = 1
# sum = 0
# while x <11:
#     sum = sum + x
#     x += 1
# print(sum)

#exercise5 Ask the user for a number 3 times using a while loop.  Print the sum of the 3 numbers.

# x = 0
# sum = 0
# while x < 3:
#     num = int(input("Number: "))
#     sum = sum + num
#     x = x + 1
# print("Sum:", sum)

# x =0 
# favorite=input("name: ")
# while x<5:
#     print("wow")
#     x = x+1 

# x =0 
# while x<11:
#     print(x)
#     x += 1


# x = 0
# fav = input("where are you ?")
# while x<5:
#     print("Nowhere")
#     x += 1

# name = input ("what your name?")
# for i in range(5):
#     print(name)

# 
# sum = 0
# number = input("enter number: ")
# for i in range(3):
#     number = int(input("enter number: "))
#     sum = sum + number
# print(sum)
    

# num = 1
# for i in range(6):
#     print(i**2)


# mylist=[1,2,3,4,5,6,7,8,9,10]
# for i in mylist:
#     print(i)

# for i in mylist:
#     if i % 2 == 0:
#          print(i)
#     else:
#         print(f'odd number : {i}')

# list_sum = 0
# for num in mylist:
#     list_sum = list_sum + num
# print(list_sum)


# mystring = "Sofia"
# for letter in mystring:
#     print(letter)
   
# my_list = [(1,2),(3,4),(5,6),(7,8)]
# print(len(my_list))
# for item in my_list:
#     print(item)

# d= {"k1":1,"k2":2,"k3":3}
# for value in d.values():
# #     print(value)


# x =0
# while x<5:
#     print(x)
#     x+=1

# x = [1,2,3]
# for item in x:
#     pass
# print(x)

# mystring = "Sammy"
# for letter in mystring:
#     if letter == "a":
#         continue
#     print(letter)


# x = 0
# while x<5:
#     print(x)
#     x += 1

# mylist = [1,2,3]
# for num in range(10):
#     print(num)

# index_count = 0
# for letter in "abcde":
#     print(index_count,letter)
#     index_count += 1


# word = 'abcde'
# for item in enumerate(word):
#     print(item)


mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item in zip(mylist1,mylist2):
    print(item)

index_count = 0
for letter in "abcde":
    print()