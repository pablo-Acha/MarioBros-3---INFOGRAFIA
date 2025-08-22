import arcade
import pymunk


class Gumba(arcade.Sprite):
    def __init__(self, path_or_texture = None, scale = 2.9, center_x = 0, center_y = 0, angle = 0):
        super().__init__("assets/images/enemigos/cupa I.png", scale, center_x, center_y, angle)
        self.frame = 0
        self.vacio = False
        self.body_gumba = pymunk.Body(mass=100,moment=1000)    
        self.body_gumba.position = center_x, center_y 
        self.original_x = center_x
        self.original_y = center_y
        self.fondo_x = 0
        self.gumba_box = pymunk.Poly.create_box(self.body_gumba, size=(30, 50))
        self.textures = [
            arcade.load_texture("assets/images/enemigos/cupa I.png"),
            arcade.load_texture("assets/images/enemigos/cupa D.png"),
            arcade.load_texture("assets/images/enemigos/cupa pisado.png")
        ]

    def soltar_objeto(self):
        if not self.vacio:
            self.vacio = True
    
    def draw(self):
        arcade.draw_sprite(self)
    
    def update(self,fondo_pos_x):
        self.fondo_x = fondo_pos_x
        if self.body_gumba.position.y <150:
            self.body_gumba.position = (self.body_gumba.position.x,150)
        self.center_x,self.center_y = self.body_gumba.position
        self.frame=(self.frame+1)%30
        if self.frame<15:
            self.texture = self.textures[0]
        elif self.frame < 30:
            self.texture = self.textures[1]


    def derecha(self):
        self.body.velocity = (+200, self.body.velocity.y)
        

    def izquierda(self):
        self.body.velocity = (-200, self.body.velocity.y)
