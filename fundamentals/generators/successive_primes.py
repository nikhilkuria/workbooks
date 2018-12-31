import math


def get_prime_number(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


def is_prime(number):
    """
    If number is 1, return False
    If the number 2, return True
    If the number is divisible by 2, return False
    else,
    if the number is divisible by any number <= sqrt(num), return True,
    else, false
    :param number:
    :return: boolean
    """
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        else:
            # Step by 2 to avoid even numbers
            for divisor in range(3, int(math.sqrt(number)) + 1, 2):
                if number % divisor == 0:
                    return False
            return True
    else:
        return False


prime_generator = get_prime_number(1)

for _ in range(10):
    print(next(prime_generator))
