# index_count = 0
# word = "abcde"
# for letter in word:
#     print(word[index_count])
#     index_count += 1


# word = "abcde"
# for index, letter in enumerate(word):
#     print(index)
#     print(letter)
#     print('\n')


# mylist1 = [1,2,3]
# mylist2 = ['a','b','c']
# mylist3 = [100,200,300]
# for item in zip(mylist1,mylist2,mylist3):
#     print(item)

# mylist = [10,20,30,40,50,100]
# print(min(mylist))
# print(max(mylist))


# from random import shuffle
# mylist = [1,2,3,4,5,6,7,8,9,10]
# random_list= shuffle(mylist)
# print(mylist)


# from random import randint
# my_num=randint(0,100)
# print(my_num)
mystring = 'sofia'
mylist= []
for letter in mystring:
    mylist.append(letter)
print(mylist)

mylist = [letter for letter in mystring]
print(mylist)

mylist = [x for x in  'sofiasdream']
print(mylist)


mylist = [num**2 for num in range (0,11)]
print(mylist)

mylist = [x**2 for x in range(0,11) if x%2==0]
print(mylist)


mylist = []
for x in[2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
print(mylist)



mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)