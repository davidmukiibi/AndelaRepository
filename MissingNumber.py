def find_missing(haha, hehe):
  
  if len(haha) > 0 and len(hehe) > 0:
    
    if haha == hehe:
      return 0
      
    else:
      combinedList = set(haha).union(set(hehe))
      differenceList = set(haha).intersection(set(hehe))
      result = set(combinedList - differenceList)
      for i in result:
        return i
      
  else:
		return 0