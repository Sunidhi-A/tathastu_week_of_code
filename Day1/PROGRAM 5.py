a = int(input("Enter runs of PLAYER 1: "))
b = int(input("Enter runs of PLAYER 2: "))
c = int(input("Enter runs of PLAYER 3: "))

sa = (a/60)*100
sb = (b/60)*100
sc = (c/60)*100

print("\nStrike rate of PLAYER 1: ",sa)
print("Strike rate of PLAYER 2: ",sb)
print("Strike rate of PLAYER 3: ",sc)

print("\nScore after next 60 balls: ")
print("PLAYER 1: ", (a +(sa/100)*60))
print("PLAYER 2: ", (b +(sb/100)*60))
print("PLAYER 3: ", (c +(sc/100)*60))

print("\nMaximum sixes each player could have hit: ")
print("PLAYER 1: ",(a +(sa/100)*60)/6)
print("PLAYER 2: ",(b +(sb/100)*60)/6)
print("PLAYER 3: ",(c +(sc/100)*60)/6)