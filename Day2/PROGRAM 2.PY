n  = int(input("Enter the Number: "))
number1 = 0
number2 = 1
for i in range(n):
    if(i <= 1):
        number3 = i
    else:
        number3 = number1 + number2
        number1 = number2
        number2 = number3

    if i == n-1:
        print(number3)
    else:
        print(number3,end = ",") 