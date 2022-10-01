# Importamos los archivos de ciudad y de clases.
from Ciudad import *
from Clases import *
from Funcionalidades import *

# Preguntamos el nombre de jugador, el inventario a 0 y el dinero inicial.
def jugador():
    datos_jugador = [input("¿Cual es tu nombre?\n"), 0, [0, 0, 0, 0, 0]]
    dinero_jugador = input("¿Con cuanto dinero quieres empezar?\n"
                               "\n1- 1000 monedas (muy poco)\n2- 5000 monedas (poco)"
                               "\n3- 15000 monedas (normal)\n4- 30000 monedas (mucho)"
                               "\n5- 50000 monedas (muchísimo)\n")
    dinero_jugador = valores_correctos(1, 5, dinero_jugador)
    if dinero_jugador == 1:
        datos_jugador[1] = 1000
    elif dinero_jugador == 2:
        datos_jugador[1] = 5000
    elif dinero_jugador == 3:
        datos_jugador[1] = 15000
    elif dinero_jugador == 4:
        datos_jugador[1] = 30000
    elif dinero_jugador == 5:
        datos_jugador[1] = 50000
    return datos_jugador


def precio_aleatorio(precio):
    precio = random.randint(precio[0], precio[1])
    return precio


# Se prepara la factura del 5% cada ronda.
def factura(dinero):
    print("Se cobra la factura del turno, con un total de {} monedas.".format(round(dinero * 0.05)))
    return round(dinero * 0.05)


# Elegimos la ciudad de inicio.
def ciudad_inicial():
    ciudades = ["Lubeck", "Stettin", "Malmo", "Rostock"]
    print("\n")
    for i in range(len(ciudades)):
        print("{}- {}.".format(i + 1, ciudades[i]))
    pregunta = input("¿Cual quieres que sea tu ciudad de inicio?\n")
    pregunta = valores_correctos(1, 4, pregunta)
    return ciudades[pregunta - 1]
# ----------------------------------------------------------------------------------------------------------------------
def opciones_comercio(dinero, espacio):
    opcion = input("¿Que quieres hacer?\n"
                       "1- Comprar.\n"
                       "2- Vender.\n"
                       "3- Salir.\n")
    opcion = valores_correctos(1, 3, opcion)
    return opcion


def comprar(dinero, espacio):
    eleccion_compra = int(input("¿Qué quieres comprar?\n"
                                "1- Tela"))


def juego(jugador, ciudad_inicio):
    # Empezamos guardando los datos.
    stop = False
    turno = 0
    salud_barcos = 90
    numero_barcos = [1, 0, 0]
    espacio_barcos = 300 * numero_barcos[0]
    prestamos = []
    inventario = jugador[2]
    precios = [0, 0, 0, 0, 0]
    dinero = jugador[1]
    nombre = jugador[0]
    ciudad = ciudad_inicio
    print("Bienvenido a tu ciudad natal {}. Ahora debes comerciar, crear barcos y expandir tu imperio, {}.\n\n"
          .format(ciudad, nombre))
    while not stop:
        # Cada turno, aumentamos en 1 el turno.
        print("*" * 50)
        turno += 1
        dinero -= factura(dinero)
        print("Se avanza un turno, ahora vas por el turno {}.\n".format(turno))
        #Aqui se tienen en cuenta los prestamos
        evolucion_prestamos = liquidacion_prestamos(prestamos, dinero)
        prestamos = evolucion_prestamos[0]
        dinero = evolucion_prestamos[1]
        # Aqui tenemos en cuenta la creación de barcos, y cuando pasan los turnos:
        numero_barcos = comprobacion_barcos(numero_barcos)
        print("*" * 50)
        # Preguntamos que queremos hacer en esta ciudad.
        # Bucle para no pasar de turno automáticamente.
        while not stop:
            eleccion = opciones_ciudad(ciudad)
            eleccion = valores_correctos(1, 5, eleccion)
            # Si elegimos el comercio.
            if eleccion == 1:
                # Comprobamos en que ciudad estamos, mostramos los precios y preguntamos las opciones de comercio.
                ciudad_actual = en_que_ciudad_estoy(ciudad)
                if ciudad_actual == 1:
                    Lubeck.mostrar_precios()
                    eleccion_comercio = opciones_comercio(dinero, espacio_barcos)
                    continue
                elif ciudad_actual == 2:
                    Stettin.mostrar_precios()
                    eleccion_comercio = opciones_comercio(dinero, espacio_barcos)
                    continue
                elif ciudad_actual == 3:
                    Rostock.mostrar_precios()
                    eleccion_comercio = opciones_comercio(dinero, espacio_barcos)
                    continue
                elif ciudad_actual == 4:
                    Malmo.mostrar_precios()
                    eleccion_comercio = opciones_comercio(dinero, espacio_barcos)
                    continue
            elif eleccion == 2:
                eleccion_astillero = astillero(salud_barcos, dinero, nombre)
                if eleccion_astillero[1] == True:
                    dinero = eleccion_astillero[0]
                    numero_barcos[1] += 1
                    continue
            # Esto es el prestamista.
            elif eleccion == 3:
                prestamos_procesados = prestamista_paso_final(dinero, prestamos)
                if prestamos_procesados == "continuar":
                    continue
                else:
                    prestamos = prestamos_procesados[0]
                    dinero = prestamos_procesados[1]
            elif eleccion == 4:
                comprobar_dinero(dinero, inventario, numero_barcos, turno, prestamos)
                continue
            # Aquí se termina el turno.
            elif eleccion == 5:
                print("{} ha dejado pasar un turno.\n\n".format(nombre))
                break


# Función principal.
def main():
    print("Bienvenido a este homenaje al juego Patrician III. Creado por FernandooMarinn (GitHub)")
    juego(jugador(), ciudad_inicial())


# Llamamos aqui a la función principal, de momento es lugar de pruebas.
if __name__ == '__main__':
    main()
    print("De alguna maravillosa manera has terminado")