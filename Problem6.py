sum1 = 0
sum2 = 0

for i in range (1, 101, 1):
  sum1 = sum1 + (i**2)
  sum2 = sum2 + i

sum2 = sum2**2

answer = sum2-sum1

print(answer)
