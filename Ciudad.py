import random

from Funcionalidades import *
from time import sleep
from Clases import *


# A partir de aqui se definen las funciones de la ciudad:
# --------------------------------------------PRESTAMISTA--------------------------------------------------------------


def generar_prestamos():
    opciones = []
    for i in range(4):
        opcion = [random.randint(5000, 20000), random.randint(20, 50), random.randint(4, 15)]
        opcion.append(round(opcion[0] + ((opcion[0] * opcion[1]) / 100)))
        opciones.append(opcion)

    return opciones


def imprimir_prestamos(opciones):
    opcion_1 = opciones[0]
    opcion_2 = opciones[1]
    opcion_3 = opciones[2]
    print("Tus opciones son:\n"
          "1- {} a un interés de {}%, a devolver en {} turnos. Se devuelven {} monedas.\n"
          "2- {} a un interés de {}%, a devolver en {} turnos. Se devuelven {} monedas.\n"
          "3- {} a un interés de {}%, a devolver en {} turnos. Se devuelven {} monedas.\n"
          "4- Salir".format(opcion_1[0], opcion_1[1], opcion_1[2],
                            opcion_1[3],
                            opcion_2[0], opcion_2[1], opcion_2[2],
                            opcion_2[3],
                            opcion_3[0], opcion_3[1], opcion_3[2],
                            opcion_3[3]))


def prestamista(dinero, opciones, prestamos):
    eleccion = input("Bienvenido al prestamista, ¿Qué quieres hacer?\n1- Pedir prestamo   2- Conceder prestamo"
                     "   3- Comprobar prestamos   4- Devolver prestamo   5- Salir.\n")
    eleccion = valores_correctos(1, 5, eleccion)
    if eleccion == 1:
        if len(prestamos) > 2:
            print("Ya tienes 3 prestamos en proceso de ser liquidados,"
                  " mejor esperamos más antes de pedir el siguiente.")
            return "muchos prestamos"
        else:
            imprimir_prestamos(opciones)
            opcion = input()
            opcion = valores_correctos(1, 4, opcion)
            if opcion == 4:
                print("De acuerdo, hasta la proxima.\n")
                return "muchos prestamos"
            else:
                prestamo_pedido = opciones[opcion - 1]
                prestamo_pedido.append("solicitado")
                print("Enhorabuena, acabas de solicitar un prestamo. Ten en cuenta que se te cobrará en {} turnos"
                      .format(prestamo_pedido[2]))
                return prestamo_pedido
    elif eleccion == 2:
        if len(prestamos) > 3:
            print("Ya tienes 3 prestamos en proceso de ser liquidados,"
                  " mejor esperamos más antes de pedir el siguiente.")
            return "muchos prestamos"
        else:
            imprimir_prestamos(opciones)
            opcion = input()
            opcion = valores_correctos(1, 4, opcion)
            posibles_prestamos = opciones[opcion]
            if opcion == 4:
                print("De acuerdo, hasta la proxima")
                return "no money"
            else:
                if dinero > posibles_prestamos[0]:
                    prestamo_concedido = opciones[opcion - 1]
                    prestamo_concedido.append("concedido")
                    print("Enhorabuena, acabas de conceder un prestamo. Te será devuelto en {} turnos"
                          .format(prestamo_concedido[2]))
                    return prestamo_concedido
                else:
                    print("No tienes suficiente dinero para prestar esa cantidad.")
                    return "no money"
    # Se comprueban los prestamos actuales, si existen.
    elif eleccion == 3:
        comprobador_prestamos(prestamos)
    # Se devuelven los prestamos.
    elif eleccion == 4:
        if len(prestamos) == 0:
            print("No tienes prestamos que devolver")
        numero_prestamos = 0
        for prestamo in prestamos:
            # Solo se comprueban los solicitados, los concedidos se devuelven automaticamente.
            if prestamo[4] == "solicitado":
                numero_prestamos += 1
                print("Se van a mostrar todos los prestamos que has solicitado, elije el que quieres pagar:")
                print("\n{}- {} monedas.".format(numero_prestamos, prestamo[3]))
                devolver = input("¿Quieres devolver este prestamo?\n1- Si.\n2- No.\n")
                devolver = valores_correctos(1, 2, devolver)
                # Se va iterando por todos los prestamos solicitados.
                if devolver == 2:
                    continue
                # Si hay dinero suficiente, se devuelve True y la cantidad a devolver.
                elif devolver == 1 and dinero > prestamo[3]:
                    return True, prestamo[3]
                else:
                    print("No tienes dinero para devolver ese prestamo")
                    return "no money"
        print("Ya no te quedan más prestamos.")
    elif eleccion == 5:
        print("De acuerdo. Vuelve pronto.")


