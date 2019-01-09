N=input("i")
  words =sum(c.isalpha()for c in N)
  spaces =sum(c.isspace()for c in N)
  others =len(N)-words-spaces
  print(others)
