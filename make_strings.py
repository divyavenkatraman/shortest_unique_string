import string
from functools import reduce

def divmod_26(n):
  a, b = divmod(n, 26)
  if b == 0:
    return a - 1, b + 26
  return a, b

def to_str(num):
  chars = []
  while num > 0:
    num, d = divmod_26(num)
    chars.append(string.ascii_uppercase[d - 1])
  return ''.join(reversed(chars))

def from_str(chars):
  return reduce(lambda r, x: r * 26 + x + 1, map(string.ascii_uppercase.index, chars), 0)

#-----------------------ALTER THIS--------------------------------
n = 100
#-----------------------------------------------------------------
for i in range(1,n):
  print(to_str(i))
  print("\n")
