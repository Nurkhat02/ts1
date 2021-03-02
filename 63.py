#Re.start() & Re.end()
import re

s = input().strip()
k = input().strip()
ns = len(s)
nk = len(k)
matched = False
for i in range(0, ns-nk+1):
  m = re.match(r"%s" %k, s[i:])
  if m:
    print((m.start()+i, m.end()+i-1))
    matched = True
if not matched:
  print((-1,-1))