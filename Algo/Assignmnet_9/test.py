def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        sss = power(x, n / 2)
        return sss * sss
    return x * power(x, n - 1)


print(power(2, 10))
