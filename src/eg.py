from about import the
import sys,random

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

  def aa(): print(1)
