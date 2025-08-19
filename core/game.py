import arcade
from configuraciones import WIDTH, HEIGHT, TITLE
from level.level1_1 import Level1


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)

        #deberia iniciar con el menu pero por ahora que sea solo el primer mundo
        self.scene = Level1("level_1_1")  
    
    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        if self.scene:
            self.scene.on_draw()

    def on_update(self, delta_time):
        if self.scene:
            self.scene.on_update(delta_time)
