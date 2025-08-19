from .levels import Level
import pymunk

class Level1(Level):
    def __init__(self, nombre_imagen, extension_imagen = "png",left=0, center_y=450):
        super().__init__(nombre_imagen,extension_imagen,left, center_y)
        self.enemigos =  self.setEnemigos()
        self.obstaculos =  self.setEnemigos()
        self.space = pymunk.Space()
        self.space.gravity = (0, -900)


    def setEnemigos(self):
        #crear enemigos

        pass

    def on_draw(self):

        return super().on_draw()
    