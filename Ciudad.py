import random
from Funcionalidades import valores_correctos
from time import sleep
# A partir de aqui se definen las funciones de la ciudad:
#---------------------------------------------PRESTAMISTA--------------------------------------------------------------
def generar_prestamos():
    opciones = []
    for i in range(4):
        opcion = [random.randint(5000, 20000), random.randint(20, 50), random.randint(4, 15)]
        opcion.append(round(opcion[0] + (opcion[0] * opcion[1]) / 100))
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
                            opcion_1[0] + opcion_1[3],
                            opcion_2[0],  opcion_2[1],  opcion_2[2],
                            opcion_2[0] + opcion_2[3],
                            opcion_3[0], opcion_3[1], opcion_3[2],
                            opcion_3[0] + opcion_3[3]))


def prestamista(dinero, opciones, prestamos):
    eleccion = input("Bienvenido al prestamista, ¿Qué quieres hacer?\n1- Pedir prestamo   2- Conceder prestamo"
                         "   3- Comprobar prestamos   4- Devolver prestamo   5- Salir.\n")
    valores_correctos(1, 5, eleccion)
    if eleccion == 1:
        if len(prestamos) > 3:
            print("Ya tienes 3 prestamos en proceso de ser liquidados,"
                  " mejor esperamos más antes de pedir el siguiente.")
            return "muchos prestamos"
        else:
            imprimir_prestamos(opciones)
            opcion = input()
            opcion = valores_correctos(1, 4, opcion)
            if opcion == 4:
                print("De acuerdo, hasta la proxima")
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
            valores_correctos(1, 4, opcion)
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
            or accion_prestamista == None:
        return "continuar"
    # Este es un prestamo que devolvemos antes de tiempo.
    elif accion_prestamista[0] == True:
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
    print("\n¿Quieres crear un nuevo barco para tu flota?\n1- Si 25000 monedas.\n2- No, salir.")
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

def reparacion_barco(salud, dinero):
    print("La salud de tu barco es de {}%".format(salud))
    precio_reparacion = (100 - salud) * 500
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
        else:
            print("No te puedes permitir la reparación.")

    return salud, dinero

def astillero(salud, dinero, nombre):
    eleccion = int(input("\nBienvenido al astillero, {}. ¿Qué deseas hacer?\n1- Reparar flota."
                         "\n2- Construir barco.\n3- Salir.".format(nombre)))
    if eleccion == 3:
        print("De acuerdo, hasta la proxima")
    elif eleccion == 2:
        barco_nuevo = creacion_barcos(dinero)
        return barco_nuevo
    elif eleccion == 1:
        reparar_flota = reparacion_barco(salud, dinero)
        return reparar_flota

def comprobacion_barcos(numero_barcos):
    if numero_barcos[1] > 0:
        numero_barcos[2] += 1
    if numero_barcos[2] == 5:
        numero_barcos[0] += 1
        numero_barcos[2] = 0
        numero_barcos[1] -= 1
        print("Se ha añadido un nuevo barco a tu flota. ¡Enhorabuena!")
    return numero_barcos

# -------------------------------------------ACABA ASTILLERO ----------------------------------------------------------
# -------------------------------------------EMPIEZA CIUDAD ----------------------------------------------------------
def opciones_ciudad(ciudad):
    print("Acabas de llegar a {}.\n".format(ciudad))
    opcion = input("¿Qué quieres hacer?\n\n1- Comerciar con la ciudad.\n2- Ir al astillero.\n3- Ir al prestamista.\n"
                       "4- Comprobar dinero e inventario.\n5- Acabar el turno.\n")
    opcion = valores_correctos(1, 5, opcion)
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
    else:
        ValueError("Ups, parece que algo ha ido mal en la elección de la ciudad.")


# -------------------------------------------ACABA CIUDAD--------------------------------------------------------------