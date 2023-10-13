#1

def fake_bin(x):
    if int(x) >= 5:
        return 1
    else:
        return 0

#2

def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9

#3

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump / mpg <= fuel_left:
        return True 
    else:
        return False

#4

def double_integer(i):
    return i * 2

#5

def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else: 
        return n * m

#6

def check(seq, elem):
    return elem in seq

#7

def count_sheeps(sheep):
    x = 0
    for i in sheep:
        if i == True:
            x = x + 1
    return x

#8

def find_short(s):
    x = s.split(' ')
    l = len(x[0])
    for i in x:
        if len(i) < l:
            l = len(i)
    return l
            

#9

def string_to_array(s):
    return s.split(' ')

#10

def sum_mix(arr):
    return sum(int(i) for i in arr)
