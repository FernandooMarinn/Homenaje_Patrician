import random

class Ciudad:

    # Declaramos los precios minimos y maximos para los productos, que vienen como argumentos de la función.
    def __init__(self, max_pieles, min_pieles, max_herramientas, min_herramientas, max_cerveza, min_cerveza,
                 max_vino, min_vino, max_telas, min_telas, nombre):

        self.pieles = random.randint(min_pieles, max_pieles)
        self.herramientas = random.randint(min_herramientas, max_herramientas)
        self.cerveza = random.randint(min_cerveza, max_cerveza)
        self.vino = random.randint(min_vino, max_vino)
        self.telas = random.randint(min_telas, max_telas)
        self.nombre = nombre

        # Se guardan los maximos y los minimos
        self.max_pieles = max_pieles
        self.min_pieles = min_pieles
        self.max_herramientas = max_herramientas
        self.min_herramientas = min_herramientas
        self.max_cerveza = max_cerveza
        self.min_cerveza = min_cerveza
        self.max_vino = max_vino
        self.min_vino = min_vino
        self.max_telas = max_telas
        self.min_telas = min_telas


    # Funcion para determinar los precios de manera aleatoria, teniendo en cuenta los precios max y min.

    def cambiar_precios(self):
        self.pieles = random.randint(self.min_pieles, self.max_pieles)
        self.herramientas = random.randint(self.min_herramientas, self.max_herramientas)
        self.cerveza = random.randint(self.min_cerveza, self.max_cerveza)
        self.vino = random.randint(self.min_vino, self.max_vino)
        self.telas = random.randint(self.min_telas, self.max_telas)
    # Imprimir los precios en pantalla.

    def mostrar_precios(self):
        print("""Los precios actuales de {} son:
        Telas: {}
        Cerveza: {}
        Herramientas: {}
        Pieles: {}
        Vino: {}
        """.format(self.nombre, self.telas, self.cerveza, self.herramientas, self.pieles, self.vino))

    def eleccion_compra(self):
        print("""Los precios actuales de {} son:
        1- Telas: {}
        2- Cerveza: {}
        3- Herramientas: {}
        4- Pieles: {}
        5- Vino: {}
        """.format(self.nombre, self.telas, self.cerveza, self.herramientas, self.pieles, self.vino))
        eleccion = int(input())
        eleccion = valores_correctos(1, 5, eleccion)



# Pequeña función que comprueba si el valor introducido es correcto, eliminando los bucles en las otras funciones.
def valores_correctos(inicio, final, numero_a_comprobar):
    if inicio <= numero_a_comprobar <= final:
        return numero_a_comprobar
    else:
        while not inicio <= numero_a_comprobar <= final:
            print("Has introducido un valor incorrecto, tus opciones son del {} al {}.".format(inicio, final))
            numero_a_comprobar = int(input())
        return numero_a_comprobar