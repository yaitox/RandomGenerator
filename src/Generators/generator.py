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

def ProductosMedios(firstSeed, secondSeed, total, randomNumbers = [], calls = 0, length = 0):
    if total == 0:
        return randomNumbers
    
    if calls == 0:
        length = len(str(firstSeed))
    
    productSeed = firstSeed * secondSeed
    
    middleNumber = GetMiddleNumber(productSeed, length)
    randomNumbers.append(CalculateRandom(middleNumber, length))
    
    return ProductosMedios(secondSeed, middleNumber, total - 1, randomNumbers, calls + 1, length)

def CuadradosMedios(seed, total, randomNumbers = [], calls = 0, length = 0):
    if total == 0:
        return randomNumbers
    
    if calls == 0:
        length = len(str(seed))
        
    square = seed * seed
    
    middleNumber = GetMiddleNumber(square, length)
    randomNumbers.append(CalculateRandom(middleNumber, length))
    
    return CuadradosMedios(middleNumber, total - 1, randomNumbers, calls + 1, length)

def MultiplicadorConstante(constSeed, seed, total, randomNumbers = [], calls = 0, length = 0):
    if total == 0:
        return randomNumbers
    
    if calls == 0:
        length = len(str(seed))
        
    newSeed = constSeed * seed
    
    middleNumber = GetMiddleNumber(newSeed, length)
    randomNumbers.append(CalculateRandom(middleNumber, length))
    
    return MultiplicadorConstante(constSeed, middleNumber, total - 1, randomNumbers, calls + 1, length)
