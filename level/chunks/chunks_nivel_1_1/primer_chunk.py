from ..Chunk import Chunk
import pymunk
from configuraciones import WIDTH, HEIGHT, TITLE
import arcade
from entities.bloques import Bloques


class Primer_Chunk(Chunk):
    def __init__(self,pivot):
        super().__init__(pivot)


    def agregar_todo(self, space,body_piso):
        self.agregar_bloques(space)
        self.agregar_plataformas(space,body_piso)

    def agregar_bloques(self, space):
        self.lista_bloques = [
            Bloques(center_x = 550,center_y= 310),
            Bloques(center_x = 600,center_y= 310),
            Bloques(center_x = 695,center_y= 455),
            Bloques(center_x = 745,center_y= 455)
        ]
        for bloque in self.lista_bloques:
            space.add(bloque.body_bloque,bloque.bloque_box)

    
    def agregar_plataformas(self, space,piso_body):
        self.lista_plataformas  = [
            pymunk.Segment(piso_body,(-50,100),(WIDTH+500,100),50),
            pymunk.Segment(piso_body, (720,280), (860,280), 5),
            pymunk.Segment(piso_body, (530,280), (625,280), 5),
            pymunk.Segment(piso_body, (530,330), (625,330), 5),
            pymunk.Segment(piso_body, (675,425), (765,425), 5),
            pymunk.Segment(piso_body, (675,475), (765,475), 5),
        ]
        space.add(piso_body,*self.lista_plataformas)

    
    def agregar_enemigos(self, space):
        return super().agregar_enemigos(space)
    
    def update_todo(self):
        for bloque in self.lista_bloques:
            bloque.update()

    def draw_todo(self):
        for bloque in self.lista_bloques:
            bloque.draw()

    def mover_todo(self,pivot_fondo,piso_body):
        x,y = piso_body.position 
        piso_body.position = (self.pivot_x+pivot_fondo,y)
        for bloque in self.lista_bloques:
            xb,yb = bloque.body_bloque.position
            bloque.body_bloque.position = (self.pivot_x+pivot_fondo+bloque.original_x,yb)