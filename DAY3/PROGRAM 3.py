strg = input("Enter a Word: ")
length = len(strg)
duplicate_string = ""
for i in range(0,length):
    if strg[i] in duplicate_string:
        continue
    else:
        duplicate_string += strg[i]
print(duplicate_string)