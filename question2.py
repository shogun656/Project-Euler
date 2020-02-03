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


if __name__ == "__main__":
    n = 1
    k = fib(n)
    sum = 0
    while k < 4000000:
        if k % 2 == 0:
            sum += k
        n += 1
        k = fib(n)
    print(sum)
