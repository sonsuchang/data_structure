import sys
num = int(input())
target = int(input())
array = []
for i in range(num):
    array.append(int(sys.stdin.readline()))
array.sort()
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)

result = binary_search(array, target, 0, len(array) - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)