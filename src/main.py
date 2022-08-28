# import sys
# sys.path.insert(0, 'D:\Pseudorandom-Generator\PseudorandomGenerator\src\Pruebas')

from generator import Input
from pruebas import prueba_media, prueba_varianza, prueba_uniformidad, grafica

if __name__ == '__main__':
    alfa = 0.05
    numbers = Input()

    if not prueba_media(numbers, alfa):
        print("Average test has not been passed.")
        
    elif not prueba_varianza(numbers, alfa):
        print("Variance test has not been passed.")
        
    elif not prueba_uniformidad(numbers, alfa):
        print("Uniformity test has not been passed.")
    
    else:
        print("All tests have been passed.")

    grafica(numbers) # Grafica de dispersion de los numeros pseudoaleatorios.

    print("Pseudorandom numbers obtained. Total: %d " % len(numbers))
    print(numbers)
