import arcade
import pymunk


class Bloques(arcade.Sprite):
    def __init__(self, path_or_texture = None, scale = 2.9, center_x = 0, center_y = 0, angle = 0):
        super().__init__("assets/images/Items/bloque item 1.png", scale, center_x, center_y, angle)
        self.frame = 0
        self.vacio = False
        self.body_bloque = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.body_bloque.position = center_x, center_y-22
        self.original_x = center_x
        self.original_y = center_y-22
        self.bloque_box = pymunk.Poly.create_box(self.body_bloque, size=(40, 22))
        self.linea_costado_iz = pymunk.Segment(self.body_bloque, (center_x-20,center_y+22), (center_x-20,center_y-22), 10)
        self.linea_costado_der = pymunk.Segment(self.body_bloque, (center_x+10,center_y+22), (center_x+10,center_y-22), 10)
        self.textures = [
            arcade.load_texture("assets/images/Items/bloque item 1.png"),
            arcade.load_texture("assets/images/Items/bloque item 2.png"),
            arcade.load_texture("assets/images/Items/bloque item 3.png"),
            arcade.load_texture("assets/images/Items/bloque item vacio.png")
        ]
        self.lista_shapes = [self.bloque_box,self.linea_costado_iz,self.linea_costado_der]

    def soltar_objeto(self):
        if not self.vacio:
            self.vacio = True
    

    def draw(self):
        arcade.draw_sprite(self)
        x,y = self.body_bloque.position
        y+=22
        arcade.draw_polygon_outline([(x-20,y+22),(20+x,y+22)
                             ,(x+20,y-22),(x-20,y-22)],arcade.color.BLACK)    
        arcade.draw_line(x-20,y+22, x-20,y-22,arcade.color.BLUE,10)               # plataforma 1

    
    def update(self,space,personaje_shape):
        self.salto(space,personaje_shape)
        self.center_x,self.center_y = self.body_bloque.position.x,self.body_bloque.position.y+22
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

    def salto(self,space,personaje_shape):
        # verificar colision con perosonaje si existe cambie a estado vacio
        if not self.vacio:
            colisiones = space.shape_query(self.bloque_box)
            for col in colisiones:
                if col.shape == personaje_shape:
                    self.vacio = True

        