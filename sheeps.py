def check_digits(number, array):
  while number > 0:
    index = number%10
    array[index] = 1
    number = number//10

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  number = int(raw_input())  # read a int
  check_number = [0] * 10
  count = 1
  if number != 0:
    while (0 in check_number and count < 100):
      check_digits(number*count, check_number)
      count = count + 1

  if 0 in check_number:
    print "Case #{}: {}".format(i, "INSOMNIA")
  else:
    print "Case #{}: {}".format(i, number*(count-1))

