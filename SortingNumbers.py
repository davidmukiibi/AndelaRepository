def find_max_min(numbers):
  if numbers is not None:
    newNumbers = sorted(numbers) 
    if newNumbers[0] == newNumbers[len(newNumbers)-1]:
      return len(newNumbers)
    else:  
      return [newNumbers[0], newNumbers[len(numbers)-1]]