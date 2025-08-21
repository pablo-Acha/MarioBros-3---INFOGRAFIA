from .levels import Level
import pymunk
from configuraciones import WIDTH, HEIGHT, TITLE
import arcade


class Level1(Level):
    def __init__(self, personaje, extension_imagen = "png",left=0, center_y=450):
        super().__init__("level_1_1",personaje,extension_imagen,left, center_y)
        self.enemigos =  self.setEnemigos()
        self.plataformas =  self.setPlataformas()
        
        #codigo temporal 
        self.piso_body  = self.space.static_body
        #                                           x1,y1      x2,     y2
        self.piso = pymunk.Segment(self.piso_body,(-50,150),(WIDTH+50,150),10)
        

        

        #
        self.space.add(self.piso)


    def setEnemigos(self):
        #crear enemigos
        pass
    
    def setPlataformas(self):
        #crear Plataformas
        pass

    def on_draw(self):
        super().on_draw()    
        arcade.draw_polygon_outline([(-50,150),(WIDTH+50,150)
                             ,(WIDTH+50,100),(-50,100)],arcade.color.BLACK)    

    def update(self, delta_time):
        super().update(delta_time)
        if self.fondo.left <= -500:
            pass 
        if self.fondo.left <= -1000:
            pass