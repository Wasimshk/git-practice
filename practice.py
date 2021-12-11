# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))

# Calculate the area of a circle

'''from math import pi

r=int(input("enter the radius of a circle: "))
print("the area of the circle with radium", r, "is:", pi*r**2)'''


# a= "hello"
# print(a[::-1])

# value = input("enter some numbers: ")
# list1 = value.split(",")
# tuple1=tuple(list1)
# print(tuple1)


# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print ("The name of the file is : " + repr(f_extns[0]))

'''color_list = ["Red","Green","White" ,"Black"]
print( color_list[0],color_list[-1])

exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)'''

# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)

# import calendar
# y = int(input("enter the year: "))
# m = int(input("enter the month: "))
# print(calendar.month(y,m))

# Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
'''def sum_thrice(x, y, z):

     sum = x + y + z
  
     if x == y == z:
      sum = sum * 3
     return sum

print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))'''


'''num = int(input("enter the number: "))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")
'''

# Write a Python program to count the number 4 in a given list.

'''def the_number(x):
    count=0
    for num in x:
        if num==4:
            count=count+1
    return count
print(the_number([4,6,4,6,4,6,8,4,86,4]))'''


# Write a Python program to test whether a passed letter is a vowel or not.
'''def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))'''



'''numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for x in numbers:
    if x == 237:
        break    
    elif x % 2 == 0:
        print(x)'''


# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

'''color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))'''


# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

'''def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum

print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))'''


# Write a Python program to add two objects if both objects are an integer type.

'''def add_numbers(a, b):
   if not(type(a)==int and type(b)==int):
       return "Inputs must be integers!"
   return a + b
print(add_numbers(10, 20))
print(add_numbers(10, 20.23))
print(add_numbers('5', 6))
print(add_numbers('5', '6'))'''
    


'''dict1 = { "name": "wasim", "age": 25}

print(dict1.get( "age")) 

def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()  '''

# def square(a,b):
#     return (a*a) + (2*a*b) + (b*b)
# print(square(4,2))

# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

'''import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)

dist= ((p1[0]-p2[0])**2+(p1[1]+p2[1])**2)**(1/2)

print(dist)
'''
    
# import os.path
# print(os.path.isfile('tempcoderunnerfile.py'))
# print(os.path.isfile('main.py'))

# import multiprocessing
# print(multiprocessing.cpu_count())


# Write a Python program to parse a string to Float or Integer.

'''a = "6545640.54"
print(int(float(a)))'''

#  Print without newline or space
'''for i in range(0, 10):
    print('*', end="")
print("\n")'''

# import getpass
# print(getpass.getuser())

# Write a Python program to sum of the first n positive integers.

# num = int(input("enter the sumber: "))
# sum=num*(num+1)/2
# print(int(sum))

# Write a Python program to convert seconds to day, hour, minutes and seconds.

# time = float(input("Input time in seconds: "))
# day = time // (24 * 3600)
# time = time % (24 * 3600)
# hour = time // 3600
# time %= 3600
# minutes = time // 60
# time %= 60
# seconds = time
# print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))


# Write a Python program to calculate body mass index
'''height = float(input("Input your height in meter: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))'''

# import math
# tan1=math.tan(45*math.pi/180)
# print(tan1)


# Write a Python program to calculate midpoints of a line.

'''print('\nCalculate the midpoint of a line :')

x1 = float(input('The value of x (the first endpoint) '))
y1 = float(input('The value of y (the first endpoint) '))

x2 = float(input('The value of x (the first endpoint) '))
y2 = float(input('The value of y (the first endpoint) '))

x_m_point = (x1 + x2)/2
y_m_point = (y1 + y2)/2
print()
print("The midpoint of line is :")
print( "The midpoint's x value is: ",x_m_point)
print( "The midpoint's y value is: ",y_m_point)
print()'''


# list_of_colors = ['Red', 'White', 'Black']  
# colors = '-'.join(list_of_colors)
# print(""+colors)
# print()

# a = 30
# b = 40
# print("%d+%d=%d"%(a,b,a+b))

'''
a = int(input("enter a number: "))
if type(a)!=int:
    print("enter value is not a number ")   '''


# Filter the positive numbers from a list
# nums = [34, 1, 0, -23, 12, -88]
# print("Original numbers in the list: ",nums)
# new_nums = list(filter(lambda x: x >0, nums))
# print("Positive numbers in the said list: ",new_nums)   

# Empty a variable without destroying it
'''n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)())'''

# Write a Python program to convert true to 1 and false to 0.
'''x = 'true'
x = int(x == 'true')
print(x)
x = 'abcd'
x = int(x == 'true')
print(x)
'''
# find out min and max values
'''list1=[12,23,351,65,45,3,56]
def min_max(x):
    min=list1[0]
    max=list1[0]
    for i in list1:
        if i>max:
            max=i
        elif i<min:
            min=i
    return min, max
print("min and max values are: ", min_max(list1))'''



