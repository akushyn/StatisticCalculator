import src.loadCSVFile as csv
from pandas import DataFrame
#from pandas import DataFrame

highLow = []
highClose = []
openHigh = []
openLow = []
lowClose = []
distributions = []
shortNames = ['HL', 'HC', 'OH', 'OL', 'LC']
data = []
header = []

def getDistributionList():

    global highLow, highClose, openHigh, openLow, lowClose, data, distributions
    
    # D - [0]   O - [1]   H - [2]   L - [3]   C - [4]
    data = csv.csvData
    #print(DataFrame(data))
    
    for i in range(len(data)):
        if( i == 0):
            continue
        highLow.append(float(data[i][2]) - float(data[i][3]))
        highClose.append(float(data[i][2]) - float(data[i][4]))
        openHigh.append(float(data[i][2]) - float(data[i][1]))
        openLow.append(float(data[i][1]) - float(data[i][3]))
        lowClose.append(float(data[i][4]) - float(data[i][3]))

    # append data according to shortNames posistions
    distributions = [] 
    distributions.append(highLow)
    distributions.append(highClose)
    distributions.append(openHigh)
    distributions.append(openLow)
    distributions.append(lowClose)
  
    return distributions
        
def getDistributionByShortName(name):
    global shortNames
    for i in range(len(shortNames)):    
        if (shortNames[i] == name):
            result = distributions[i]
            break
            
    return result

#distributions = getDistributionList() 

# print to test output
#print(DataFrame(getDistributionByShortName('OL')))
