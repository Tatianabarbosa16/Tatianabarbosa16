
nombre  = "Casa Rosa"
antiguedad = 23  
comprada  = True
altura  = 3.5
print("nombre", nombre)
print("antiguedad", antiguedad)
print("comprada", comprada )
print("altura", altura, "m")

print("nombre", type(nombre))
print("antiguedad", type(antiguedad))
print("cromprada", type(comprada))
print("altura", type(altura))

nombre  = "Casa Rosa"
antiguedad = 23  
comprada  = True
altura  = 3.5
datos = "El nombre de la casa es: " + nombre + ", su antiguedad es: " + str(antiguedad) + ", vendida: " + str(comprada) + ", su altura es: " + str(altura)
print(datos) 
#Los enteros en python no tienen limite.
#El límite para un número flotante en Python depende del sistema en el que estás trabajando. Python utiliza el tipo float, que típicamente es un flotante de doble precisión que sigue el estándar IEEE 754. Esto significa que tiene una precisión de hasta 15 dígitos decimales y un rango amplio de exponentes.

#suma de n numeros 
suma = 0
n = 1
while n != 0: 
    n = int(input("Iingresa un numero: "))
    if n != 0:
        if n % 2 == 0:
            suma = suma + n
print("La suma de los numeros pares es:",suma)            