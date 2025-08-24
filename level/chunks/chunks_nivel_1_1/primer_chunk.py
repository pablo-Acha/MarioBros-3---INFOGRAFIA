from ..Chunk import Chunk
import pymunk
from configuraciones import WIDTH, HEIGHT, TITLE
import arcade
from entities.bloques import Bloques
from entities.Gumba import Gumba


class Primer_Chunk(Chunk):
    def __init__(self,pivot,personaje,space):
        super().__init__(pivot,personaje,space)


    def agregar_todo(self, space,body_piso):
        self.agregar_bloques(self.space)
        self.agregar_plataformas(space,body_piso)
        self.agregar_enemigos(space)

    def agregar_bloques(self, space):
        self.lista_bloques = [
            Bloques("moneda",self.space,self.personaje,center_x = 550,center_y= 310),
            Bloques("moneda",self.space,self.personaje,center_x = 600,center_y= 310),
            Bloques("moneda",self.space,self.personaje,center_x = 695,center_y= 455),
            Bloques("moneda",self.space,self.personaje,center_x = 745,center_y= 455)
        ]
        for bloque in self.lista_bloques:
            bloque.unirse_al_espacio()

    
    def agregar_plataformas(self, space,piso_body):
        self.lista_plataformas  = [
            pymunk.Segment(piso_body,(-50,100),(2000,100),50),
            pymunk.Segment(piso_body, (720,280), (860,280), 10),
            # pymunk.Segment(piso_body, (530,280), (625,280), 5),
            pymunk.Segment(piso_body, (530,330), (625,330), 10),
            # pymunk.Segment(piso_body, (675,425), (765,425), 5),
            pymunk.Segment(piso_body, (675,475), (765,475), 10),
        ]
        space.add(piso_body,*self.lista_plataformas)

    
    def agregar_enemigos(self, space):
        self.lista_gumbas = [
            Gumba(self.personaje,self.space,center_x=450,center_y=225)            
        ]
        for gumbas in self.lista_gumbas:
            gumbas.agregar_al_espacio()

    def update_todo(self,fondo,space,personaje_hide_box):
        for bloque in self.lista_bloques:
            bloque.update(space,personaje_hide_box)

        for enemigo in self.lista_gumbas:
            enemigo.update(fondo)

    def draw_todo(self):
        for bloque in self.lista_bloques:
            bloque.draw()
        for enemigo in self.lista_gumbas:
            enemigo.draw()

    def mover_todo(self,pivot_fondo,piso_body):
        x,y = piso_body.position 
        piso_body.position = (self.pivot_x+pivot_fondo,y)
        for bloque in self.lista_bloques:
            xb,yb = bloque.body_bloque.position
            bloque.body_bloque.position = (self.pivot_x+pivot_fondo+bloque.original_x,yb)
        for enemigo in self.lista_gumbas:
            xb,yb = enemigo.body_gumba.position
            # enemigo.original_x = xb
            a =xb + pivot_fondo-enemigo.fondo_x 
            enemigo.body_gumba.position = (
               a,
               yb
            )