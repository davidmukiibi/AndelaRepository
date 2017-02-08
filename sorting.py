def find_max_min(numbersList):
  if len(numbersList) > 1:
  	centerIndex = len(numbersList) / 2 
  	smallNumbers = [] 
  	largeNumbers = []
  	for i, sortedArray in enumerate(numbersList): 
  		if i != centerIndex:
  			if sortedArray < numbersList[centerIndex]: 
  				smallNumbers.append(sortedArray)
  			else: 
  			  largeNumbers.append(sortedArray)
  	find_max_min(smallNumbers)
  	find_max_min(largeNumbers)
  	numbersList[:] = smallNumbers + [numbersList[centerIndex]] + largeNumbers
  	finalSortedArray = [numbersList[0], numbersList[len(numbersList)-1]]
  	if numbersList[0] == numbersList[len(numbersList)-1]:
  	  return [len(numbersList)]
  	else:
  	  return finalSortedArray