def comprobador_prestamos(prestamos):
    # Si no hay prestamos, devolvemos False
    if len(prestamos) < 1:
        print("\nNo tienes ningún prestamo. Vive una vida alejado de las deudas.\n")
    else:
        numero_prestamo = 1
        for i in prestamos:
            print("\nTienes un prestamo con las siguientes condiciones:")
            print("{}- Has {} {} a un interés de {}%, a devolver en {} turnos. Se devuelven {} monedas.\n"
                  .format(numero_prestamo, i[4], i[0], i[1], i[2], i[3]))
            numero_prestamo += 1


def liquidacion_prestamos(prestamos, dinero):
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
    return prestamos, dinero


def prestamista_paso_final(dinero, prestamos):
    accion_prestamista = prestamista(dinero, generar_prestamos(), prestamos)
    if accion_prestamista == "no money" or accion_prestamista == "muchos prestamos" \
            or accion_prestamista is None:
        return "continuar"
    # Este es un prestamo que devolvemos antes de tiempo.
    elif accion_prestamista[0] is True:
        dinero -= accion_prestamista[1]
        print("Has devuelto un total de {} monedas. El prestamo se elimina."
              .format(accion_prestamista[1]))
        for i in prestamos:
            if i[3] == accion_prestamista[1]:
                prestamos.remove(i)
        return prestamos, dinero
    # Este es un prestamo que se ha solicitado (nos dan dinero)
    elif accion_prestamista[4] == "solicitado":
        prestamos.append(accion_prestamista)
        dinero += accion_prestamista[0]
        return prestamos, dinero
    # Este es un prestamo que hemos concecido (prestamos dinero)
    elif accion_prestamista[4] == "concedido":
        prestamos.append(accion_prestamista)
        dinero -= accion_prestamista[0]
        return prestamos, dinero


# -------------------------------------------ACABA PRESTAMISTA --------------------------------------------------------

# -------------------------------------------ASTILLERO-----------------------------------------------------------------
def creacion_barcos(dinero):
    print("\n¿Quieres crear un nuevo barco para tu flota?\n1- Si 25000 monedas.\n2- No, salir.\n")
    eleccion = input()
    eleccion = valores_correctos(1, 2, eleccion)
    if eleccion == 1:
        if dinero >= 25000:
            dinero -= 25000
            print("Tu nuevo barco está en construcción, tardará 5 turnos."
                  "\nRecuerda que el nuevo barco tendrá la misma salud que tu flota actual,"
                  " intenta reparar tus barcos.")
            return dinero, True
        else:
            print("\nNo te puedes permitir el barco.")
    else:
        print("No has introducido un valor correcto.")
    return dinero, False


def reparacion_barco(salud, dinero, numero_barcos):
    print("La salud de tu barco es de {}%".format(salud))
    precio_reparacion = ((100 - salud) * 500) * numero_barcos
    opciones = input("¿Que quieres hacer?\n"
                     "1- Reparar ({} monedas).\n"
                     "2- Salir.\n".format(precio_reparacion))
    opciones = valores_correctos(1, 2, opciones)

    if opciones == 2:
        print("¡Hasta la vista!")
    elif opciones == 1:
        if dinero >= precio_reparacion:
            dinero -= precio_reparacion
            print("¡Manos a la obra!")
            for i in range(100 - salud + 1):
                print("La salud de tu barco es de {}%.".format(salud))
                salud += 1
                sleep(0.5)
            print("\nTu barco está como nuevo, ya puedes salir a navegar otra vez.")
            salud = 100
            return salud, "reparado", dinero
        else:
            print("No te puedes permitir la reparación.")




def astillero(salud, dinero, nombre, numero_barcos):
    eleccion = int(input("\nBienvenido al astillero, {}. ¿Qué deseas hacer?\n1- Reparar flota."
                         "\n2- Construir barco.\n3- Salir.\n".format(nombre)))
    eleccion = valores_correctos(1, 3, eleccion)
    if eleccion == 3:
        print("De acuerdo, hasta la proxima")
        return False
    elif eleccion == 2:
        barco_nuevo = creacion_barcos(dinero)
        return barco_nuevo
    elif eleccion == 1:
        reparar_flota = reparacion_barco(salud, dinero, numero_barcos)
        return reparar_flota


