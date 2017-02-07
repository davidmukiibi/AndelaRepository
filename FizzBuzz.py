def fizz_buzz(haha):
  if haha%3 == 0 and haha%5 == 0:
    return 'FizzBuzz'
  elif haha%5 == 0:
    return 'Buzz'
  elif haha%3 == 0:
    return 'Fizz'
  else:
    return haha