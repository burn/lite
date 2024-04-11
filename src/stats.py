import math

def entropy(d):
  N = sum(d.values())
  return - sum( n/N * math.log(n/N,2) for n in d.values() if n>0)