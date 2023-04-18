import socket # Librería puerto para los puertos del PC

host = input("Introduce la IP a escanear: ") # para que el usuario introduzca la IP
ports = input("Introduce los puertos a escanear (separados con coma): ") # para que introduzca los puertos

ports = ports.split(",") # para que entienda que los numeros entre las comas son distintos unos de otros

print(len(ports)) # para arrays de datos