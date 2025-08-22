import arcade
import pymunk


class Bloques(arcade.Sprite):
    def __init__(self, path_or_texture = None, scale = 2.9, center_x = 0, center_y = 0, angle = 0):
        super().__init__("assets/images/Items/bloque item 1.png", scale, center_x, center_y, angle)
        self.frame = 0
        self.vacio = False
        self.body_bloque = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.body_bloque.position = center_x, center_y 
        self.original_x = center_x
        self.original_y = center_y
        self.bloque_box = pymunk.Poly.create_box(self.body_bloque, size=(30, 50))
        self.textures = [
            arcade.load_texture("assets/images/Items/bloque item 1.png"),
            arcade.load_texture("assets/images/Items/bloque item 2.png"),
            arcade.load_texture("assets/images/Items/bloque item 3.png"),
            arcade.load_texture("assets/images/Items/bloque item vacio.png")
        ]

    def soltar_objeto(self):
        if not self.vacio:
            self.vacio = True
    

    def draw(self):
        arcade.draw_sprite(self)
    
    def update(self):
        self.center_x,self.center_y = self.body_bloque.position
        if self.vacio:
            self.texture = self.textures[3]
        else:
            self.frame=(self.frame+1)%30
            if self.frame<10:
                self.texture = self.textures[0]
            elif self.frame < 20:
                self.texture = self.textures[2]
            else:
                self.texture = self.textures[1]

