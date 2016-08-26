#!/usr/bin/python
"""
utest.py (c) 2016 tim@menzies.us, MIT licence

Part of http://tiny.cc/ase16: teaching tools for
(model-based) automated software enginering.

USAGE: 
(1) If you place '@ok' before a function, then
load that file, then that function will execute and
all assertion failures will add one to a FAIL
count.
(2) To get the final counts, add 'oks()' at the end
of the source code.

For more on this kind of tool, see
https://www.youtube.com/watch?v=nIonZ6-4nuU
"""
from __future__ import division,print_function
import sys,re,traceback,random,string
sys.dont_write_bytecode=True

PASS=FAIL=0
VERBOSE=True

def oks():
  global PASS, FAIL
  print("\n# PASS= %s FAIL= %s %%PASS = %s%%"  % (
          PASS, FAIL, int(round(PASS*100/(PASS+FAIL+0.001)))))

def ok(f):
  global PASS, FAIL
  try:
      print("\n-----| %s |-----------------------" % f.__name__)
      if f.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
      f()
      print("# pass")
      PASS += 1
  except Exception,e:
      FAIL += 1
      print(traceback.format_exc()) 
  return f
