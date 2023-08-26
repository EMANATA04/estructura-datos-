edades = [35, 12, 15, 40, 20]

def promedio_edades (edades):
    suma = 0
    for n in edades:
        suma = suma + n

    return suma / len (edades)
for n in edades: 
    print(f"edades: {n}")    

promedio = promedio_edades (edades)
print (f"el pormedio de las edades es {promedio}")