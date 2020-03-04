x = 2

while x < 600851475143:
  if (600851475143/x) == int(600851475143/x):
    n =2
    while (n>1) and (n<x):
      if (x/n) != int(x/n):
        n = n+1
      else:
        n = n + x
    if n == x:
      print(x)
  x = x + 1
