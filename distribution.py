import loadCSV as csv


'''
D - [0]   O - [1]   H - [2]   L - [3]   C - [4]
'''
header = ['High-Low', 'Open-High', 'Open-Low', 'High-Close', 'Low-Close']

highLow = []
openHigh = []
openLow = []
highClose = []
lowClose = []

 
for i in range(len(csv.data)):
  highLow.append(float(csv.data[i][2]) - float(csv.data[i][3]))
  highClose.append(float(csv.data[i][2]) - float(csv.data[i][4]))
  openHigh.append(float(csv.data[i][2]) - float(csv.data[i][1]))
  openLow.append(float(csv.data[i][1]) - float(csv.data[i][3]))
  lowClose.append(float(csv.data[i][4]) - float(csv.data[i][3]))

distributions = [] 
distributions.append(highLow)
distributions.append(openHigh)
distributions.append(openLow)
distributions.append(highClose)
distributions.append(lowClose)