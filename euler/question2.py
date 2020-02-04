import time


def fib(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
        # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def dyn_fib(n):
    if n <= 2:
        return 0
    res = [0] * (n + 1)
    res[0] = 0
    res[1] = 0
    res[2] = 1

    for i in range(3, n + 1):
        res[i] = res[i - 2] + res[i - 1]

    return res[n]


if __name__ == "__main__":
    time1 = time.perf_counter()
    n = 1
    k = fib(n)
    sum = 0
    while k < 4000000:
        if k % 2 == 0:
            sum += k
        n += 1
        k = fib(n)
    print(sum)
    time2 = time.perf_counter()
    print(time2 - time1)

    n = 1
    k = dyn_fib(n)
    sum = 0
    while k < 4000000:
        if k % 2 == 0:
            sum += k
        n += 1
        k = dyn_fib(n)
    print(sum)
    print(time.perf_counter() - time2)

