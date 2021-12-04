# finding minimum value

import random
randl = random.sample(range(1,50),7)
def rmin(x):
    min = randl[0]
    for i in randl:
        if i < min:
            min = i
    return min
print("the minimum value is: ",rmin(randl))


#finding maximum value of array

import random
randl = random.sample(range(1,50),7) 
def rmax(x):
    max=randl[0]
    for i in randl:
        if i>max:
            max=i
    return max
print("the maximum value is", rmax(randl))


#finding mean

import random
randl = random.sample(range(1,50),7) 
n=len(randl)
def rmean(x):
    sum=0
    for i in range(0, n):
        sum=sum+randl[i]
    return sum/n
print("the mean is: ",rmean(randl))


#finding median

import random
randl = random.sample(range(1,50),7) 
n=len(randl)
randl.sort()
def rmedian(x):
    if n%2==0:
        median1=randl[n//2]
        median2=randl[n//2-1]
        median=(median1+median2)/2
    else:
         median=randl[n//2]
    return median
print("the median is: ",rmedian(randl))


#finding factorial 

num1=int(input("enter the number: "))
def myfactorial(x):
    mfact=1
    for i in range(num1):
        mfact=mfact*(i+1)
    return mfact
print("the factorial of your number is:", myfactorial(num1))


# ATM operation 

print("welcome to the Bank")
Pin=int(input("Please enter the ATM PIN\n"))
if Pin==1234:
    print("please select the option")
    t=int(input("1 - Cash Withdraw\n2 - Balance Inquiry\n"))
    if t==1:
        w=int(input("Enter the amount:\n"))
        if w%100!=0:
            print("Please enter the amount multiple of 100")
        elif w>25000:
            print("insufficiant Balance")
        elif w%100==0 and w<=25000:
            print("Please collect your cash.\nThank you!")
    elif t==2:
        print("Your current balance is 25000")
    else:
        print("invalid option")
else:
    print("incorrect PIN entered")
