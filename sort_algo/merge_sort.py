num = int(input())
arr = []
for _ in range(num):
    a = int(input())
    arr.append(a)

def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    low_array = merge_sort(array[:mid])
    high_array = merge_sort(array[mid:])

    merged_array = []
    l = h = 0

    while l < len(low_array) and h < len(high_array):
        if low_array[l] < high_array[h]:
            merged_array.append(low_array[l])
            l += 1
        else:
            merged_array.append(high_array[h])
            h += 1
    merged_array += low_array[l:]
    merged_array += high_array[h:]
    return merged_array
b = merge_sort(arr)
for i in range(len(b)):
    print(b[i])