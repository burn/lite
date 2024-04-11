from about import the
from lib import csv
import sys,random,math
R=random.random

from cols import NUM,SYM
from data import DATA

def norm(mu,sd):
  return mu + sd*(math.sqrt(-2*math.log(R())) * math.cos(2*math.pi*R()))

class EG:  # store all the possible start-up functions
  def _all():  # return number of how examples that return false  
    sys.ext(sum(EG._one(s)==False for s in sorted(dir(EG)) if s[0] != "_"))

  def _one(s): # 
    global the
    old={k:v for k,v in the.__dict__.items()}
    random.seed(the.seed) 
    out = getattr(EG, s, lambda :print(f"E> '{s}' unknown."))() 
    for k,v in old.items(): the.__dict__[k]=v 
    return out

  def the(): print(the)

  def sym():
    s = SYM(init="aaaabbc")
    assert 'a' == s.mid() 
    assert 1.378 <= s.div() <= 1.379
 
  def num():
    n = NUM(init=[norm(10,2) for _ in range(1000)]) 
    assert 10 <= n.mid() <= 10.1 
    assert 1.95 <= n.div() <= 2.05 

  def csv():
    assert 3192 == sum(len(row)  for row in csv(the.file))

  def data():
    DATA().adds(csv(the.file))