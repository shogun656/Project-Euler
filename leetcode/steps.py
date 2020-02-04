# bunny hop step question


def count_ways(n):
    res = [0] * (n + 1)
    res[0] = 1
    res[1] = 1
    res[2] = 2

    for i in range(3, n + 1):
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]
    print(res[n])


if __name__ == '__main__':
    count_ways(4)
