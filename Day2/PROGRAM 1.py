import math

number = int(input("Enter the Number: "))


print("\n1 - Odd/Even")
if number % 2 == 0 and number != 0:
    print(number," is an Even Number")
elif number % 2:
    print(number," is an Odd Number")


print("\n2 - Prime or Not?")
count=0
for i in range(1,number+1):
    if number % i == 0:
        count = count+1
if count == 2 :
    print(number," is a Prime number")
else :
    print(number," is not a Prime number")


print("\n3 - Palindrome or Not?")
number_2 = str(number) 
rev_number = ""
for i in range(len(number_2)-1,-1,-1):
   rev_number += number_2[i];
rev_number = int(rev_number)

if rev_number == number:
    print(number," is a palindrome number")
else:
    print(number," is not a palindrome number")


print("\n4 -  Armstrong or Not?")
length_user_number = len(number_2)
rem=0
sum_number =0
num=number
for i in range(length_user_number):
    rem = num % 10
    sum_number = sum_number + pow(rem,length_user_number)
    num = num // 10
if sum_number == number:
    print(number," is an Armstrong number")
else:
    print(number," is not an Armstrong number")