num = int(input())
food_container = list(map(int, input().split()))
dp = [0] * 100

dp[0] = food_container[0]
dp[1] = max(food_container[0], food_container[1])
for i in range(2, num):
    dp[i] = max(dp[i-1],dp[i-2] + food_container[i])
print(dp[num - 1])