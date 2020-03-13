f = open('input.txt', 'r')
o = open('input.txt', 'r+')
for line in f:
  r = ''.join(reversed(line))
  w = r.split()
  w.reverse()

  for x in w:
    o.writelines(x)
    o.write(' ')
  o.writelines('\n')
o.close
f.close
