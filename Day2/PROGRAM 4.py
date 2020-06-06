x = int(input("Enter the Number"))
z=x
y=x
for i in range(x):
    print("*" * z + "  " * (i+1) + "*" *z)
    z = z - 1
for j in range(x):
    print("*" * (j+1) + "  " * y + "*" * (j+1))