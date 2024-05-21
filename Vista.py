import tkinter as tk
from AlgoritmoGenetico import calcular

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

ventana = tk.Tk()
ventana.title("Algoritmo genetico")

ventana.configure(bg='aqua')


def calcular_algoritmo_genetico(maximizar):
    formula_str = input_formula.get()
    poblacion_inicial = int(input_poblacion_inicial.get())
    intervalo = input_intervalo.get()
    resolucion = float(input_resolucion_deseable.get())
    prob_cruza = float(input_prob_cruza.get())
    prob_mutacion_ind = float(input_prob_mutacion_ind.get())
    prob_mutacion_gen = float(input_prob_mutacion_gen.get())
    poblacion_maxima = int(input_poblacion_maxima.get())
    num_iteraciones = int(input_num_iteraciones.get())
    calcular(formula_str, poblacion_inicial, intervalo, resolucion,
              prob_cruza, prob_mutacion_ind, prob_mutacion_gen,
              poblacion_maxima, num_iteraciones, maximizar)

# Etiquetas
text_formula = tk.Label(ventana, text="Ingrese la formula", bg="white", font=12)
text_formula.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
text_población_inicial = tk.Label(ventana, text="Ingrese la población inicial", bg="white", font=12)
text_población_inicial.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
text_intervalo = tk.Label(ventana, text="Ingrese el intervalo", bg="white", font=12)
text_intervalo.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
text_resolucion_deseable = tk.Label(ventana, text="Ingrese la resolucion deseable", bg="white", font=12)
text_resolucion_deseable.grid(row=3, column=0, padx=5, pady=5, columnspan=2)
text_prob_cruza = tk.Label(ventana, text="Ingrese la probabilidad de cruza", bg="white", font=12)
text_prob_cruza.grid(row=4, column=0, padx=5, pady=5, columnspan=2)
text_prob_mutacion_ind = tk.Label(ventana, text="Ingrese la probabilidad de mutacion del individuo", bg="white", font=12)
text_prob_mutacion_ind.grid(row=5, column=0, padx=5, pady=5, columnspan=2)
text_prob_mutacion_gen = tk.Label(ventana, text="Ingrese la probabilidad de mutacion del gen", bg="white", font=12)
text_prob_mutacion_gen.grid(row=6, column=0, padx=5, pady=5, columnspan=2)
text_poblacion_maxima = tk.Label(ventana, text="Ingrese la poblacion maxima", bg="white", font=12)
text_poblacion_maxima.grid(row=7, column=0, padx=5, pady=5, columnspan=2)
text_num_iteraciones = tk.Label(ventana, text="Ingrese el numero de iteraciones", bg="white", font=12)
text_num_iteraciones.grid(row=8, column=0, padx=5, pady=5, columnspan=2)

# Entradas
input_formula = tk.Entry(ventana, width=30)
input_formula.grid(row=0, column=2, padx=5, pady=5, columnspan=2)
input_poblacion_inicial = tk.Entry(ventana, width=15)
input_poblacion_inicial.grid(row=1, column=2, padx=5, pady=5, columnspan=2)
input_intervalo = tk.Entry(ventana, width=15)
input_intervalo.grid(row=2, column=2, padx=5, pady=5, columnspan=2)
input_resolucion_deseable = tk.Entry(ventana, width=15)
input_resolucion_deseable.grid(row=3, column=2, padx=5, pady=5, columnspan=2)
input_prob_cruza = tk.Entry(ventana, width=15)
input_prob_cruza.grid(row=4, column=2, padx=5, pady=5, columnspan=2)
input_prob_mutacion_ind = tk.Entry(ventana, width=15)
input_prob_mutacion_ind.grid(row=5, column=2, padx=5, pady=5, columnspan=2)
input_prob_mutacion_gen = tk.Entry(ventana, width=15)
input_prob_mutacion_gen.grid(row=6, column=2, padx=5, pady=5, columnspan=2)
input_poblacion_maxima = tk.Entry(ventana, width=15)
input_poblacion_maxima.grid(row=7, column=2, padx=5, pady=5, columnspan=2)
input_num_iteraciones = tk.Entry(ventana, width=15)
input_num_iteraciones.grid(row=8, column=2, padx=5, pady=5, columnspan=2)

boton_maximizar = tk.Button(ventana, text="Maximizar", command=lambda: calcular_algoritmo_genetico(True), font=12)
boton_maximizar.grid(row=9, column=1, padx=5, pady=5, columnspan=2)

boton_minimizar = tk.Button(ventana, text="Minimizar", command=lambda: calcular_algoritmo_genetico(False), font=12)
boton_minimizar.grid(row=9, column=3, padx=5, pady=5, columnspan=2)

ventana.update_idletasks()
center_window(ventana)

ventana.mainloop()
