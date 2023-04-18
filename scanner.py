import socket # Librería puerto para los puertos del PC

def leer_archivo(filename):
    # Le estamos diciendo que, con el archivo abierto, que haga lo siguiente:
    with open(filename, "r") as file:
        lineas= file.readlines()
        lineaslimpias=[]
        for linea in lineas:
            lineaslimpias.append(linea.rstrip())
        return lineaslimpias

# host = input("Introduce la IP a escanear: ") # para que el usuario introduzca la IP
# ports = input("Introduce los puertos a escanear (separados con coma): ") # para que introduzca los puertos

hosts = leer_archivo('ips.txt')
ports = leer_archivo('puertos_comunes.txt')

# print(len(ports)) # para arrays de datos, te dice la cantidad de puertos guardados en la array ports (hemos metido 4)

# Para cada host que haya en "hosts"
for host in hosts: 
    #Para cada puerto que haya en "puertos"
    for port in ports:   #todo lo que creas dentro de un bloque de código existe solo ahí (en este caso for, más abajo if o else)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result= sock.connect_ex((host, int(port))) #La comunicación está abierta, el puerto está abierto
        if result == 0:
            print(f"El puerto {port} está abierto en el host {host}")
        else:
            print(f"El puerto {port} está cerrado en el host {host}")
        sock.close() #La comunicación se cierra para que no esté ocupado el puerto
    