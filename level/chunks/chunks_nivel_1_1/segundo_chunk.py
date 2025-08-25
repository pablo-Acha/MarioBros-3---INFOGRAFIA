from ..Chunk import Chunk
import pymunk
from configuraciones import WIDTH, HEIGHT, TITLE
import arcade
from entities.bloques import Bloques
from entities.Gumba import Gumba


class Segundo_Chunk(Chunk):
    def __init__(self,pivot,personaje,space):
        super().__init__(pivot,personaje,space)


    def agregar_todo(self, space,body_piso,body_piso_flotante,body_paredes):
        self.agregar_bloques(self.space)
        self.agregar_plataformas(space,body_piso)
        self.agregar_plataformas_flotantes(space,body_piso_flotante)
        self.agregar_enemigos(space)
        self.agregar_plataformas_paredes(space,body_paredes)

    def agregar_bloques(self, space):
        self.lista_bloques = [
            Bloques("moneda",self.space,self.personaje,center_x = self.pivot_x+270,center_y= 403),
            Bloques("moneda",self.space,self.personaje,center_x = self.pivot_x+991,center_y= 210)
        ]
        for bloque in self.lista_bloques:
            bloque.unirse_al_espacio()

    
    def agregar_plataformas(self, space,piso_body):
        self.lista_plataformas  = [
            pymunk.Segment(piso_body,(self.pivot_x-50,100),(self.pivot_x+2000,100),50),
            pymunk.Segment(piso_body,(self.pivot_x+55,273),(self.pivot_x+146,270),10),
            pymunk.Segment(piso_body,(self.pivot_x+248,418),(self.pivot_x+291,418),10),
            pymunk.Segment(piso_body,(self.pivot_x+968.0,229.0),
(self.pivot_x+999.0,225.0),10)
        ]
        space.add(*self.lista_plataformas)

    def agregar_plataformas_flotantes(self,space,piso_flotante):
        self.lista_plataformas_flotante  = [
            pymunk.Segment(piso_flotante, (self.pivot_x+866.0,130.0),
(self.pivot_x+0.0,130.0), 10),
            pymunk.Segment(piso_flotante, (self.pivot_x+874.0,174.0),
(self.pivot_x+997.0,179.0), 10),
            pymunk.Segment(piso_flotante, (self.pivot_x+539,473), (self.pivot_x+723,473), 10),
            pymunk.Segment(piso_flotante, (self.pivot_x+541,220), (self.pivot_x+820,220), 10),
            pymunk.Segment(piso_flotante, (self.pivot_x+394,377), (self.pivot_x+575,377), 10),            
        ]
        space.add(*self.lista_plataformas_flotante)
    

    def agregar_plataformas_paredes(self,space,body_paredes):
        self.lista_paredes  = [
            pymunk.Segment(body_paredes, (self.pivot_x+151.0,270.0)
,(self.pivot_x+146.0,135.0), 10),
            pymunk.Segment(body_paredes, (self.pivot_x+54.0,274.0)
,(self.pivot_x+58.0,134.0), 10),    
            pymunk.Segment(body_paredes, (self.pivot_x+1000,134.0),
(self.pivot_x+1000,618.0), 100)
        ]

        space.add(*self.lista_paredes)



    def agregar_enemigos(self, space):
        self.lista_gumbas = [
            Gumba(self.personaje,self.space,center_x=self.pivot_x+450,center_y=225)            
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
        # piso_body.position = (self.pivot_x+pivot_fondo,y)
        for bloque in self.lista_bloques:
            xb,yb = bloque.body_bloque.position
            bloque.body_bloque.position = (pivot_fondo+bloque.original_x,yb)
        for enemigo in self.lista_gumbas:
            xb,yb = enemigo.body_gumba.position
            a =xb + pivot_fondo-enemigo.fondo_x 
            enemigo.body_gumba.position = (
               a,
               yb
            )