"first:{0},second:{0}".format(34,12)
"""
SyntaxError: invalid non-printable character U+0016
>>> "first:{0},second:{0}".format(34,12)
'first:34,second:34'
>>> "first:{1},second:{0}".format(34,12)
'first:12,second:34'
>>> "one:{m},two:{n}.format(m=45,n=90)
  File "<python-input-3>", line 1
    "one:{m},two:{n}.format(m=45,n=90)
    ^
SyntaxError: unterminated string literal (detected at line 1)
>>> "one:{m},two:{n}".format(m=45,n=90)
'one:45,two:90'
>>> "one:{n},two:{m}".format(m=45,n=90)
'one:90,two:45'
>>> 
"""

vov = ['A', 'E', 'I', 'O', 'U']
print(vov[1 : 4])