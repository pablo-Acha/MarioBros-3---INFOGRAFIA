import pymunk
from configuraciones import WIDTH, HEIGHT, TITLE
import arcade
from entities.bloques import Bloques

class Chunk():
    def __init__(self,pivot,personaje,space):
        self.pivot_x  = pivot
        self.space = space
        self.personaje = personaje
        self.lista_bloques = []
        self.lista_plataformas = []
        self.lista_gumbas = []
        self.lista_todo = []

    def eliminar_todo(self,space):
        if len(self.lista_bloques)>0:
            for bloque in self.lista_bloques:
                if bloque.estar_en_espacio:
                    bloque.borrar_del_espacio()
            # self.lista_bloques = []

        if len(self.lista_plataformas)>0:
            if self.lista_plataformas[0].body.space is not None:
                space.remove(self.lista_plataformas[0].body,*self.lista_plataformas)
            
            # self.lista_plataformas = []

        if len(self.lista_gumbas)>0:
            for gumbas in self.lista_gumbas:
                gumbas.borrar_del_espacio()

    def agregar_todo(self,space):
        pass

    def agregar_bloques(self,space):
        pass

    def agregar_plataformas(self,space):
        pass

    def agregar_enemigos(self,space):
        pass