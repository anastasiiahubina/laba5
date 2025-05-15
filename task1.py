def fibonacci_sum(n):
    fib = [0, 1]  # Початкові значення
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return sum(fib[:n + 1])

# Зчитування числа N
N = int(input())
# Виведення суми перших N + 1 чисел Фібоначчі
print(fibonacci_sum(N))