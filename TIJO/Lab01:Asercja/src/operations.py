def add(first, second):
    return first + second


def max(digits):

    if not digits:
        return None

    max = digits[0]
    for i in digits:
        if i > max:
            max = i

    return max


def perfect(number):
    suma = 0

    for i in range(1, number):
        if number % i == 0:
            suma += i

    return suma == number

