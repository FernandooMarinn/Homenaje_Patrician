# Importamos random para producir precios de manera aleatoria y tiempo para la cuenta atrás entre ciudades.
from Ciudad import *
from Clases import *

# Se definen la clase ciudad, con productos y sus correspondientes precios.

# ----------------------------------------------CIUDADES---------------------------------------------------------------


# Se definen las ciudades y se inicializan sus precios.
# Lubeck produce algo de vino, y herramientas.
Lubeck = Ciudad(1400, 1000, 450, 250, 70, 45, 290, 200, 420, 300, "Lubeck")
# Stettin produce cerveza.
Stettin = Ciudad(1400, 1000, 450, 250, 42, 32, 400, 280, 420, 300, "Stettin")
# Malmo produce telas y pieles.
Malmo = Ciudad(1100, 700, 450, 250, 70, 45, 400, 280, 300, 200, "Malmo")
# Rostock compra de todo.
Rostock = Ciudad(1400, 1000, 450, 250, 70, 45, 400, 280, 420, 300, "Rostock")


# Podemmos comprobar en todo momento el dinero y el inventario del que disponemos.
def comprobar_dinero(dinero, inventario, barcos):
    print("Tienes {} monedas.\n\n"
          "Tu inventario consta de:\n"
          "Cerveza: {}\n"
          "Telas: {}\n"
          "Herramientas: {}\n"
          "Pieles: {}\n"
          "Vino: {}\n\n"
          "Tienes {} barco(s) en tu convoy.\n"
          .format(dinero, inventario[0], inventario[1], inventario[2], inventario[3], inventario[4], barcos[0]))


# Preguntamos el nombre de jugador, el inventario a 0 y el dinero inicial.
def jugador():
    datos_jugador = [input("¿Cual es tu nombre?\n"), 0, [0, 0, 0, 0, 0]]
    dinero_jugador = int(input("¿Con cuanto dinero quieres empezar?\n"
                               "\n1- 1000 monedas (muy poco)\n2- 5000 monedas (poco)"
                               "\n3- 15000 monedas (normal)\n4- 30000 monedas (mucho)"
                               "\n5- 50000 monedas (muchísimo)\n"))
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
    pregunta = int(input("¿Cual quieres que sea tu ciudad de inicio?\n"))
    pregunta = valores_correctos(1, 4, pregunta)
    return ciudades[pregunta - 1]


def turno(turno):
    turno += 1
    return turno


# ----------------------------------------------------------------------------------------------------------------------
def opciones_comercio(dinero, espacio):
    opcion = int(input("¿Que quieres hacer?\n"
                       "0- Comprar.\n"
                       "1- Vender.\n"
                       "2- Salir.\n"))

    return opcion


def comprar(dinero, espacio):
    eleccion_compra = int(input("¿Qué quieres comprar?\n"
                                "1- Tela"))


def juego(jugador, ciudad_inicio):
    # Empezamos guardando los datos.
    stop = False
    turno = 0
    salud_barcos = 100
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
        # Aqui tenemos que tener en cuenta los prestamos, y cuando pasan los turnos:
        for prestamo in prestamos:
            # Cada turno se disminuye en 1 los turnos que faltan para devolver el prestamo.
            prestamo[2] -= 1
            # Si los turnos acaban:
            if prestamo[2] < 1:
                # Si el prestamo estaba solicitado, se devuelve el dinero.
                if prestamo[4] == "solicitado":
                    print("Ha llegado el momento de pagar tu prestamo. Se te descuentan {} monedas.".format(prestamo[3]))
                    dinero -= prestamo[3]
                    prestamos.remove(prestamo)
                # En cambio, si lo habiamos concedido nos devuelven a nosotros.
                elif prestamo[4] == "concedido":
                    print("Ha llegado el momento de que te devuelvan el prestamo que concediste. Ingresas {} monedas."
                          .format(prestamo[3]))
                    dinero += prestamo[3]
                    prestamos.remove(prestamo)
        # Aqui tenemos en cuenta la creación de barcos, y cuando pasan los turnos:
        if numero_barcos[1] > 0:
            numero_barcos[2] += 1
        if numero_barcos[2] == 5:
            numero_barcos[0] += 1
            numero_barcos[2] = 0
            numero_barcos[1] -= 1
            print("Se ha añadido un nuevo barco a tu flota. ¡Enhorabuena!")
        print("*" * 50)
        # Preguntamos que queremos hacer en esta ciudad.
        # Bucle para no pasar de turno automáticamente.
        while not stop:
            eleccion = opciones_ciudad(ciudad)
            eleccion = valores_correctos(1, 5, eleccion)
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
                accion_prestamista = prestamista(dinero, generar_prestamos(), prestamos)
                if accion_prestamista == "no money" or accion_prestamista == "muchos prestamos"\
                or accion_prestamista == None:
                    continue
                # Este es un prestamo que devolvemos antes de tiempo.
                elif accion_prestamista[0] == True:
                    dinero -= accion_prestamista[1]
                    print("Has devuelto un total de {} monedas. El prestamo se elimina."
                          .format(accion_prestamista[1]))
                    for i in prestamos:
                        if i[3] == accion_prestamista[1]:
                            prestamos.remove(i)
                # Este es un prestamo que se ha solicitado (nos dan dinero)
                elif accion_prestamista[4] == "solicitado":
                    prestamos.append(accion_prestamista)
                    dinero += accion_prestamista[0]
                # Este es un prestamo que hemos concecido (prestamos dinero)
                elif accion_prestamista[4] == "concedido":
                    prestamos.append(accion_prestamista)
                    dinero -= accion_prestamista[0]
            elif eleccion == 4:
                comprobar_dinero(dinero, inventario, numero_barcos)
                continue
            elif eleccion == 5:
                print("{} ha dejado pasar un turno.\n\n".format(nombre))
                break


# Funcion principal.
def main():
    print("Bienvenido a el gran patrician 3.")
    juego(jugador(), ciudad_inicial())


# Llamamos aqui a la función principal, de momento es lugar de pruebas.
if __name__ == '__main__':
    main()
    print("De alguna maravillosa manera has terminado")