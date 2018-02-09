
number = 1692
check_number = [0] * 10

def check_digits(number, array):
  while number > 0:
    index = number%10
    array[index] = 1
    number = number//10

count = 1
while (0 in check_number and count < 100):
  check_digits(number*count, check_number)
  count = count + 1

if 0 in check_number:
  print "INSOMNIA"
else:
  print number*(count - 1)
