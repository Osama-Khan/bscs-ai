#Write a Python function which should take two arguments (string and a list) and return yes/no based on following condition. 
#return YES if the type of all elements of list matches the given type of first argument (str for string, number for numbers and list for lists) otherwise return NO.

def typeOf(t, data):
  for i in range(1, len(data)):
    if (type(data[i]) != type(data[0])):
      return "NO"
  if t == 'str' and type(data[0]) is str: return "YES"
  elif t == 'number' and type(data[0]) is int: return "YES"
  elif t == 'list' and type(data[0]) is list: return "YES"
  return "NO"