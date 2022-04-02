#메모이제이션 탑다운
dp = [0] * 100
def fibo(x):
    if x == 1 or x == 2:
        return 1
    elif dp[x] != 0:
        return dp[x]
    else:
        return fibo(x-1) + fibo(x-2)
x = int(input())
print(fibo(x))