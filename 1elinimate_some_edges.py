import random
with open('data/interactions_with_seq.txt') as pid:
      LPI = pid.readlines()
a = 4577
b = LPI
f = []
while len(b) > 4121:
      index = random.randint(0, a)
      c = set()
      d = set()
      e = b[index]
      del b[index]
      for item in b:
            item = item.strip('\n')
            item = item.split('\t')
            c.add(item[0])
            d.add(item[1])
      if len(c) == 2009 and len(d) == 78:
            a = a-1
            f.append(e)
      else:
            b.append(e)
with open('train/4121_positive_pair.txt', 'w') as pid:
      pid.writelines(b)
with open('test/457_positive_pair.txt', 'w') as pid:
      pid.writelines(f)

