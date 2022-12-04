def Part1():
  set1 = set()
  set2 = set()
  total = 0
  with open('txtinput\day4.txt', 'r') as f:
    for line in f:
      line = line.replace("\n", "").split(",")
      first = list(map(int, line[0].split("-")))
      second = list(map(int, line[1].split("-")))
      while(first[0] != first[1] + 1):
        set1.add(first[0])
        first[0] += 1
      while(second[0] != second[1] + 1):
        set2.add(second[0])
        second[0] += 1
      if(set1.issubset(set2)):
        total += 1
      elif(set2.issubset(set1)):
        total += 1
      set1.clear()
      set2.clear()
  return total
        
        
def Part2():
  set1 = set()
  set2 = set()
  total = 0
  with open('txtinput\day4.txt', 'r') as f:
    for line in f:
      line = line.replace("\n", "").split(",")
      first = list(map(int, line[0].split("-")))
      second = list(map(int, line[1].split("-")))
      while(first[0] != first[1] + 1):
        set1.add(first[0])
        first[0] += 1
      while(second[0] != second[1] + 1):
        set2.add(second[0])
        second[0] += 1
      if(set1.isdisjoint(set2)):
        pass
      else:
        total += 1
      set1.clear()
      set2.clear()
  return total



print(Part1())
print(Part2())