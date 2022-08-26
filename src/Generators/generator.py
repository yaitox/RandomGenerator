import math

def GetMiddleNumber(productSeed, length):
    productLength = len(str(productSeed))
    for i in range(0, length * 2 + ((productLength - length) % length) - productLength):
        productSeed = '0' + str(productSeed)
    
    return int(str(productSeed)[length // 2:length // 2 + length])

def CalculateRandom(number, length):
    return number / math.pow(10, length)

def ProductosMedios(firstSeed, secondSeed, total, randomNumbers = []):
    if total == 0:
        return randomNumbers
    
    firstSeedLength = len(str(firstSeed))
    secondSeedLength = len(str(secondSeed))
    
    if firstSeedLength != secondSeedLength:
        return
    
    productSeed = firstSeed * secondSeed
    
    middleNumber = GetMiddleNumber(productSeed, firstSeedLength)
    randomNumbers.append(CalculateRandom(middleNumber, firstSeedLength))
    
    return ProductosMedios(secondSeed, middleNumber, total - 1, randomNumbers)