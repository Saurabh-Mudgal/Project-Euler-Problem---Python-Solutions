i = 0
num = 2
prime = []

while i < 10001:
    j = 2
    for j in range(2, num):
        if (num%j) == 0:
            break
    else:
        prime.append(num)
        i = i+1
    num = num+1

print(prime[(i-1)])
