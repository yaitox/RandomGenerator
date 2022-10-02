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

def ProductosMedios(firstSeed, secondSeed, length, total):
    randomNumbers = []
    
    for i in range(0, total):
        productSeed = firstSeed * secondSeed
        
        middleNumber = GetMiddleNumber(productSeed, length)
        randomNumbers.append(CalculateRandom(middleNumber, length))
        
        firstSeed = secondSeed
        secondSeed = middleNumber
        
    return randomNumbers

def CuadradosMedios(seed, length, total):
    randomNumbers = []
    
    for i in range(0, total):    
        square = seed * seed
        
        middleNumber = GetMiddleNumber(square, length)
        if middleNumber == 0:
            return randomNumbers
        
        seed = middleNumber
        randomNumbers.append(CalculateRandom(middleNumber, length))
    
    return randomNumbers

def MultiplicadorConstante(seed, constSeed, length, total):
    randomNumbers = []
    
    for i in range(0, total):
        newSeed = constSeed * seed
        
        middleNumber = GetMiddleNumber(newSeed, length)
        randomNumbers.append(CalculateRandom(middleNumber, length))
        
        seed = middleNumber
    
    return randomNumbers

def Lineal(seed, k, g, c, total, randomNumbers = []):
    if total == 0:
        return randomNumbers
    
    if not isprime(c):
        print("Warning. C = %d is not a prime number." % c)
    
    a = 1 + 4 * k
    m = math.pow(2, g)
    newSeed = (a * seed + c) % m
    randomNumbers.append(newSeed / (m - 1))
    
    return Lineal(newSeed, k, g, c, total - 1, randomNumbers)

def CongruencialMultiplicativo(seed, k, g, total, randomNumbers = []):
    if total == 0:
        return randomNumbers
    
    if not seed & 1:
        print("Warning. Seed = %d is not an odd number." % seed)
        
    if k < 0:
        print("Warning. K = %d is not a natural number." % k)
        
    m = math.pow(2, g)
    a = 8 * k + 3 
    newSeed = (a * seed) % m
    randomNumbers.append(newSeed / (m - 1))
    
    return CongruencialMultiplicativo(newSeed, k, g, total - 1)

def Aditivo(numbers, m, randomNumbers = []):
    for i in range(0, m):
        length = len(numbers)
        seed = (numbers[length - 1] + numbers[i]) % m
        numbers.append(seed)
        randomNumbers.append(seed / (m - 1))
        
    return randomNumbers
    
def CongruencialCuadratico(seed, a, c, g, b, randomNumbers = []):
    if a & 1:
        print("Warning. A = %d is not an even number." % a)
    
    if not c & 1:
        print("Warning. C = %d is not an odd number." % c)
    
    if ((b - 1) % 4) != 1:
        print("Warning. (%d - 1) mod 4 is not equal 1." % b)
    
    m = math.pow(2, g)
    
    for i in range(0, m):
        seed = (a * (seed * seed) + b * seed + c) % m
        randomNumbers.append(seed)
    
    return randomNumbers

def VisualBase(seed, total):
    randomNumbers = []
    
    m = 2 ** 24
    
    for i in range(0, total):
        x_i = (1140671485 * (12820163 + seed)) % m
        r_i = x_i / (m - 1)
        randomNumbers.append(r_i)
        seed = x_i
    
    return randomNumbers
        
class GeneratorType(Enum):
    GENERATOR_PRODUCTOS_MEDIOS            = 1
    GENERATOR_CUADRADOS_MEDIOS            = 2
    GENERATOR_MULTIPLICADOR_CONSTANTE     = 3
    GENERATOR_LINEAL                      = 4
    GENERATOR_CONGRUENCIAL_MULTIPLICATIVO = 5
    GENERATOR_ADITIVO                     = 6
    GENERATOR_CONGRUENCIAL_CUADRATICO     = 7
    
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
