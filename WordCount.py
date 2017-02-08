def words(sentence):
  finalDic = {}
  wordsInSentence = sentence.split()
  for word in wordsInSentence:
    if word is not None:
          finalDic[word] = wordsInSentence.count(word)
  return finalDic