import random
from time import sleep
from Clases import *
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
          .format(dinero, turno, inventario[0], precios[0],  inventario[1], precios[1], inventario[2], precios[2],
                  inventario[3], precios[3], inventario[4], precios[4], numero_barcos))
    if len(prestamos) > 0:
        print("Tienes {} prestamos pendientes de liquidar.".format(len(prestamos)))
    elif len(prestamos) == 0:
        print("No tienes prestamos pendientes")
    if espacios_barco == 0:
        print("No te queda espacio de carga en tu flota.")
    else:
        print("Todavía tienes {} espacios de carga libres en tu flota.".format(espacios_barco))
# -----------------------------------------------EMPIEZAN LOS BARCOS---------------------------------------------------


def deterioro_barcos(salud_barcos, nombre):
    salud_barcos -= 1
    print("Tus barcos ahora tienen {} % de salud.".format(salud_barcos))
    if salud_barcos == 0:
        print("Tus barcos se han hundido. Lo siento,{}, has perdido la partida.".format(nombre))
        exit()
    else:
        return salud_barcos


def ataque_pirata(salud_barcos, numero_barcos, dinero):
    probabilidad_de_ataque = random.randint(1, 10)
    if probabilidad_de_ataque == 5:
        numero_barcos_pirata = random.randint(1, numero_barcos[0] + 2)
        salud_barcos_pirata = random.randint(40, 100)
        print("¡Te están atacando {} barcos piratas! La salud de tu(s) {} barcos es de {}%.\n¿Qué quieres hacer?\n"
              "1- Enfrentarte a ellos.\n2- Huir."
              .format(numero_barcos_pirata, numero_barcos[0], salud_barcos))
        eleccion = input()
        eleccion = valores_correctos(1, 2, eleccion)
        if eleccion == 1:
            resultado_combate = combate(salud_barcos, numero_barcos, numero_barcos_pirata, salud_barcos_pirata)
            if resultado_combate is False:
                inventario = [0, 0, 0, 0, 0]
                precios = [0, 0, 0, 0, 0]
                numero_barcos = 0
                return False, inventario, precios, numero_barcos
            elif resultado_combate[0] is True:
                botin_consegido = botin_pirata(numero_barcos_pirata, dinero)
                dinero = botin_consegido
                salud_barcos = resultado_combate[1]
                return True, dinero, salud_barcos
        elif eleccion == 2:
            return "huir"
    else:
        return "no ataque"


def combate(salud_barcos, numero_barcos, numero_barcos_pirata, salud_barcos_pirata):
    while salud_barcos > 0 and salud_barcos_pirata > 0:
        if salud_barcos % 5 == 0:
            print("La salud de tu(s) barcos va por {}%.".format(salud_barcos))
            separar_opciones()
        if salud_barcos_pirata % 5 == 0:
            print("La salud de tu enemigo va por {}%.".format(salud_barcos_pirata))
            separar_opciones()
        salud_barcos -= numero_barcos_pirata
        salud_barcos_pirata -= numero_barcos[0]
        sleep(0.1)
    if salud_barcos < 1:
        print("Tu audacia no te ha salvado de perder tus barcos. Esperemos que tengas monedas para fabricar un barco.")
        return False
    elif salud_barcos_pirata < 1:
        print("Contra viento y marea, has conseguido superar al pirata. ¡Enhorabuena!")
        return True, salud_barcos


def botin_pirata(numero_barcos_pirata, dinero):
    botin = random.randint(20000, 50000)
    dinero += botin * numero_barcos_pirata
    print("El capitán enemigo guardaba {} monedas en cada barco. Al hacerte con el botín, tu fortuna aumenta a {}"
          " monedas."
          .format(botin, dinero))
    return dinero

# -----------------------------------------------ACABAN LOS BARCOS----------------------------------------------

def factura(dinero, numero_barcos):
    return round(dinero * 0.02) + 1500 * numero_barcos


def guardar_partida(datos_partida):
    print("¿Quieres guardar la partida? (De momento solo puede haber una partida guardada)\n1- Si.\n2- No.")
    eleccion = input()
    eleccion = valores_correctos(1, 2, eleccion)
    if eleccion == 1:
        None
    elif eleccion == 2:
        print("De acuerdo. ¡Hasta la proxima!")
        exit()


def separar_opciones():
    print("-" * 180)