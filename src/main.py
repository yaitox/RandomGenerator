import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

import sys
sys.path.insert(0, 'D:\Pseudorandom-Generator\PseudorandomGenerator\src\Variables')
sys.path.insert(0, 'D:\Pseudorandom-Generator\PseudorandomGenerator\src\Generators')

from generator import CuadradosMedios, ProductosMedios, VisualBase, MultiplicadorConstante
from randomVariable import DistributionF, DistributionGamma, DistributionExponential

def InitRoot():
    root = tk.Tk()
    root.title("Prueba lab")
    root.geometry("900x700")
    
    return root

def GeneratorMenuChange(generator):
    if generator == "Visual Base" or generator == "Cuadrados Medios":
        labelSeed2.place(width = 0, height = 0)
        seed2Input.place(width = 0, height = 0)
    else:
        labelSeed2.place(x = 200, y = 80, width = 167, height = 22)
        seed2Input.place(x = 200, y = 100, width = 130, height = 20)
        
        labelSeed2['text'] = 'Introducir valor cte de semilla' if generator == "Multiplicador Constante" else 'Introducir el valor de la semilla'

root = InitRoot()

# Canvas
fig = Figure(figsize = (5,5), dpi = 100)
canvas = FigureCanvasTkAgg(fig, master = root)

#Desplegable de algoritmos generadores
label = tk.Label(root, text = "Seleccionar algoritmo generador")
label.place(x = 30, y = 23)

generator = tk.StringVar(root)
generator.set("Visual Base")

generatorOptions = ["Visual Base", "Cuadrados Medios", "Productos Medios", "Multiplicador Constante"]
generatorMenu = tk.OptionMenu(root, generator, *generatorOptions, command = GeneratorMenuChange)
generatorMenu.config(width = 30)
generatorMenu.place(x = 30, y = 40)

# Distributions
label = tk.Label(root, text = "Seleccionar distribución")
label.place(x = 500, y = 23)

distribution = tk.StringVar(root)
distribution.set("Normal")
distributionOptions = ["Normal", "Log Normal", "Chi Cuadrado", "F", "Exponencial", "Gamma"]
distributionMenu = tk.OptionMenu(root, distribution, *distributionOptions)
distributionMenu.config(width = 20)
distributionMenu.place(x = 500, y = 40)

# Seeds
label = tk.Label(root, text = "Introducir el valor de la semilla")
label.place(x = 30, y = 80)
seed = tk.IntVar()
seedInput = tk.Entry(root, textvariable = seed)
seedInput.place(x = 30, y = 100)

labelSeed2 = tk.Label(root, text = "Introducir el valor de la semilla")
seed2 = tk.IntVar()
seed2Input = tk.Entry(root, textvariable = seed2)

# Random variables
label=tk.Label(root, text = "Introducir el número de variables")
label.place(x = 500, y = 70)
totalRandomVariables = tk.IntVar()
totalRandomVariables.set(20)
totalRandomVariablesInput = tk.Entry(root, textvariable = totalRandomVariables)
totalRandomVariablesInput.place(x=500,y=90)

# Valores para las distribuciones

# Generar r
boton_r1=tk.Button(root, text = "Generar numeros", width = 20, command = lambda: GenerateRandomNumbers(seed.get(), seed2.get(), generator.get()))
boton_r1.place(x = 30, y = 180)

randomNumbers = []
def GenerateRandomNumbers(seed, seed2, generator):
    if len(randomNumbers) == 2:
        randomNumbers.clear()
    
    if generator == 'Productos Medios':
        randomNumbers.append(ProductosMedios(seed, seed2, len(str(seed)), 1000000))
    
    elif generator == 'Multiplicador Constante':
        randomNumbers.append(MultiplicadorConstante(seed, seed2, len(str(seed)), 1000000))
        
    elif generator == 'Visual Base':
        randomNumbers.append(VisualBase(seed, 1000000))
        
    elif generator == 'Cuadrados Medios':
        randomNumbers.append(CuadradosMedios(seed, len(str(seed)), 1000000))
        
chi2Vector = []

def DrawGraph(distribution):
    fig.clear()
    
    data = []
    if distribution == 'Normal':
        data = Normal(randomNumbers[0], randomNumbers[1], totalRandomVariables.get())
        
    elif distribution == 'Log Normal':
        normal = Normal(randomNumbers[0], randomNumbers[1], totalRandomVariables.get())
        data = LogNormal(normal, totalRandomVariables.get())
        
    elif distribution == 'Chi Cuadrado':
        data = ChiCuadrado(normalDist[0], normalDist[1], normalDist[2], totalRandomVariables.get())
        chi2Vector.append(data)
        normalDist.clear()
        
    elif distribution == 'F':
        if len(chi2Vector) != 2:
            return
        
        data = DistributionF(chi2Vector[0], chi2Vector[1])
        print(data)
        
    elif distribution == 'Exponencial':
        normal = Normal(randomNumbers[0], randomNumbers[1], totalRandomVariables.get())
        data = DistributionExponential(normal)
        
    elif distribution == 'Gamma':
        data = DistributionGamma(5, 0.3, randomNumbers[0], randomNumbers[1], totalRandomVariables.get())

        
    plot = fig.add_subplot(111)
    plot.hist(data, 100)
    canvas.draw()
    canvas.get_tk_widget().place(x = 400, y = 200)
    print('graphing...')
    
 #   plot.hist(data, 100)
 #   plot.show()
    
        
        
normalDist = []
def Normal(r1, r2, num_variables):
    zi = 0
    media = 10
    desviacion = 4
    variables = []
    
    for i in range(0, num_variables):
        if r1[i] <= 0 or r2[i] <= 0:
            continue
        try:
            zi = (math.sqrt(-2 * math.log10(r1[i]))) * math.cos(2 * math.pi * r2[i])
        except:
            print(r1[i])
            print(r2[i])
            return
        variables.append(media + (desviacion*zi))
        
    normalDist.append(variables)
    return variables

def LogNormal(normal, num_variables):
    variables=[]
    for i in range(0, num_variables):
        xiln=math.exp(normal[i])
        variables.append(xiln)

    return variables

def ChiCuadrado(x1,x2,x3, num_variables):
    variables=[]
    if num_variables > len(x1):
        tk.messagebox.showinfo('Advertencia', 'Se estan generando un numero total de variables superiores al total de variables de distribucion normal.')
        return
      
    for i in range(0,num_variables):
        chi=x1[i] ** 2 + x2[i] ** 2 + x3[i] ** 2
        variables.append(chi)

    return variables
    

   

#Boton graficar
#atipico 0 con atipicos, 1 sin atipicos

boton_graficar=tk.Button(root, text = "Graficar", width=10, command = lambda: DrawGraph(distribution.get()))
boton_graficar.place(x=30, y=360) 
        







    
    

root.mainloop()