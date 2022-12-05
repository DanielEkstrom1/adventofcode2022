from textwrap import wrap
import re

def Part1():
  lst = []
  created = False
  with open('txtinput\day5.txt', 'r') as f:
    for line in f.readlines():
      modifiied = wrap(line.replace("\n", " ").replace(" ", ","), 4)
      lst, created = createLst(lst, len(modifiied), created)
      for i in range(len(modifiied)):
        if(modifiied[i].startswith("[")):
          lst[i].insert(0, modifiied[i].replace(",", "").replace("[", "").replace("]", ""))
        elif(modifiied[i].startswith("move")):
          line = [int(s) - 1 for s in re.findall(r'\d+', line)]
          for i in range(line[0] + 1):
            lst[line[2]].append(lst[line[1]].pop())
  s = ""
  for i in lst:
    s += i.pop()
  return s


def Part2():
  created = False
  lst = []
  with open('txtinput\day5.txt', 'r') as f:
    for line in f.readlines():
      modifiied = wrap(line.replace("\n", " ").replace(" ", ","), 4)
      lst, created = createLst(lst, len(modifiied), created)
      for i in range(len(modifiied)):
        if(modifiied[i].startswith("[")):
          lst[i].insert(0, modifiied[i].replace(",", "").replace("[", "").replace("]", ""))
        elif(modifiied[i].startswith("move")):
          line = [int(s) - 1 for s in re.findall(r'\d+', line)]
          templst = []
          for i in range(line[0] + 1):
            templst.insert(0, lst[line[1]].pop())
          lst[line[2]].extend(templst)
  s = ""
  for i in lst:
    s += i.pop()
  return s


def createLst(lst, size, created):
  if(not created):
    lst = []
    for _ in range(size):
      lst.append([])
    created = True
  return lst, created

  
print(Part1())
print(Part2())