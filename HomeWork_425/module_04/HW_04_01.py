# Модуль 4/1-1
print("\nМодуль 4/1-1\n")

def tekst():
    a = '"Don\'t compare yourself with anyone in this world...\nif yoy do so, you are insulting yourself.\n\t\t\t\t\t\t\t\t\tBill Gates'
    return a

print(tekst())

# Модуль 4/1-2
print("\nМодуль 4/1-2\n")

def num(x,y):
    for i in range(x,y+1):
        if i % 2== 0:
          print(i, end=" ")

num(1,10)


# Модуль 4/1-3
print("\n\nМодуль 4/1-3\n")

def square(length, symbol, a):
    for i in range(length):
        for j in range(length):
            if not a:
                if i == 0 or j ==0 or i == length-1 or j == length -1:
                    print(symbol, end=" " )
                else:
                    print(" ", end=" ")
            else:
                print(symbol, end=" ")
        print()

square(5,"/",False)

# Модуль 4/1-4
print("\nМодуль 4/1-4\n")

def num_min(num1, num2, num3, num4, num5):
    my_list = (num1, num2, num3, num4,num5)
    num = min(my_list)
    return num

print(num_min(20,5,8,10,6))

# Модуль 4/1-5
print("\nМодуль 4/1-5\n")

def multi(a,b):
    my_list = [a, b]
    a = min(my_list)
    b = max(my_list)
    n = 1
    for i in range(a, b+1):
        n *= i
    return n

print(multi(3,6))

# Модуль 4/1-6
print("\nМодуль 4/1-6\n")

def length(num):
    num = str(num)
    n = 0
    for i in range(len(num)):
        n += 1
    return n

print(length(554213132))

'''Модуль 4/1-7'''
print("\nМодуль 4/1-7\n")

def palindrome(a):
    a = str(a)
    return a == a[::-1]

print(palindrome(12344321))
