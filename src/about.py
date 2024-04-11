"""
lite.py: semi-supervised multi-objective explanation
(c)2024, Tim Menzies <timm@ieee.org>, BSD-2 clause license

USAGE: python3 lite.py

OPTIONS
    -f --file     data file                           = ../../tests4mop/misc/auto93.csv
    -h --help     show help                           = False
    -p --p        in distance calcs, use Euclidean    = 2
    -s --seed     random number seed                  = 1234567891                      
    -t --todo     start up action                     = nothing

  Bayes classifier settings:                                    
    -m --m        kludge for low frequency attributes = 2
    -k --k        kludge for low frequency classes    = 1
   
  SMO settings:
    -b --best     label the n**'b' items are "best"   = 5
    -u --upper    on sorting unlabelled keep top U%   = 8
    -l --label    initially label 'l' examples        = 42
    -L --Label    label at most another 'L' examples

  SWAY settings:
    -F --Far      seeking distant egs at 'F'*max      = 9
    -S --Some     seeking distant examples, from 's'  = 256
    -M --Min      recursion stops at n^'M'            = 5

  SWAY2 settings:
    -d --dive     at first, stop at size 'd'          = 50
    -D --Deeper   next step, top at size 'D'          =  4 """

import re,lib
the = lib.settings(__doc__) 
the._help = __doc__