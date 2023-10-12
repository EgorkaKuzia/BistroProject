#1

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

#2

def repeat_str(repeat, string):
    return string * repeat

repeat_str(3, 'loh')

#3

def grow(arr):
    if (arr != 0):
        result = 1
        for i in arr:
            result = result * i
            
        return result

#4

def number_to_string(num):
   return str(num)

#5

def get_grade(s1, s2, s3):
    
    sum = (s1 + s2 + s3) / 3
    
    if sum >= 90 :
        return "A"
    elif sum >= 80:
        return "B"
    elif sum >= 70:
        return "C"
    elif sum > 60:
        return "D"
    else:
        return "F"

#6

def rps(p1, p2):
    rsp = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if rsp[p1] == p2:
        return "Player 1 won!"
    if rsp[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

#7

def sum_array(a):
    if a != 0:
         return sum(x for x in a)
    else:
        return 0

#8

def better_than_average(class_points, your_points):
  if sum(class_points)/len(class_points) < your_points:
    return true
  else:
    return false

#9

def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return (l * w) * 2

#10

def string_to_number(s):
    return int(s)
