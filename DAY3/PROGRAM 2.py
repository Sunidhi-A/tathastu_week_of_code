def p(s,i,n):
    if(i == n-1):
        print("".join(s),end=" ")
    else:
        for j in range(i,n):
            s[i],s[j] = s[j],s[i]
            p(s,i+1,n)
            s[i],s[j] = s[j],s[i]


str = input("Enter a String: ")
l=len(str)
s = list(str)
p(s,0,l)
