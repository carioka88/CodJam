def change(S):
  aux = ""
  for i in S:
    if i == '-':
      aux = aux + '+'
    else:
      aux = aux + '-'
  return aux

def flip(S):
  if len(S) == 1:
    if S[0] == '-':
      return 1
    else:
      return 0
  else:
    if S[-1] == '-':
      return 1 + flip(change(S[:-1]))
    else:
      return flip(S[:-1])


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = raw_input()  # read a list of integers, 2 in this case
  print "Case #{}: {}".format(i, flip(n))
  # check out .format's specification for more formatting options
