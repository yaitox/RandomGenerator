import math

def GetMiddleNumber(seed, length):
    seedLength = len(str(seed))
    
    # Right elimination
    seed = str(seed)[0:seedLength - 1]
    seedLength = len(str(seed))
    if seedLength == length:
        return int(seed)
    
    # Left elimination
    seed = str(seed)[1: seedLength]
    seedLength = len(str(seed))
    if seedLength == length:
        return int(seed)
    
    return GetMiddleNumber(seed, length)

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

def CuadradosMedios(seed, total, randomNumbers = [], calls = 0, length = 0):
    if total == 0:
        return randomNumbers
    
    if calls == 0:
        length = len(str(seed))
        
    square = seed * seed
    
    middleNumber = GetMiddleNumber(square, length)
    randomNumbers.append(CalculateRandom(middleNumber, length))
    
    return CuadradosMedios(middleNumber, total - 1, randomNumbers, calls + 1, length)
