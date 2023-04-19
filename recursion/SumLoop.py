def sum_n(n):
    sum = 0
    for i in range(n, 0, -1):
        sum += i

    return sum


print(sum_n(5))
