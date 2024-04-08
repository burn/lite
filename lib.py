import ast,sys

class OBJ:  # simple struct; easy init; can present itself
  def __init__(self,**d) : self.__dict__.update(d)
  __repr__ = lambda x: x.__class__.__name__+str(x.__dict__) 

def coerce(s): # convert s to int,float,bool or string
  try: return ast.literal_eval(s)   
  except Exception: return s

def cli(d): # update, in place, d from command line
  for k,v in sorted(d.items()):
    v = str(v)
    for j,x in enumerate(sys.argv):
      if x in ["-"+k[0], "--"+k]: 
        v = "True" if v=="False" else ("False" if v=="True" else sys.argv[j+1])
        d[k] = coerce(v)
