def words(sentence):
  finalDic = {}
  wordsInSentence = sentence.split()
  for word in wordsInSentence:
    if word is not None:
      if word.isdigit() == True:
        finalDic[int(word)] = wordsInSentence.count(word)
      else:
        finalDic[word] = wordsInSentence.count(word)
          	
  return finalDic