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

def valores_correctos(inicio, final, numero_a_comprobar):
    es_un_numero = valores_correctos_numero(inicio, final, numero_a_comprobar)
    if es_un_numero == False:
        print("Tienes que introducir un numero para que el programa pueda funcionar.\n")
        while es_un_numero == False:
            numero_a_comprobar = input("Introduce el numero valor, del {} al {}\n".format(inicio, final))
            es_un_numero = valores_correctos_numero(inicio, final, numero_a_comprobar)
        return int(es_un_numero)
    else:
        return int(es_un_numero)

# Podemos comprobar en todo momento el dinero y el inventario del que disponemos.
def comprobar_dinero(dinero, inventario, barcos, turno, prestamos):
    print("Tienes {} monedas. Estás en el turno {}\n\n"
          "Tu inventario consta de:\n"
          "Cerveza: {}\n"
          "Telas: {}\n"
          "Herramientas: {}\n"
          "Pieles: {}\n"
          "Vino: {}\n\n"
          "Tienes {} barco(s) en tu convoy.\n"
          "Te quedan {} prestamos en proceso de ser liquidados\n"
          .format(dinero, turno, inventario[0], inventario[1], inventario[2],
                  inventario[3], inventario[4], barcos[0], len(prestamos)))

