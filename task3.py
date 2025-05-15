def solve(points):
    points.sort()
    n = len(points)
    INF = float('inf')

    dp = [INF] * (n + 1)
    dp[0] = 0  # жодної точки — нульова довжина

    for i in range(1, n + 1):
        for j in range(i - 1, 0, -1):
            cost = abs(points[i - 1] - points[j - 1])
            dp[i] = min(dp[i], dp[j - 1] + cost)

    return dp[n]

# Ввід
n = int(input())
points = list(map(int, input().split()))
print(solve(points))