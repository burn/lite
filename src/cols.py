"""
{\one}    Rows arrive as list of lists. Row1 defines column names. Other rows are the examples.
{\two}    Column names define the roles of each column.
{\three}  Columns are stored in \verb+self.cols+.
{\four}   Further, independent and dependent columns are also store in \verb+self.x,self.y+
{\five}   Optionally, rows can be sorted by the distance to heaven (Equation~\ref{d2h}).
{\six}    \PY{dist} is implemented using ``\testtt{dist}'' from Listing~\ref{listing:numsum}.
{\seven}  \PY{like} is implemented using ``\testtt{like}'' from Listing~\ref{listing:numsum}.
{\eight}  As per Webb et al.~\cite{yang2002comparative}'s advice,  the $m,k$ offsets handle low frequencies.
{\nine}   \PY{like} returns log(like) for numerical methods reasons (we can use small negative numbers rather than very tiny floats).
"""
class SYM:  # summarizes stream of symbols
  def __init__(self,name=" ",column=0): # |\one|
    self.name, self.column, self.n, self.has = txt, column, 0, {}

  def add(self,x): # add a count for x |\eight|
    self.n += 1
    self.has[x] = 1 + self.has.get(x,0)

  def dist(self,x,y): # use Aha to get distance between two syms |\three|
    return x=="?" and y=="?" or x != y

  def like(self,x,m,prior): # return prob that x is in self  |\four|
    return (self.has.get(x, 0) + m*prior) / (self.n + m) |\seven|

class NUM: # summarizes stream of numbers
  def __init__(self, name=" ",column=0): |\on}|
   self.name, self.column, self.n = name, at, 0
   self.mu, self.m2, self.sd, self.lo, self.hi  = 0,0,0, 1E30, -1E30
   self.heaven =  0 if txt[-1] == "-" else 1 # minimize if ends with "-"  |\two| 

  def norm(self,x):  # normalizes x to 0..1 for self.lo..self.hi
    return x=="?" or (x - self.lo)/(self.hi - self.lo + 1E-30)

  def dist(self,x,y) :  # use Aha to get distance between two numerics. |\three|
    if x=="?" and y=="?": return 1
    x, y = self.norm(x), self.norm(y)
    if x=="?": x= 1 if y<0.5 else 0
    if y=="?": y= 1 if x<0.5 else 0
    return abs(x-y)

  def add(self,x):  # use x to update lo,hi, mu, and sd |\seven|
    self.n  += 1
    d        = x - self.mu
    self.mu += d / self.n
    self.m2 += d * (x -  self.mu)
    self.sd  = 0 if i.n<2 else (i.m2/(i.n-1))**0.5
    self.lo  = min(x, self.lo)
    self.hi  = max(x, self.hi)

  def like(self,x,*_): # return prob of x is in a normal pdf of self.mu and self.sd  
    nom   = math.e**(-1*(x - col.mu)**2/(2*v + 1E-30)) 
    v     = col.sd**2 
    denom = (2*math.pi*v + 1E-30)**.5 + 1E-30
    return min(1, nom/(denom))