def comprobacion_barcos(numero_barcos, espacio_barcos):
    if numero_barcos[1] > 0:
        numero_barcos[2] += 1
    if numero_barcos[2] == 5:
        numero_barcos[0] += 1
        numero_barcos[2] = 0
        numero_barcos[1] -= 1
        print("Se ha añadido un nuevo barco a tu flota. ¡Enhorabuena!")
        espacio_barcos += 300
    return numero_barcos, espacio_barcos


# -------------------------------------------ACABA ASTILLERO ----------------------------------------------------------
# -------------------------------------------EMPIEZA CIUDAD ----------------------------------------------------------
def opciones_ciudad(ciudad):
    print("Acabas de llegar a {}.\n".format(ciudad))
    opcion = input("¿Qué quieres hacer?\n\n1- Comerciar con la ciudad.\n2- Ir al astillero.\n3- Ir al prestamista.\n"
                   "4- Comprobar dinero e inventario.\n5- Cambiar de ciudad\n6- Acabar el turno.\n"
                   "7- Salir del juego.\n")
    opcion = valores_correctos(1, 7, opcion)
    return opcion


def en_que_ciudad_estoy(ciudad):
    if ciudad == "Lubeck":
        return 1
    elif ciudad == "Stettin":
        return 2
    elif ciudad == "Rostock":
        return 3
    elif ciudad == "Malmo":
        return 4
    elif ciudad == "Gdanks":
        return 5

def cambio_ciudad(ciudad, salud_barcos, numero_barcos, dinero):
    ciudades = ["Lubeck", "Stettin", "Malmo", "Rostock", "Gdanks"]
    print("\n")
    for i in range(len(ciudades)):
        print("{}- {}.".format(i + 1, ciudades[i]))
    pregunta = input("¿A qué ciudad quieres viajar?\n")
    pregunta = valores_correctos(1, 5, pregunta)
    if ciudades[pregunta - 1] == ciudad:
        print("No puedes viajar a {}, ya estás en ella.".format(ciudades[pregunta - 1]))
    else:
        ciudad = ciudades[pregunta - 1]
        print("Viajando a {}...".format(ciudades[pregunta - 1]))
        cambiar_precios()
        espera_viaje(salud_barcos)
        posible_ataque = ataque_pirata(salud_barcos, numero_barcos, dinero)
        if posible_ataque == "huir":
            print("Aprovechando el viento escapas de la batalla.")
            return ciudad
        elif posible_ataque == "no ataque":
            return ciudad
        elif posible_ataque[0] is True:
            dinero = posible_ataque[1]
            salud_barcos = posible_ataque[2]
            return True, ciudad, dinero, salud_barcos
        elif posible_ataque[0] is False:
            return False, ciudad, posible_ataque[1], posible_ataque[2], posible_ataque[3]



def espera_viaje(salud_barcos):
    if salud_barcos > 90:
        sleep(1)
    elif salud_barcos > 70:
        sleep(1.5)
    elif salud_barcos > 50:
        print("Tu flota empieza a deteriorarse, el viaje tarda un poco más.")
        sleep(2.5)
    elif salud_barcos > 30:
        print("Con las velas en estas condiciones es dificil avanzar. El viaje tardará bastante.")
        sleep(4.5)
    elif salud_barcos > 10:
        print("De milagro tus barcos siguen flotando, es hora de visitar el astillero para repararlos.")
        sleep(6.5)
    else:
        print("Tus marineros están rezando por sus vidas y no pueden trabajar. Acomodate, el viaje será largo.")
        sleep(10)

def cambiar_precios():
    Lubeck.cambiar_precios()
    Rostock.cambiar_precios()
    Stettin.cambiar_precios()
    Malmo.cambiar_precios()
    Gdanks.cambiar_precios()
#------------------------------------------------ACABA CIUDAD-----------------------------------------------------------
#-----------------------------------------------EMPIEZA COMERCIO--------------------------------------------------------

def opciones_comercio(dinero, ciudad, inventario, espacio_barcos, precios):
    opcion = input("¿Qué quieres hacer?\n1- Comprar\n2- Vender\n3- Salir\n")
    opcion = valores_correctos(1, 3, opcion)
    if opcion == 1:
        donde_estoy = que_ciudad(dinero, ciudad, inventario, espacio_barcos, precios, "compra")
        a_retornar = segunda_compra(donde_estoy)
        return a_retornar
    elif opcion == 2:
        donde_estoy = que_ciudad(dinero, ciudad, inventario, espacio_barcos, precios, "venta")
        a_retornar = segunda_compra(donde_estoy)
        return a_retornar
    elif opcion == 3:
        print("De acuerdo, hasta la proxima")


