import numpy as np
import matplotlib.pyplot as plt
from Grabar import animarPlot

def grafica_evolucion(mejores, peores, promedios, num_iteraciones):
    fig = plt.figure()
    plt.plot(np.arange(num_iteraciones + 1), mejores, label="Mejor caso")
    plt.plot(np.arange(num_iteraciones + 1), peores, label="Peor Caso")
    plt.plot(np.arange(num_iteraciones + 1), promedios, label="Caso promedio")
    plt.legend()
    plt.title("Evolución")
    plt.xlabel("Generaciones")
    plt.ylabel("Valor del fitness")
    animarPlot(mejores, peores, promedios, num_iteraciones)
    fig.show()

def grafica_distribucion(i, p, f, a, b, x_costo, y_costo):
    fig = plt.figure()
    plt.plot(x_costo, y_costo, label='Función de Costo', color='blue')
    x = [x[2] for x in p]
    y = [x[3] for x in p]
    plt.xlim(a, b)
    plt.scatter(x[1:-1], y[1:-1], color='purple', label='Poblacion', zorder=3)
    plt.scatter(x[-1], y[-1], color='red', label='Peor Punto', zorder=3)
    plt.scatter(x[0], y[0], color='green', label='Mejor Punto', zorder=3)
    plt.legend()
    plt.title(f'Población de la generación {i} \n Función {f}')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    return fig
