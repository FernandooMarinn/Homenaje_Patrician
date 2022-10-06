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
        1- Telas: {}
        2- Cerveza: {}
        3- Herramientas: {}
        4- Pieles: {}
        5- Vino: {}
        """.format(self.nombre, self.telas, self.cerveza, self.herramientas, self.pieles, self.vino))




# Se definen las ciudades y se inicializan sus precios.
# Lubeck produce algo de vino, y herramientas.
Lubeck = Ciudad(1400, 1000, 450, 250, 70, 45, 290, 200, 420, 300, "Lubeck")
# Stettin produce cerveza.
Stettin = Ciudad(1400, 1000, 450, 250, 42, 32, 400, 280, 420, 300, "Stettin")
# Malmo produce telas y pieles.
Malmo = Ciudad(1100, 700, 450, 250, 70, 45, 400, 280, 300, 200, "Malmo")
# Rostock compra de todo.
Rostock = Ciudad(1400, 1000, 450, 250, 70, 45, 400, 280, 420, 300, "Rostock")
# Gdanks compra telas, vino, y herramientas. Vende cerveza.
Gdanks = Ciudad(1400, 1000, 450, 250, 43, 32, 400, 280, 420, 300, "Gdanks")