jI = 1
k = 0
q = 0
jF = 0
summ = 0

while jI < 4000000:
  if (jI/2) == int(jI/2):
    summ = summ + jI
  
  q = k
  k = jI
  jF = k + q
  jI = jF

  
print("The sum of the even terms is:")
print(summ)
