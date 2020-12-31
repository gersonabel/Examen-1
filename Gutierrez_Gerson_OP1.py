"""
importamos las librerias necesarias
"""

import time
import numpy as np
import sys

"""
con esta funcion las letras saldran como animacion 
"""

def imprimir_lento(s):

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

#creamos la clase pokemon con la cual trabajaremos
class Pokemon:

    # incializamos para tener los atributos del pokemon
    def __init__(self, nombre, tipo, movim, EVs, vida='==================='):
        # save variables as attributes
        self.nombre = nombre
        self.tipo = tipo
        self.movim = movim
        self.ataque = EVs['ATAQUE']
        self.defensa = EVs['DEFENSA']
        self.vida = vida
        self.barras = 40 # Amount of health bars

    #la funcion con la cual se da la batalla
    def lucha(self, Pokemon2):
        # Allow two pokemon to fight each other

        # Print fight information
        print("-----BATALLA POKEMON-----")
        print(f"\n{self.nombre}")
        print("TIPO/", self.tipo)
        print("ATAQUE/", self.ataque)
        print("DEFENSA/", self.defensa)
        print("LVL/", 3*(1+np.mean([self.ataque,self.defensa])))
        print("\nVS")
        print(f"\n{Pokemon2.nombre}")
        print("TIPO/", Pokemon2.tipo)
        print("ATAQUE/", Pokemon2.ataque)
        print("DEFENSA/", Pokemon2.defensa)
        print("LVL/", 3*(1+np.mean([Pokemon2.ataque,Pokemon2.defensa])))

        time.sleep(2)

        # se considera el tipo de pokemon, para poder tener en cuenta los daños
        version = ['fuego', 'agua', 'planta']
        for i,k in enumerate(version):
            if self.tipo == k:
                # cuando son del mismo tipo
                if Pokemon2.tipo == k:
                    cadena1 = '\nno fue efectivo...\n'
                    cadena2 = '\nno fue efectivo...\n'


                # Pokemon2 es fuerte
                if Pokemon2.tipo == version[(i+1)%3]:
                    Pokemon2.ataque *= 2
                    Pokemon2.defensa *= 2
                    self.ataque /= 2
                    self.defensa /= 2
                    cadena1 = '\nno fue efectivo...\n'
                    cadena2 = '\nes super efectivo!\n'


                # Pokemon2 es debil
                if Pokemon2.tipo == version[(i+2)%3]:
                    self.ataque *= 2
                    self.defensa *= 2
                    Pokemon2.ataque /= 2
                    Pokemon2.defensa /= 2
                    cadena1 = '\nes super efectivo!\n'
                    cadena2 = '\nno fue efectivo...\n'


        """
        con este bucle podremos dar la animacion del juego hasta
        que algun pokemon se quede sin vida.
        """
        while (self.barras > 0) and (Pokemon2.barras > 0):
            # Print the health of each pokemon
            print(f"\n{self.nombre}\t\tvida\t{self.vida}")
            print(f"{Pokemon2.nombre}\t\tvida\t{Pokemon2.vida}\n")

            print(f"adelante {self.nombre}!")
            for i, x in enumerate(self.movim):
                print(f"{i+1}.", x)
            index = int(input('elija su movimiento: '))
            imprimir_lento(f"\n{self.nombre} usó {self.movim[index-1]}!")
            time.sleep(1)
            imprimir_lento(cadena1)

            # Determine daño
            Pokemon2.barras -= self.ataque
            Pokemon2.vida = ""

            #nos dice el estado de las barras conforme al daño recibido
            for j in range(int(Pokemon2.barras+.1*Pokemon2.defensa)):
                Pokemon2.vida += "="

            time.sleep(1)
            print(f"\n{self.nombre}\t\tvida\t{self.vida}")
            print(f"{Pokemon2.nombre}\t\tvida\t{Pokemon2.vida}\n")
            time.sleep(.5)

            # revisa la cantidad de vida, y enc caso sea 0 finaliza la batalla
            if Pokemon2.barras <= 0:
                imprimir_lento("\n..." + Pokemon2.nombre + ' se debilitó.\n')
                break

            # turno del segundo pokemon

            print(f"Adelante {Pokemon2.nombre}!")
            for i, x in enumerate(Pokemon2.movim):
                print(f"{i+1}.", x)
            index = int(input('elija su movimiento: '))
            imprimir_lento(f"\n{Pokemon2.nombre} usó {Pokemon2.movim[index-1]}!")
            time.sleep(1)
            imprimir_lento(cadena2)

            self.barras -= Pokemon2.ataque
            self.vida = ""

            for j in range(int(self.barras+.1*self.defensa)):
                self.vida += "="

            time.sleep(1)
            print(f"{self.nombre}\t\tvida\t{self.vida}")
            print(f"{Pokemon2.nombre}\t\tvida\t{Pokemon2.vida}\n")
            time.sleep(.5)

            if self.barras <= 0:
                imprimir_lento("\n..." + self.nombre + ' se debilitó.\n')
                break

        money = np.random.choice(5000)
        imprimir_lento(f"\nganó ${money}.\n")

if __name__ == '__main__':

    #Creamos todos los pokemons que creeemos teniendo en cuenta este formato
    # pokemon = pokemon(nombre, tipo, [ataques(#)],[ataque:#, defensa:#] )

    Charizard = Pokemon('Charizard', 'fuego', ['Flama de fuego', 'volar', 'tacleada', 'puño de fuego', 'golpe dragon'], {'ATAQUE':12, 'DEFENSA': 8})
    Blastoise = Pokemon('Blastoise', 'agua', ['chorro de agua', 'Burbuja gigante', 'Hydro golpe', 'marea alta'],{'ATAQUE': 10, 'DEFENSA':10})
    Venusaur = Pokemon('Venusaur', 'planta', ['latigo cepa', 'hoja cortante', 'hiedra venenosa', 'enredadera'],{'ATAQUE':8, 'DEFENSA':12})

    # designamos el pokemon con el que lucharemos
    # y con el que nos enfrentamos.

    Charizard.lucha(Venusaur)