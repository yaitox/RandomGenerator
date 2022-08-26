import sys
sys.path.insert(0, 'D:\Pseudorandom-Generator\PseudorandomGenerator\src\Generators')

from generator import ProductosMedios

if __name__ == '__main__':
    numbers = ProductosMedios(5015, 5734, 5)
    print(numbers)
