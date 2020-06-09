def removeduplicateele(A):
   newlist = []
   for n in A:
      if n not in newlist:
         newlist.append(n)
   return newlist

A=list()
n=int(input("Enter the size of the List : "))
print("Enter the number : ")
for i in range(n):
   k=int(input(""))
   A.append(int(k))
print("THE NEW LIST IS : >",removeduplicateele(A))