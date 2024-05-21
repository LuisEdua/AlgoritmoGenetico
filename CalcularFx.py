import sympy as sp

def calcular_y_mostrar_resultado(expresion_str, valor):
    x = sp.symbols('x')

    try:
        expresion = sp.sympify(expresion_str)

        resultado = expresion.subs(x, valor)
        return resultado
    except sp.SympifyError:
        print("Error al analizar la expresión.")