def que_ciudad(dinero, ciudad, inventario, espacio_barcos, precios, modo):
    if ciudad == "Lubeck":
        return Lubeck, dinero, inventario, espacio_barcos, precios, modo
    elif ciudad == "Rostock":
        return Rostock, dinero, inventario, espacio_barcos, precios, modo
    elif ciudad == "Malmo":
        return Malmo, dinero, inventario, espacio_barcos, precios, modo
    elif ciudad == "Stettin":
        return Stettin, dinero, inventario, espacio_barcos, precios, modo
    elif ciudad == "Gdanks":
        return Gdanks, dinero, inventario, espacio_barcos, precios, modo


def segunda_compra(datos_compra):
    stop = False
    ciudad = datos_compra[0]
    dinero = datos_compra[1]
    inventario = datos_compra[2]
    espacio_barcos = datos_compra[3]
    precios = datos_compra[4]
    modo = datos_compra[5]
    ciudad.mostrar_precios()
    while not stop:
        opcion = input("¿Qué quieres comerciar?\n")
        opcion = valores_correctos(1, 5, opcion)
        if opcion == 1:
            producto = ciudad.telas
            posicion_inventario = 0
            a_retornar = tercera_compra(producto, dinero, espacio_barcos, inventario,
                                        posicion_inventario, precios, modo)
            return a_retornar
        elif opcion == 2:
            producto = ciudad.cerveza
            posicion_inventario = 1
            a_retornar = tercera_compra(producto, dinero, espacio_barcos, inventario,
                                        posicion_inventario, precios, modo)
            return a_retornar
        elif opcion == 3:
            producto = ciudad.herramientas
            posicion_inventario = 2
            a_retornar = tercera_compra(producto, dinero, espacio_barcos, inventario,
                                        posicion_inventario, precios, modo)
            return a_retornar
        elif opcion == 4:
            producto = ciudad.pieles
            posicion_inventario = 3
            a_retornar = tercera_compra(producto, dinero, espacio_barcos, inventario,
                                        posicion_inventario, precios, modo)
            return a_retornar
        elif opcion == 5:
            producto = ciudad.vino
            posicion_inventario = 4
            a_retornar = tercera_compra(producto, dinero, espacio_barcos, inventario,
                                        posicion_inventario, precios, modo)
            return a_retornar


def tercera_compra(producto, dinero, espacio_barcos, inventario, posicion_inventario, precios, modo):
    # Si seleccionamos compra.
    if modo == "compra":
        cuantos = int(input("¿Cuantas unidades quieres comprar? Te puedes permitir {}\n"
                            .format(round(dinero / producto - 1))))
        cuantos = valores_correctos(0, round(dinero / producto - 1), cuantos)
        if dinero >= cuantos * producto:
            if espacio_barcos >= cuantos:
                if precios[posicion_inventario] == 0:
                    precios[posicion_inventario] = producto
                elif precios[posicion_inventario] == producto:
                    precios[posicion_inventario] = producto
                else:
                    nuevo_precio_medio = round((inventario[posicion_inventario] * precios[posicion_inventario] +
                                                cuantos * producto) / (cuantos + inventario[posicion_inventario]))
                    precios[posicion_inventario] = nuevo_precio_medio
                dinero -= cuantos * producto
                inventario[posicion_inventario] += cuantos
                espacio_barcos -= cuantos
                print("Acabas de comprar {} unidades a {} monedas. Te quedan {} espacios libres.\n"
                      .format(cuantos, cuantos * producto, espacio_barcos))
                return dinero, inventario, espacio_barcos, precios

            else:
                print("No tienes suficiente espacio en tu flota para cargar tantas mercancias.")
        else:
            print("No tienes suficiente dinero para comprar tantas mercancias.")
    # Si seleccionamos venta.
    elif modo == "venta":
        cuantos = input("¿Cuantas unidades quieres vender? Tienes {} unidades en el inventario.\n"
                        .format(inventario[posicion_inventario]))
        cuantos = valores_correctos(0, inventario[posicion_inventario], cuantos)
        dinero += cuantos * producto
        inventario[posicion_inventario] -= cuantos
        espacio_barcos += cuantos
        if inventario[posicion_inventario] == 0:
            precios[posicion_inventario] = 0
        print("Has vendido {} unidades por un total de {} monedas".format(cuantos, cuantos * producto))

        return dinero, inventario, espacio_barcos, precios
