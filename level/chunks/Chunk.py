import pymunk
from configuraciones import WIDTH, HEIGHT, TITLE
import arcade
from entities.bloques import Bloques

class Chunk():
    def __init__(self,pivot):
        self.pivot_x  = pivot
        self.lista_bloques = []
        self.lista_plataformas = []
        self.lista_enemigos = []
        self.lista_todo = []

    def eliminar_todo(self,space):
        space.remove()

    def agregar_todo(self,space):
        pass

    def agregar_bloques(self,space):
        pass

    def agregar_plataformas(self,space):
        pass

    def agregar_enemigos(self,space):
        pass