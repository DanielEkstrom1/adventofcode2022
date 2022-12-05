from textwrap import wrap
import re

def Do_task(task):
  lst = []
  created = False
  with open('txtinput\day5.txt', 'r') as f:
    for line in f.readlines():
      modified = wrap(line.replace("\n", " ").replace(" ", ","), 4)
      lst, created = createLst(lst, len(modified), created)
      lst = task(line, modified, lst)
            
  return ToString(lst)

def Part1(line, modified, lst):
  for i in range(len(modified)):
        if(modified[i].startswith("[")):
          lst[i].insert(0, modified[i].replace(",", "").replace("[", "").replace("]", ""))
        elif(modified[i].startswith("move")):
          line = [int(s) - 1 for s in re.findall(r'\d+', line)]
          for i in range(line[0] + 1):
            lst[line[2]].append(lst[line[1]].pop())
  return lst


def Part2(line, modified, lst):
  for i in range(len(modified)):
    if(modified[i].startswith("[")):
      lst[i].insert(0, modified[i].replace(",", "").replace("[", "").replace("]", ""))
    elif(modified[i].startswith("move")):
      line = [int(s) - 1 for s in re.findall(r'\d+', line)]
      templst = []
      for i in range(line[0] + 1):
        templst.insert(0, lst[line[1]].pop())
      lst[line[2]].extend(templst)
  return lst


def createLst(lst, size, created):
  if(not created):
    lst = []
    for _ in range(size):
      lst.append([])
    created = True
  return lst, created

def ToString(lst):
  s = ""
  for i in lst:
    s += i.pop()
  return s
  
print(Do_task(Part1))
print(Do_task(Part2))