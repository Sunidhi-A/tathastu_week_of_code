dict_main = {
    "Hello":150,
    "Sunidhi":52,
    "Singh":200,
}
list_copy=[]
dict_val = list(dict_main.values())
max = dict_val[-1]
list_copy.append(max)
for i in range(len(dict_val)-2,-1,-1):
    if max < dict_val[i]:
        max = dict_val[i]
dict_val.remove(max)

max_2 = dict_val[-1]
for i in range(len(dict_val)-2,-1,-1):
    if max_2 < dict_val[i]:
        max_2 = dict_val[i]
print("The second maximum value is ",max_2)