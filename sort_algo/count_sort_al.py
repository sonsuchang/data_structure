num = int(input())
array = []
for _  in range(num):
    a = int(input())
    array.append(a)
count_array = [0] * (max(array) + 1)
for i in range(len(array)):
    count_array[array[i]] += 1
for k in range(len(count_array)):
    for j in range(count_array[k]):
        print(k)