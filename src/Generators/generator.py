import math
from sympy import isprime
from enum import Enum

def GetMiddleNumber(seed, length):
    seedLength = len(str(seed))
    if seedLength == 0:
        return 0
    
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

def ProductosMedios(firstSeed, secondSeed, length, total, randomNumbers = []):
    if total == 0:
        return randomNumbers
    
    productSeed = firstSeed * secondSeed
    
    middleNumber = GetMiddleNumber(productSeed, length)
    randomNumbers.append(CalculateRandom(middleNumber, length))
    
    return ProductosMedios(secondSeed, middleNumber, length, total - 1, randomNumbers)

def CuadradosMedios(seed, length, total, randomNumbers = []):
    if total == 0:
        return randomNumbers
        
    square = seed * seed
    
    middleNumber = GetMiddleNumber(square, length)
    randomNumbers.append(CalculateRandom(middleNumber, length))
    
    return CuadradosMedios(middleNumber, length, total - 1, randomNumbers)

def MultiplicadorConstante(constSeed, seed, length, total, randomNumbers = []):
    if total == 0:
        return randomNumbers
        
    newSeed = constSeed * seed
    
    middleNumber = GetMiddleNumber(newSeed, length)
    randomNumbers.append(CalculateRandom(middleNumber, length))
    
    return MultiplicadorConstante(constSeed, middleNumber, length, total - 1, randomNumbers)

def Lineal(seed, k, g, c, total, randomNumbers = []):
    if total == 0:
        return randomNumbers
    
    if not isprime(c):
        print("Parameter C = %d is not a prime number. Returning empty list." % c)
        return
    
    a = 1 + 4 * k
    m = math.pow(2, g)
    newSeed = (a * seed + c) % m
    randomNumbers.append(newSeed / (m - 1))
    
    return Lineal(newSeed, k, g, c, total - 1, randomNumbers)
    
class GeneratorType(Enum):
    GENERATOR_PRODUCTOS_MEDIOS        = 1
    GENERATOR_CUADRADOS_MEDIOS        = 2
    GENERATOR_MULTIPLICADOR_CONSTANTE = 3
    GENERATOR_LINEAL                  = 4
    
def GenerateRandomNumbers(generatorType):
    length = 0
    
    if generatorType == GeneratorType.GENERATOR_PRODUCTOS_MEDIOS:
        firstSeed = 0
        secondSeed = 0
        total = 0
        
        try:
            firstSeed = int(input("First seed: "))
            secondSeed = int(input("Second seed: "))
            total = int(input("Total random numbers to generate: "))
        except:
            print("An error occurred at input. Tried to convert the input to int but exception was found. Returning empty list")
        
        length = len(str(firstSeed))
        return ProductosMedios(firstSeed, secondSeed, length, total)
    
    elif generatorType == GeneratorType.GENERATOR_CUADRADOS_MEDIOS:
        seed = 0
        total = 0
        
        try:
            seed = int(input("Seed: "))
            total = int(input("Total random numbers to generate: "))
        except:
            print("An error occurred at input. Tried to convert the input to int but exception was found. Returning empty list")
            
        length = len(str(seed))
        return CuadradosMedios(seed, length, total)
    
    elif generatorType == GeneratorType.GENERATOR_MULTIPLICADOR_CONSTANTE:
        constSeed = 0
        seed = 0
        total = 0
        
        try:
            constSeed = int(input("Constant seed: "))
            seed = int(input("Seed: "))
            total = int(input("Total random numbers to generate: "))
        except:
            print("An error occurred at input. Tried to convert the input to int but exception was found. Returning empty list")

        length = len(str(seed))
        return MultiplicadorConstante(constSeed, seed, length, total)
    
    elif generatorType == GeneratorType.GENERATOR_LINEAL:
        seed = 0
        k = 0
        g = 0
        c = 0
        total = 0
        
        try:
            seed = int(input("Seed: "))
            k = int(input("K: "))
            g = int(input("G: "))
            c = int(input("C: "))
            total = int(input("Total random numbers to generate: "))
        except:
            print("An error occurred at input. Tried to convert the input to int but exception was found. Returning empty list")

        return Lineal(seed, k, g, c, total)
    
def Input():
    print("Please enter a generator type:")
    print("1 - Productos medios")
    print("2 - Cuadrados medios")
    print("3 - Multiplicador constante")
    print("4 - Lineal")
    generatorType = 0
    
    try:
        generatorType = int(input("Generator type: "))
        try:
            generatorType = GeneratorType(generatorType)
        except:
            print("Generator type not valid. Tried to enter type = %d." % generatorType)
    except:
        print("An error occurred at input. Tried to convert the input to int but exception was found.")
    
    return GenerateRandomNumbers(generatorType)
    
                
