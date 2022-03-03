"""
Given a String as input, count the number of x in the string. Use recursion. Do not use loops. Do a dry run for each test case.
Input-> "x1x2x3x"
Output-> 4
"""

def countX(st):
  len1 = len(st)
  if (len1==0):
    return 0
  chr = 0
  ch = st[0]
  if (ch=="x"):
    chr = chr + 1
  return chr + countX(st[1:])

st = "x1x2x3x"
print(countX(st))
  