num = int(input())
d = [[1,0], [0,1]]
for i in range(2, num + 1):
    a = []
    a.append(d[i-1][0] + d[i-2][0])
    a.append(d[i-1][1] + d[i-2][1])
    d.append(a)
print(' '.join(str(x) for x in d[num]))