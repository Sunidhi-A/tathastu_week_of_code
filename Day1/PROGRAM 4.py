cp = input("Enter Cost Price: ")
sp = input("Enter Selling Price: ")
 
p = float(sp) - float(cp)

print("Profit: ", p)
 
p1 = p*0.05 + p

print("Selling price to increase the profit by 5%: ", (float(sp) + p1))