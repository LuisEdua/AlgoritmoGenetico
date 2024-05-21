import re
import math
import random
from CalcularFx import calcular_y_mostrar_resultado
from statistics import mean
from Graficas import grafica_distribucion, grafica_evolucion
from Grabar import grabarVideo
import numpy as npy

a = 0
b = 0
resolucion = 0
formula = ""
nb = 0
poblacion = []
mejores_casos = []
peores_casos = []
promedios = []

def calcular_limites(i):
    global a, b
    match = re.match(r'^(\[|\()(-?\d+.?\d*),\s*(-?\d+.?\d*)(\]|\))$', i)
    a = float(match.group(2))
    b = float(match.group(3))

def calcular_bits(i, rd):
    global a, b, np
    calcular_limites(i)
    rango = b-a
    np = (rango//rd) + 1
    return math.ceil(math.log2(np)), rango

def calcular_datos_individuo(genotipo, individuo):
    global a, resolucion, formula
    i = int(genotipo, 2)
    x = round(a + (i * resolucion), 4)
    fitness = round(calcular_y_mostrar_resultado(formula, x), 4)
    individuo.append(genotipo)
    individuo.append(i)
    individuo.append(x)
    individuo.append(fitness)


def generar_individuos(pi, nb):
    global poblacion
    for _ in range(pi):
        individuo = []
        genotipo= ""
        for _ in range(0, nb):
            genotipo += str(random.randint(0, 1))
        calcular_datos_individuo(genotipo, individuo)
        poblacion.append(individuo)


def inicializar(pi, i, rd):
    global resolucion, nb
    nb, rango = calcular_bits(i, rd)
    resolucion = round(rango / ((2**nb)-1), 4)
    generar_individuos(pi, nb)


def cruza(padre1, padre2):
    global nb
    npc = random.randint(1, nb)
    puntos_cruza = random.sample(range(0, nb), npc)
    puntos_cruza.sort()
    gen1 = padre1[0]
    gen2 = padre2[0]
    hijo1 = ""
    hijo2 = ""
    inicio = 0
    for punto in puntos_cruza:
        hijo1 += gen1[inicio:punto]
        hijo2 += gen2[inicio:punto]
        inicio = punto
        gen1, gen2 = gen2, gen1
    if inicio < len(gen1) or inicio < len(gen2):
        hijo1 += gen1[inicio:nb]
        hijo2 += gen2[inicio:nb]
    return hijo1, hijo2

def mutacion(genes, pmi, pmg):
    newGenes = list(genes)
    longitud = len(newGenes)
    individuo = []
    if random.randint(0, 100) < pmi*100:
        for i in range(longitud):
            if random.randint(0, 100) < pmg*100:
                numero_aleatoreo = random.randint(0, longitud - 1)
                valor_viejo = newGenes[i]
                newGenes[i] = newGenes[numero_aleatoreo]
                newGenes[numero_aleatoreo] = valor_viejo
    calcular_datos_individuo(''.join(x for x in newGenes), individuo)
    return individuo


def cruza_mutacion(pc, pmi, pmg):
    newPoblacion = []
    for individuo in poblacion:
        if random.randint(0, 100) < pc * 100:
            hijo1, hijo2 = cruza(individuo, poblacion[random.randint(0, len(poblacion) - 1)])
            newPoblacion.append(mutacion(hijo1, pmi, pmg))
            newPoblacion.append(mutacion(hijo2, pmi, pmg))
    poblacion.extend(newPoblacion)


def calcular_estadisticos():
    global mejores_casos, peores_casos, promedios
    mejores_casos.append(poblacion[0][3])
    peores_casos.append(poblacion[-1][3])
    fines_cases = [float(x[3]) for x in poblacion]
    promedios.append(round(mean(fines_cases), 4))

def eliminar_duplicados(arreglo):
    resultado = []
    for lista in arreglo:
        if lista not in resultado:
            resultado.append(lista)
    return resultado

def poda(pm):
    global poblacion
    poblacion = eliminar_duplicados(poblacion)
    if len(poblacion) > pm:
        poblacion = poblacion[:pm]


def reestablecer():
    global a, b, resolucion, formula, nb, poblacion, promedios, peores_casos, mejores_casos
    a = 0
    b = 0
    resolucion = 0
    formula = ""
    nb = 0
    poblacion = []
    mejores_casos = []
    peores_casos = []
    promedios = []


def calcular(f, pi, i, rd, pc, pmi, pmg, pm, ni, max):
    global formula, poblacion, nb
    figs = []
    reestablecer()
    formula = f
    inicializar(pi, i, rd)
    ne = int(b-a)*100
    x_costo = npy.linspace(a*1.1, b*1.1, ne)
    y_costo = [calcular_y_mostrar_resultado(f, valor) for valor in x_costo]
    poblacion.sort(key=lambda x: x[3], reverse=max)
    figs.append(grafica_distribucion(0, poblacion, f, a, b, x_costo, y_costo))
    calcular_estadisticos()
    for i in range(1, ni+1):
        cruza_mutacion(pc, pmi, pmg)
        poblacion.sort(key=lambda x: x[3], reverse=max)
        print(poblacion)
        calcular_estadisticos()
        figs.append(grafica_distribucion(i, poblacion, f, a, b, x_costo, y_costo))
        poda(pm)
    grafica_evolucion(mejores_casos, peores_casos, promedios, ni)
    grabarVideo(figs)
