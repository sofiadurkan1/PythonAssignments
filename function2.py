# def say_hello():
#     print("hello")
#     print("are")
#     print("you")
# say_hello()

# def say_hello(name="Sofia"):
#     print(f'Hello {name}')
# say_hello()

# def add_num(num1,num2):
#     return num1+num2
# result= add_num(10,20)
# print(result)

# def sum_numbers(num1,num2):
#     return num1+num2
# sum_numbers(10,20)

# result=sum_numbers('10','20')
# print(result)

# def check_even_list(num_list):
#     for number in num_list:
#         if number %2 == 0:
#             return True
#         else:
#             pass
#     return False
# check_even_list([1,3,5])
# check_even_list([2,4,5])

#return all the even numbers in a list

def check_even_list(num_list):
    even_numbers= []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers
result = check_even_list([1,2,3,4,5,6])
print(result)
