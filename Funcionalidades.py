# Pequeña función que comprueba si el valor introducido es correcto, eliminando los bucles en las otras funciones.
def valores_correctos_numero(inicio, final, numero_a_comprobar):
    try:
        if inicio <= int(numero_a_comprobar) <= final:
            return numero_a_comprobar
        else:
            while not inicio <= numero_a_comprobar <= final:
                print("Has introducido un valor incorrecto, tus opciones son del {} al {}.".format(inicio, final))
                numero_a_comprobar = int(input())
            return numero_a_comprobar
    except ValueError:
        return False
    except TypeError:
        return False


def valores_correctos(inicio, final, numero_a_comprobar):
    es_un_numero = valores_correctos_numero(inicio, final, numero_a_comprobar)
    if es_un_numero is False:
        print("Tienes que introducir un numero para que el programa pueda funcionar.\n")
        while es_un_numero is False:
            numero_a_comprobar = input("Introduce el numero valor, del {} al {}\n".format(inicio, final))
            es_un_numero = valores_correctos_numero(inicio, final, numero_a_comprobar)
        return int(es_un_numero)
    else:
        return int(es_un_numero)


# Podemos comprobar en todo momento el dinero y el inventario del que disponemos.
def comprobar_dinero(dinero, inventario, barcos, turno, prestamos, espacios_barco, precios):
    numero_barcos = barcos[0]
    print("Tienes {} monedas. Estás en el turno {}\n\n"
          "Tu inventario consta de:\n"
          "Telas: {} a {} monedas.\n"
          "Cerveza: {} a {} monedas.\n"
          "Herramientas: {} a {} monedas.\n"
          "Pieles: {} a {} monedas.\n"
          "Vino: {} a {} monedas.\n\n"
          "Tienes {} barco(s) en tu convoy.\n"
          "Te quedan {} prestamos en proceso de ser liquidados\n"
          "Todavía tienes {} espacios sin ocupar en tu flota."
          .format(dinero, turno, inventario[0], precios[0],  inventario[1], precios[1], inventario[2], precios[2],
                  inventario[3], precios[3], inventario[4], precios[4], numero_barcos, len(prestamos), espacios_barco))

# -----------------------------------------------EMPIEZAN LOS BARCOS---------------------------------------------------


def deterioro_barcos(salud_barcos, nombre):
    salud_barcos -= 1
    print("Tus barcos ahora tienen {} % de salud.".format(salud_barcos))
    if salud_barcos == 0:
        print("Tus barcos se han hundido. Lo siento,{}, has perdido la partida.".format(nombre))
        exit()
    else:
        return salud_barcos


def en_viaje(en_viaje, turnos):
    en_viaje[1] += turnos
    if en_viaje[1] > 1:
        en_viaje[0] = True
    return en_viaje


def guardar_partida(datos_partida):
    print("¿Quieres guardar la partida? (De momento solo puede haber una partida guardada)\n1- Si.\n2- No.")
    eleccion = input()
    eleccion = valores_correctos(1, 2, eleccion)
    if eleccion == 1:
        None
    elif eleccion == 2:
        print("De acuerdo. ¡Hasta la proxima!")
        exit()