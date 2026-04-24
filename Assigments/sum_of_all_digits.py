def calculate_sum_of_digits(num):
    sum = 0

    while num > 0:
        temp = num % 10
        sum = sum + temp
        num = int(num / 10)

    return sum


