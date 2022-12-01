i = 0;
lst = [0]

with open("C:/Users/danie/OneDrive/Dokument/adventofcode.txt", 'r') as f:
  for line in f.readlines():
    if(line == "\n"):
      i += 1
      lst.append(0)
    else:
      lst[i] += int(line.replace("\n", ""))

print(max(lst))
print(sum(sorted(lst, reverse=True)[:3]))