import sys
sys.path.insert(0, 'D:\Pseudorandom-Generator\PseudorandomGenerator\src\Generators')

from generator import ProductosMedios, CuadradosMedios

if __name__ == '__main__':
    numbers = ProductosMedios(5735, 5735, 5)
    print(numbers)
