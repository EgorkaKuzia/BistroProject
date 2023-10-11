def multiply(a, b):
    i = a * b
    return i
multiply(2,3)

#2

def positive_sum(arr):
    return sum(i for i in arr if i > 0)

#3

def make_negative( number ):
    return -abs(number)

#4

def solution(string):
   i = ''.join(reversed(string))
   return i 

#5

solution('hello')
