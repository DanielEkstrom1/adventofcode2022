import string




def  Part1(lst):
  total = 0;

  with open('txtinput\day3.txt', 'r') as f:
    for line in f:
      line = line.replace("\n", "")
      str1 = slice(0, len(line)//2)
      str2 = slice(len(line)//2, len(line))
      cache = []
      for i in range(len(line[str1])):
        p1 = i
        p2 = 0
        while(p2 < len(line[str2])):
          if(line[str1][p1] == line[str2][p2]):
            if(cache.count(line[str1][p1]) < 1):
              cache.append(line[str1][p1])
              total += lst.index(line[str1][p1]) + 1
          p2 += 1;
  return total
      

def Part2(lst):
    cache = {}
    with open('txtinput\day3.txt', 'r') as f:
      count = 0;
      total = 0;
      for line in f:
        line = set(line.replace("\n", ""))
        for i in line:
          if i not in cache.keys():
            cache[i] = 1
          else:
            cache[i] += 1
        count += 1;
        if(count % 3 == 0):
          for i in cache.keys():
            if(cache[i] == 3):
              total += lst.index(i) + 1
          cache = {}
    return total
      

lst = []
alphabetLowerCase = list(string.ascii_lowercase)
alphabetUpperCase = list(string.ascii_uppercase)

for i in alphabetLowerCase:
  lst.append(i)
for j in alphabetUpperCase:
  lst.append(j)
print(Part2(lst))