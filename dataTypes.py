def data_type(haha):
  if type(haha) is str:
    return len(haha)
  elif haha is None:
    return 'no value'
  elif type(haha) is bool:
    return haha
  elif type(haha) is int:
    if haha < 100:
      return 'less than 100'
    elif haha > 100:
      return 'more than 100'
    else:
      return 'equal to 100'
  elif type(haha) is list and len(haha) < 3:
    return None
  else:
    return haha[2]