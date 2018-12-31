import math


def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number
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


def print_successive_primes(iterations, base=10):
    prime_generator = get_primes(base)
    '''
    When you're using send to "start" a generator (that is, execute the code from the first line of the generator 
    function up to the first yield statement), you must send None. This makes sense, since by definition the generator
    hasn't gotten to the first yield statement yet, so if we sent a real value there would be nothing to "receive" it.
    Once the generator is started, we can send values
    '''
    prime_generator.send(None)
    # This is also possible
    # next(prime_generator)
    for power in range(iterations):
        '''
        Get a value from the yield statement and also send a value to the generator
        '''
        print(prime_generator.send(base ** power))


print_successive_primes(10, 5)
