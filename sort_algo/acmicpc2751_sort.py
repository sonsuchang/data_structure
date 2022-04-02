import sys
num = int(input())
array = []
for _ in range(num):
    array.append(int(sys.stdin.readline()))
for i in sorted(array):
    sys.stdout.write(str(i)+'\n')