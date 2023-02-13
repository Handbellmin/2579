n = (int)(input())
#각 계단 점수
ls = [0]*301
#계단 선택 시 최대값
dp = [0]*301
for i in range(n):
  ls[i] = (int)(input())
dp[0] = ls[0]
dp[1] = ls[0]+ls[1]
dp[2] = max(ls[0]+ls[2],ls[1]+ls[2])

for i in range(3,n):
  dp[i] = max(dp[i-2]+ls[i],dp[i-3]+ls[i-1]+ls[i])

print(dp[n-1])
