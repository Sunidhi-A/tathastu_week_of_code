size = int(input("Enter the no of words you want to add in dictonary: "))
dict = []
for i in range(size):
    dict.append(input("Enter the word " + str(i + 1) + ": "))
size = int(input("Enter the no of character you want to add in array: "))
array = []
result = []
print("Enter the characters in array one by one ")
for i in range(size):
    array.append(input())
for word in dict:
    if set(word).issubset(set(array)):
        result.append(word)
print(", ".join(result) + ".")


def charCount(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict


def possible_words(lwords, charSet):
    for word in lwords:
        flag = 1
        chars = charCount(word)
        for key in chars:
            if key not in charSet:
                flag = 0
            else:
                if charSet.count(key) != chars[key]:
                    flag = 0
        if flag == 1:
            print(word)

