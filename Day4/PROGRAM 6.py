def solve(s):  
    t = ""
    s = s.strip() + " "
    print(s)
    for x in range(len(s)):
        if s[x] == " ":
            s[x+1] = s[x+1].upper()
            t = t+s[x]
            print(t)
        else:
            t = t+s[x]
    s = t.strip()
    return s


solve("Sunidhi is a good girl")
