def primefunction(number):
    if isinstance(number, int()):
        if number > 0:
            if number == 2 or number == 3:
                return "the given number is a prime number"
            elif number % 2 == 0 or number % 3 == 0:
                return "The given number is not a prime number"
            else:
                return "the given number is a prime number"
        else:
            return "the given number is zero or a negative number"

