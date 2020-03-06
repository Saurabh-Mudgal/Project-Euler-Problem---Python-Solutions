not_found = True
i = 2520
j = 11

while not_found:
  i = i + 1
  isDivisible = True

  for j in range(11, 21, 1):
    if i % j != 0:
      isDivisible = False
      break

  if isDivisible:
    not_found = False 

print(i)
