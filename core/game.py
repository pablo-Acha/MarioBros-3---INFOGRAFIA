import arcade
from configuraciones import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.scene = None  # Aquí luego pones SceneManager
    
    def setup(self):
        # Aquí cargamos el primer nivel o menú
        pass

    def on_draw(self):
        self.clear()
        if self.scene:
            self.scene.draw()

    def on_update(self, delta_time):
        if self.scene:
            self.scene.update(delta_time)
