dict_main = {
    "Hello":1,
    "Sunidhi":1,
    "Singh":1,}

print(dict_main)

dict_val =list(dict_main.values())
dict_key = list(dict_main.keys())
list_copy = []
store = {}
removed_value ={}
for i in range (0, len(dict_main)):
    if dict_val[i] not in list_copy:
        list_copy.append(dict_val[i])
        store[dict_key[i]] = dict_val[i]
    else:
        removed_value[dict_key[i]] = dict_val[i]
print('\nRemoved values are : ',removed_value)
print("\n Dictionary: ",store)