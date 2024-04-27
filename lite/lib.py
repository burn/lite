import re,ast,sys
from fileinput import FileInput as file_or_stdin

class OBJ:  # simple struct; easy init; can present itself
  def __init__(self,**d) : self.__dict__.update(d)
  __repr__ = lambda x: x.__class__.__name__ + show(x.__dict__) 

def show(d : dict):
   return str({k:v for k,v in d.items() if k[0] != "_"})

def settings(s : str): # parse settings from the string 's'
  out= OBJ(**{m[1]:coerce(m[2]) 
           for m in re.finditer(r"--(\w+)[^=]*=\s*(\S+)",s)})
  out.__help = sys
  return out

def coerce(s : str): # convert s to int,float,bool or string
  try: return ast.literal_eval(s)   
  except Exception: return s

def cli(d : OBJ): # update, in place, d from command line
  d = d.__dict__
  for k,v in sorted(d.items()):
    v = str(v)
    for j,x in enumerate(sys.argv):
      if x in ["-"+k[0], "--"+k]: 
        v = "True" if v=="False" else ("False" if v=="True" else sys.argv[j+1])
        d[k] = coerce(v)
  if d.get("help",False): sys.exit(d.get("_help",""))
  return d

def csv(file=None):
  with file_or_stdin(file) as src:
    for line in src:
      line = re.sub(r'([\n\t\r"\’ ]|#.*)', '', line)
      if line: yield [coerce(s.strip()) for s in line.split(",")]