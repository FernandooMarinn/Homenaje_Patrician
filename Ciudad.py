import random
from Clases import valores_correctos
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
    eleccion = int(input("Bienvenido al prestamista, ¿Qué quieres hacer?\n1- Pedir prestamo   2- Conceder prestamo"
                         "   3- Comprobar prestamos   4- Devolver prestamo   5- Salir."))
    valores_correctos(1, 5, eleccion)
    if eleccion == 1:
        if len(prestamos) > 3:
            print("Ya tienes 3 prestamos en proceso de ser liquidados, mejor esperamos más antes de pedir el siguiente.")
            return "muchos prestamos"
        else:
            imprimir_prestamos(opciones)
            opcion = int(input())
            opcion = valores_correctos(1, 4, opcion)
            if opcion == 4:
                print("De acuerdo, hasta la proxima")
                return "muchos prestamos"
            else:
                prestamo_pedido = opciones[opcion - 1]
                prestamo_pedido.append("solicitado")
                return prestamo_pedido
    elif eleccion == 2:
        if len(prestamos) > 3:
            print("Ya tienes 3 prestamos en proceso de ser liquidados, mejor esperamos más antes de pedir el siguiente.")
            return "muchos prestamos"
        else:
            imprimir_prestamos(opciones)
            opcion = int(input())
            valores_correctos(1, 4, opcion)
            posibles_prestamos = opciones[opcion]
            if opcion == 4:
                print("De acuerdo, hasta la proxima")
                return "no money"
            else:
                if dinero > posibles_prestamos[0]:
                    prestamo_concedido = opciones[opcion - 1]
                    prestamo_concedido.append("concedido")
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
                print("{}- {} monedas.".format(numero_prestamos, prestamo[3]))
                devolver = int(input("¿Quieres devolver este prestamo?\n1- Si.\n2- No.\n"))
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
        print("\nNo tienes ningún prestamo. Vive una vida alejado de las deudas.")
    else:
        numero_prestamo = 1
        for i in prestamos:
            print("\nTienes un prestamo con las siguientes condiciones:")
            print("{}- Has {} {} a un interés de {}%, a devolver en {} turnos. Se devuelven {} monedas.\n"
                  .format(numero_prestamo, i[4], i[0], i[1], i[2], i[3]))
            numero_prestamo += 1


# -------------------------------------------ACABA PRESTAMISTA --------------------------------------------------------

# -------------------------------------------ASTILLERO-----------------------------------------------------------------
def creacion_barcos(dinero):
    print("\n¿Quieres crear un nuevo barco para tu flota?\n1- Si 25000 monedas.\n2- No, salir.")
    eleccion = int(input())
    if eleccion == 1:
        if dinero >= 25000:
            dinero -= 25000
            print("Tu nuevo barco está en construcción, tardará 5 turnos."
                  "\nRecuerda que el nuevo barco tendrá la misma salud que tu flota actual, intenta reparar tus barcos.")
            return dinero, True
        else:
            print("\nNo te puedes permitir el barco.")
    else:
        print("No has introducido un valor correcto.")
    return dinero, False

def reparacion_barco(salud, dinero):
    print("La salud de tu barco es de {}%".format(salud))
    precio_reparacion = (100 - salud) * 500
    opciones = int(input("¿Que quieres hacer?\n"
                         "0- Reparar ({} monedas).\n"
                         "1- Salir.\n".format(precio_reparacion)))

    if opciones == 1:
        print("¡Hasta la vista!")
    elif opciones == 0:
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
    else:
        print("No has elegido una opcion correcta.")

    return salud, dinero

def astillero(salud, dinero, nombre):
    eleccion = int(input("\nBienvenido al astillero {}. ¿Qué deseas hacer?\n1- Reparar flota."
                         "\n2- Construir barco.\n3- Salir.".format(nombre)))
    if eleccion == 3:
        print("De acuerdo, hasta la proxima")
    elif eleccion == 2:
        barco_nuevo = creacion_barcos(dinero)
        return barco_nuevo
    elif eleccion == 1:
        reparar_flota = reparacion_barco(salud, dinero)
        return reparar_flota


# -------------------------------------------ACABA ASTILLERO ----------------------------------------------------------
# -------------------------------------------EMPIEZA CIUDAD ----------------------------------------------------------
def opciones_ciudad(ciudad):
    print("Acabas de llegar a {}.\n".format(ciudad))
    opcion = int(input("¿Qué quieres hacer?\n\n1- Comerciar con la ciudad.\n2- Ir al astillero.\n3- Ir al prestamista.\n"
                       "4- Comprobar dinero e inventario.\n5- Acabar el turno.\n"))
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