palindrome_list = [0]
var1 = 0
var2 = 0
var3 = 0

# Nested loop to carry out the multiple of every single 3 digit integer upto 1000 and store the resulting palindromes in a list
for var1 in range(100, 1000, 1):
  for var2 in range(100, 1000, 1):
    var3 = var1*var2
    if str(var3) == str(var3)[::-1] and var3 != 0:
      palindrome_list.append(var3)
    var2 = var2+1
  var1 = var1+1
  var2 = 0

# Arrange the list of palindrome in ascending order
palindrome_list.sort()

# To print the largest palindrome possible. List starts counting from 0. Hence '-1' gives the last entry in list; which, after arranging the list in ascending order, is the largest Palindrome.
print("Palindrome in question is: ", palindrome_list[-1])
