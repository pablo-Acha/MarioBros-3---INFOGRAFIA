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
        self.setup()

    def setup(self):
        self.personaje = self.setPersonaje() 
        self.escena = Level1(extension_imagen = "png",personaje = self.personaje)  
    

    def setPersonaje(self):
        return Player(path_or_texture="assets/images/mario.png",scale = 3,center_x=200,center_y=500)

    def on_draw(self):
        self.clear()
        if self.escena:
            self.escena.on_draw()

    def on_key_press(self, key, modifiers):  
        if self.esta_en_nivel:
            self.escena.key_press(key,modifiers)

    def on_key_release(self, key, modifiers):
        if self.esta_en_nivel:
            self.escena.key_release(key,modifiers)


    def on_update(self, delta_time):
        if self.escena:
            self.escena.update(delta_time)
