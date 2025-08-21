import arcade
import pymunk
class Player(arcade.Sprite):
    
    def __init__(self, path_or_texture = None, scale = 1, center_x = 0, center_y = 0, angle = 0, **kwargs):
        super().__init__("assets/images/Mario/Mario base D.png", scale, center_x, center_y, angle, **kwargs)
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = 0
        self.change_y = 0


        self.textures = [
            arcade.load_image("assets/images/Mario/Mario base D.png"),
            arcade.load_image("assets/images/Mario/Mario base 2 D.png"),
        ]
        
        # Configuración del cuerpo principal en pymunk
        self.body = pymunk.Body(mass=80, moment=800)    
        self.body.position = center_x, center_y 

        # Shape principal
        self.hide_box = pymunk.Poly.create_box(self.body, size=(30, 60))
        self.hide_box.elasticity = 0.2
        self.hide_box.friction = 0.5

        # Segmento superior (en el MISMO body)
        self.top_segment = pymunk.Segment(self.body, (-15, 30), (15, 30), 2)
        self.top_segment.elasticity = 0.3
        self.top_segment.friction = 0.7

        # Segmento inferior (en el MISMO body)  
        self.bottom_segment = pymunk.Segment(self.body, (-15, -30), (15, -30), 2)
        self.bottom_segment.elasticity = 0.1
        self.bottom_segment.friction = 1.0




    def draw(self):         
        # super().draw()
        arcade.draw_sprite(self)
        arcade.draw_polygon_outline([(self.center_x+15,self.center_y+15),(self.center_x-15,self.center_y+15)
                                     ,(self.center_x-15,self.center_y-15),(self.center_x+15,self.center_y-15)],arcade.color.RED)    

    def update(self, delta_time = 1 / 60):
        self.center_x = self.body.position.x
        self.center_y = self.body.position.y



    def jump(self):
        self.body.velocity = (self.body.velocity.x, 300)

    def mover_izquierda(self):
        self.body.velocity = (-200, self.body.velocity.y)

    def mover_derecha(self):
        self.body.velocity = (200, self.body.velocity.y)

    def stop(self):
        self.body.velocity = (0, self.body.velocity.y)