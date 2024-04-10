"""
{\one}     Rows arrive as list of lists. Row1 defines column names. Other rows are the examples.
{\two}     Column names define the roles of each column.
{\three}   Columns are stored in \verb+self.cols+.
{\four}    Further, independent and dependent columns are also store in \verb+self.x,self.y+
{\five}    Optionally, rows can be sorted by the distance to heaven (Equation~\ref{d2h}).
{\six}     \PY{dist} is implemented using ``\testtt{dist}'' from Listing~\ref{listing:numsum}.
{\seven}   \PY{like} is implemented using ``\testtt{like}'' from Listing~\ref{listing:numsum}.
{\eight}   As per Webb et al.~\cite{yang2002comparative}'s advice,  the $m,k$ offsets handle low frequencies. 
{\nine}    \PY{like} returns log(like) for numerical methods reasons (we can use  small negative numbers rather than very tiny  floats).
"""
def names2columns(row): # |\twenty|
   return [(NUM if s[0].isupper() else SYM)(s,i) for i,s in enumerate(row)] 

class DATA: # Hold rows, summarized in column headers 
  def __init__(self): self.rows, self.x, self.y, self.klass, self.cols = [],[],[],[],None  

  def adds(self, rows, sort=False):
    [self.add(row) for row in rows]
    if sort: self.sort() # |\circled{5}|
    return self
    
  def add(self,row): # store the row; update the column summaries | \circled{6} |   
    if   self.cols:
         self.rows += [row]
         [c.add(row[c.column]) for c in self.cols if row[c.column] != "?"] # Avoid 'dont know'   
    else self.headers(names2columns(row))

  def headers(self,cols): # |\circled{3}|  
    [self._header(col, col.txt[0], col.txt[-1]) for col in cols]
    return self
    
  def _header(self, col, a, z):
    self.cols += [col]
    if a != "X": 
       if z == "!": self.klass = col
       (self.y if z in "+-!" else self.x).append(col) # |\circled{4}|   
 
  def clone(self, rows=[], sort=False): # make a similar structure with new rows
    return DATA().headers(names2columns(self.names)).adds(rows,sort)

  def sort(self): # sort rows by d2h
    self.rows = sorted(self.rows, self.d2h)
     
  def d2h(self,row): # return Y-distance to  best Y via Equation |\ref{d2h}|
    d = sum(abs(c.heaven - c.norm(row[c.column]))^the.p for c in self.y) # |\circled{6} |
    return (d/len(self.y))**(1/the.p)

  def dist(self, row1, row2): # return X-distance row1 to row2  
    d = sum(c.dist(row1[c.column],row2[c.column])**the.p for c in self.x) # |\circled{6} |
    return (d/len(self.x))**(1/the.p)

  def like(self,row,nall,nh,m=1,k=2): # return log likelihood of row is in self  |\circled{8}| 
    prior = (len(self.rows) + k) / (nall + k*nh)
    tmp   = [col.like(row[col.colulmn], m, prior)  for col in self.x] |\circled{7} |
    return sum(math.log(x) for x in tmp + [prior]) |\circled{9}|
