import arcade
import pymunk
# from ..configuraciones import WIDTH, HEIGHT, TITLE



class Level(arcade.View):
    def __init__(self,nombre_imagen,extension_imagen = "png",left = 0,center_y = 450):
        super().__init__()
        self.x = 0
        self.y = 0
        self.sprite = arcade.Sprite(f"./assets/images/levels/{nombre_imagen}.{extension_imagen}",scale=3)
        self.sprite.left = left
        self.sprite.center_y = center_y
    
    def on_draw(self):
        self.clear()
        arcade.draw_sprite(self.sprite) 



# def main():
#     window = arcade.Window(WIDTH, HEIGHT,TITLE)
#     game = Level()
#     window.show_view(game)
#     arcade.run()


# if __name__ == "__main__":
#     main()
    