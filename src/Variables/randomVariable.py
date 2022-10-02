import math
from matplotlib import pyplot as plt

def CalcExp(x):
    return math.e ** x

def DistributionF(firstChi2, secondChi2):
    randomVariables = []
    
    length = len(firstChi2)
    
    for i in range(0, length):
        randomVariable = firstChi2[i] / secondChi2[i]
        randomVariables.append(randomVariable)
        
    return randomVariables
    
def DistributionExponential(normalDist):
    randomVariables = []
    
    length = len(normalDist)
    
    for i in range(0, length):
        if normalDist[i] <= 0:
            continue
        
        randomVariable = -math.log10(normalDist[i]) / 100
        randomVariables.append(randomVariable)
        
    return randomVariables
    
def DistributionGamma(alfa, betta, firstRandomNumbers, secondRandomNumbers, totalVariables):
    a = 1 / math.sqrt(2 * alfa - 1)
    b = alfa - math.log10(4)
    q = alfa + (1 / alfa)
    tetta = 4.5
    d = 1 + math.log10(tetta)
    
    length = min(len(firstRandomNumbers), len(secondRandomNumbers))
    
    randomVariables = []
    for i in range(0, length):
        if len(randomVariables) == totalVariables:
            break
        
        z_i = (firstRandomNumbers[i] ** 2) * secondRandomNumbers[i]
        v_i = a * math.log10(firstRandomNumbers[i] / (1 - secondRandomNumbers[i]))
        y_i = alfa * CalcExp(v_i)
        w_i = b + (q * v_i) - y_i
        
        randomVariable = 0
        
        if w_i + d - tetta * z_i > 0 or w_i >= math.log10(z_i):
            randomVariable = betta * y_i
            
        if randomVariable:
            randomVariables.append(randomVariable)

    return randomVariables

def DrawGraph(data):
    plt.hist(data, 80)
    plt.show()
    
