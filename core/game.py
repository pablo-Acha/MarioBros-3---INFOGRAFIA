import arcade
from configuraciones import WIDTH, HEIGHT, TITLE
from level.level1_1 import Level1
from entities.player import Player


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.personaje = None
        self.escena = None
        self.esta_en_menu = False 
        self.esta_en_nivel = True  
        self.izquierda_presionado = False
        self.derecha_presionado = False
        self.setup()

    def setup(self):
        self.personaje = self.setPersonaje() 
        self.escena = Level1("level_1_1")  
    

    def setPersonaje(self):
        return Player(path_or_texture="assets/images/mario.png",center_x=10,center_y=100)

    def on_draw(self):
        self.clear()
        if self.escena:
            self.escena.on_draw()
            self.personaje.draw()

    def on_key_press(self, key, modifiers):  
        if self.esta_en_nivel:
            if key == arcade.key.LEFT:
                self.izquierda_presionado = True
            if key == arcade.key.RIGHT :                
                self.derecha_presionado = True




    def on_key_release(self, key, modifiers):
        if self.esta_en_nivel:
            if key == arcade.key.LEFT:
                self.izquierda_presionado = False
                if self.derecha_presionado:
                    self.personaje.mover_derecha()
                else:
                    self.personaje.stop()
            elif key == arcade.key.RIGHT:
                self.derecha_presionado = False
                if self.izquierda_presionado:
                    self.personaje.mover_izquierda()
                else:
                    self.personaje.stop()




    def on_update(self, delta_time):
        if self.escena:
            # self.escena.on_update(delta_time)
            self.personaje.update()
            self.boton_presionado(delta_time)
            

    def boton_presionado(self,delt_time):
        if self.izquierda_presionado:
            self.personaje.mover_izquierda()
        
        if self.derecha_presionado:
            self.personaje.mover_derecha()
