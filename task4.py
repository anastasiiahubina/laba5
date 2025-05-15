def max_divisible_subsequence_length(arr):
    n = len(arr)
    dp = [1] * n  # Кожен елемент сам по собі — довжина 1

    for i in range(n):
        for j in range(i):
            if arr[i] % arr[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Зчитування
n = int(input())
arr = list(map(int, input().split()))
print(max_divisible_subsequence_length(arr))