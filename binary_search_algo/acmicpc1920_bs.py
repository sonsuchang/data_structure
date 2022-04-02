num_1 = int(input())
array_1 = list(map(int, input().split()))
num_2 = int(input())
array_2 = list(map(int, input().split()))
array_1.sort()
def binary_search(array_1, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array_1[mid] == target:
        return 1
    elif array_1[mid] > target:
        return binary_search(array_1, target, start, mid - 1)
    else:
        return binary_search(array_1, target, mid + 1, end)
for i in array_2:
    print(binary_search(array_1, i, 0, len(array_1) - 1))