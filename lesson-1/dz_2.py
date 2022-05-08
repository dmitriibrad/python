def number1(x):
    digit = 0

    while x != 0:
        digit += x % 10
        x //= 10

    return digit


calc = [i ** 3 for i in range(1, 1001, 2)]

result = sum(filter(lambda num: number1(num) % 7 == 0, calc))
result_with_17 = sum(filter(lambda num: number1(num + 17) % 7 == 0, calc))

print(result)
print(result_with_17)
