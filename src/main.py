import sys
sys.path.insert(0, 'D:\Pseudorandom-Generator\PseudorandomGenerator\src\Generators')

from generator import ProductosMedios, CuadradosMedios, MultiplicadorConstante, Lineal, GenerateRandomNumbers, GeneratorType

if __name__ == '__main__':
    numbers = GenerateRandomNumbers(GeneratorType.GENERATOR_MULTIPLICADOR_CONSTANTE)
    print(numbers)
