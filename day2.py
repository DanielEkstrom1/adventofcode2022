
i = 0;
dic = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissor', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissor'}
dic2 = {'Rock' : 1, 'Paper': 2, 'Scissor': 3}
dic3 = {'X' : "Lose", 'Y': "Draw", 'Z': "Win"}
WinDic = {'Rock' : "Paper", 'Paper': "Scissor", 'Scissor': "Rock"}
LoseDic = {'Paper' : "Rock", 'Scissor': "Paper", 'Rock': "Scissor"}



def Part1():
  total = 0;
  with open('C:/Users/danie/OneDrive/Dokument/day2.txt', 'r') as f:
    for line in f.readlines():
      line = line.replace('\n', '').split(' ')
      if(dic[line[0]] == 'Rock' and dic[line[1]] == 'Rock'):
        total += dic2[dic[line[1]]] + 3
      elif (dic[line[0]] == 'Rock' and dic[line[1]] == 'Paper'):
        total += dic2[dic[line[1]]] + 6
      elif (dic[line[0]] == 'Rock' and dic[line[1]] == 'Scissor'):
        total += dic2[dic[line[1]]]
      elif (dic[line[0]] == 'Paper' and dic[line[1]] == 'Rock'):
        total += dic2[dic[line[1]]]
      elif (dic[line[0]] == 'Paper' and dic[line[1]] == 'Paper'):
        total += dic2[dic[line[1]]] + 3
      elif (dic[line[0]] == 'Paper' and dic[line[1]] == 'Scissor'):
        total += dic2[dic[line[1]]] + 6
      elif (dic[line[0]] == 'Scissor' and dic[line[1]] == 'Rock'):
        total += dic2[dic[line[1]]] + 6
      elif (dic[line[0]] == 'Scissor' and dic[line[1]] == 'Paper'):
        total += dic2[dic[line[1]]]
      elif (dic[line[0]] == 'Scissor' and dic[line[1]] == 'Scissor'):
        total += dic2[dic[line[1]]] + 3
  return total


def Part2():
  total = 0;
  with open('C:/Users/danie/OneDrive/Dokument/day2.txt', 'r') as f:
    for line in f.readlines():
      line = line.replace('\n', '').split(' ')
      if(dic3[line[1]] == "Draw"):
        total += dic2[dic[line[0]]] + 3
      if(dic3[line[1]] == "Win"):
        total += dic2[WinDic[dic[line[0]]]] + 6
      if(dic3[line[1]] == "Lose"):
        total += dic2[LoseDic[dic[line[0]]]] + 0
    return total


print(Part2())