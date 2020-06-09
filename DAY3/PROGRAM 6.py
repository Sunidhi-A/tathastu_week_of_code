sample = []
def subset(arr, l, r, sum=0):
    
    if l > r:
        sample.append(sum)
        return

    subset(arr, l + 1, r, sum + arr[l])

    subset(arr, l + 1, r, sum)

number = int(input("Enter size of array: "))
arr = []
for i in range(0,number):
    num = int(input())
    arr.append(num)
n = len(arr)
subset(arr, 0, n - 1)
sample.remove(0) 
copy = []
for i in range(0,len(sample)):
    if sample[i] not in copy:
        copy.append(sample[i])

final_answer = []
count = 0

for i in range(0,len(copy)):
    if copy[i] not in arr:
        final_answer.append(copy[i])

for i in range(0,len(final_answer)):
    t = i
    t += 1
    if t not in final_answer:
        if t not in arr:
            print(t)
            count += 1
if count == 0:
    max = final_answer[0]
    for i in range(0,len(final_answer)):
        if max < final_answer[i]:
            max = final_answer[i]

    print(max+1)