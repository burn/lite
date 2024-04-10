import sys
sys.dont_write_bytecode = True

from about import the
from lib   import cli
from eg    import EG

if __name__ == "__main__": 
  cli(the.__dict__)
  if the.todo in dir(EG): EG._one(the.todo)
