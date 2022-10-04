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


def juego(jugador, ciudad_inicio):
    # Empezamos guardando los datos.
    stop = False
    en_viaje = [False, 0]
    turno = 0
    salud_barcos = 90
    numero_barcos = [1, 0, 0]
    espacio_barcos = 300
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
        # Aqui se tienen en cuenta los prestamos
        evolucion_prestamos = liquidacion_prestamos(prestamos, dinero)
        prestamos = evolucion_prestamos[0]
        dinero = evolucion_prestamos[1]
        # Aqui tenemos en cuenta la creación de barcos, y cuando pasan los turnos:
        cambio_barcos = comprobacion_barcos(numero_barcos, espacio_barcos)
        numero_barcos = cambio_barcos[0]
        espacio_barcos = cambio_barcos[1]
        salud_barcos = deterioro_barcos(salud_barcos, nombre)
        print("*" * 50)
        # Preguntamos que queremos hacer en esta ciudad.
        # Bucle para no pasar de turno automáticamente.
        while not stop:
            # Si estamos en viaje, se pasan varios turnos seguidos.
            if en_viaje[1] < 1:
                en_viaje[0] = False
            if en_viaje[0] is True:
                en_viaje[1] -= 1
                continue
            eleccion = opciones_ciudad(ciudad)
            # Si elegimos el comercio.
            if eleccion == 1:
                separar_opciones()
                comercio = opciones_comercio(dinero, ciudad, inventario, espacio_barcos, precios)
                if comercio is None:
                    continue
                dinero = comercio[0]
                inventario = comercio[1]
                espacio_barcos = comercio[2]
                precios = comercio[3]
            # Si elegimos el astillero.
            elif eleccion == 2:
                separar_opciones()
                eleccion_astillero = astillero(salud_barcos, dinero, nombre, numero_barcos[0])
                if eleccion_astillero[1] is True:
                    dinero = eleccion_astillero[0]
                    numero_barcos[1] += 1
                    continue
                elif eleccion_astillero[1] is False:
                    continue
                elif eleccion_astillero[1] == "reparado":
                    salud_barcos = eleccion_astillero[0]
                    dinero = eleccion_astillero[2]
            # Esto es el prestamista.
            elif eleccion == 3:
                separar_opciones()
                prestamos_procesados = prestamista_paso_final(dinero, prestamos)
                if prestamos_procesados == "continuar":
                    continue
                else:
                    prestamos = prestamos_procesados[0]
                    dinero = prestamos_procesados[1]
            elif eleccion == 4:
                separar_opciones()
                comprobar_dinero(dinero, inventario, numero_barcos, turno, prestamos, espacio_barcos, precios)
                continue
            # Aquí cambiamos de ciudad.
            elif eleccion == 5:
                separar_opciones()
                viaje_entre_ciudades = cambio_ciudad(ciudad)
                if ciudad == viaje_entre_ciudades:
                    continue
                else:
                    ciudad = viaje_entre_ciudades
                    break
            # Aquí se termina el turno.
            elif eleccion == 6:
                separar_opciones()
                print("{} ha dejado pasar un turno.\n\n".format(nombre))
                break
            elif eleccion == 7:
                print("¡Hasta la vista!")
                exit()


# Función principal.
def main():
    print("\nBienvenido a este homenaje al juego Patrician III. Creado por FernandooMarinn (GitHub)")
    separar_opciones()
    juego(jugador(), ciudad_inicial())


# Llamamos aqui a la función principal, de momento es lugar de pruebas.
if __name__ == '__main__':
    main()
    print("De alguna maravillosa manera has terminado")
