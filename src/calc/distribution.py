import src.data.loadCSV as csv
from pandas import DataFrame

def getDistributionList():
    highLow = []
    highClose = []
    openHigh = []
    openLow = []
    lowClose = []

    # D - [0]   O - [1]   H - [2]   L - [3]   C - [4]
    for i in range(len(csv.data)):
      highLow.append(float(csv.data[i][2]) - float(csv.data[i][3]))
      highClose.append(float(csv.data[i][2]) - float(csv.data[i][4]))
      openHigh.append(float(csv.data[i][2]) - float(csv.data[i][1]))
      openLow.append(float(csv.data[i][1]) - float(csv.data[i][3]))
      lowClose.append(float(csv.data[i][4]) - float(csv.data[i][3]))

    # append data according to shortNames posistions
    data = [] 
    data.append(highLow)
    data.append(highClose)
    data.append(openHigh)
    data.append(openLow)
    data.append(lowClose)
    
    return data    
        
def getDistributionByShortName(name):
    for i in range(len(shortNames)):    
        if (shortNames[i] == name):
            result = distributions[i]
            break
            
    return result


shortNames = ['HL', 'HC', 'OH', 'OL', 'LC']
distributions = getDistributionList() 

# print to test output
#print(DataFrame(getDistributionByShortName('OL')))
