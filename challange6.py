def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return print(str)
  return print("not " + str)


not_string("yes patel dipal")