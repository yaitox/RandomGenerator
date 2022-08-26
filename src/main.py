import sys
sys.path.insert(0, 'D:\Pseudorandom-Generator\PseudorandomGenerator\src\Generators')

from generator import ProductosMedios, CuadradosMedios, MultiplicadorConstante, Lineal

if __name__ == '__main__':
    numbers = Lineal(4532, 5, 12, 77232917, 10)
    print(numbers)
