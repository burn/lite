
def near(self, row1, rows=None): # Return rows, sorted by dist to row1
  return sorted(rows or self.rows, key=lambda row2: self.dist(row1,row2))
  
def faraway(self, rows, sortp=False, last=None): # Get 2 distant items, maybe reusing last 
  n     = int(len(rows) * the.Far) #|\four|
  left  = last or self.near(random.choice(rows),rows)[n] #|\two| |\nine|
  right = self.near(left,rows)[n] #|\three|
  if sortp and self.d2h(label(right)) < self.d2h(label(left)): left,right = right,left
  return left, right

def half(self, rows, sortp=False, last=None): # divide data by distance to 2 distant egs 
  def dist(r1,r2): return self.dist(r1, r2)
  def proj(row)  : return (dist(row,left)**2 + C**2 - dist(row,right)**2)/(2*C) #|\seven|
  left,right = self.faraway(random.choices(rows,  #|\one|
                            k=min(the.Half, len(rows))),  #|\five|
                            sortp=sortp, last=last)
  lefts,rights,C = [],[], dist(left,right)
  for n,row in enumerate(sorted(rows, key=proj)):
    (lefts if n < len(rows)/2 else rights).append(row) #|\eight|
  return lefts, rights, left
#---------------------------------
def sway(data, rows=None,stop=None,rest=None,labels=1, last=None): # Recurse to best half
    rows = rows or data.rows
    stop = stop or 2*len(rows)**the.Stop
    rest = rest or []
    if len(rows) > stop: #|\ten|
      lefts,rights,left  = data.half(rows, True, last)
      return sway(lefts, stop, rest+rights, labels+1, left)
    else:
      return rows, rest, labels, last