# Importa la librería random
import random

# Función para generar una lista de nodos aleatorios
def generar_lista_de_nodos(numero_de_nodos):
    lista_de_nodos = []
    
    for nodo_actual in range(numero_de_nodos):
        nodo_minimo = nodo_actual
        nodo_maximo = nodo_actual + 10
        nodo_aleatorio = random.randint(nodo_minimo, nodo_maximo)
        lista_de_nodos.append(nodo_aleatorio)
    
    return lista_de_nodos

# Solicita al usuario la cantidad de nodos que desea crear
try:
    numero_de_nodos = int(input("Ingrese el número de nodos a crear: "))
except ValueError:
    print("Error: Ingrese un número válido.")
    exit(1)

# Llama a la función para generar la lista de nodos
nodos_generados = generar_lista_de_nodos(numero_de_nodos)

# Imprime la lista con los nodos generados
print("Lista de nodos generada:")
for indice, nodo in enumerate(nodos_generados):
    print(f"Nodo {indice + 1}: {nodo}")
