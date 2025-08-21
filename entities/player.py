import arcade
import pymunk
class Player(arcade.Sprite):
    
    def __init__(self, path_or_texture = None, scale = 1, center_x = 0, center_y = 0, angle = 0, **kwargs):
        super().__init__("assets/images/Mario/Mario base D.png", scale, center_x, center_y, angle, **kwargs)
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = 0
        self.change_y = 0
        self.direccion_d = True
        self.direccion_i = False
        self.pisando = True
        self.frame_i = 0; 
        self.frame_d = 0; 

        self.textures = [
            arcade.load_texture("assets/images/Mario/Mario base D.png"),
            arcade.load_texture("assets/images/Mario/Mario base 2 D.png"),
            arcade.load_texture("assets/images/Mario/Mario base I.png"),
            arcade.load_texture("assets/images/Mario/Mario base 2 I.png"),
            arcade.load_texture("assets/images/Mario/Mario base salto D.png"),
            arcade.load_texture("assets/images/Mario/Mario base salto I.png"),
        ]
        # Configuración del cuerpo principal en pymunk
        self.body = pymunk.Body(mass=80, moment=800)    
        self.body.position = center_x, center_y 

        # Shape principal
        self.hide_box = pymunk.Poly.create_box(self.body, size=(30, 60))
        self.hide_box.elasticity = 0.2
        self.hide_box.friction = 0.5

        # # Segmento superior (en el MISMO body)
        # self.top_segment = pymunk.Segment(self.body, (-15, 30), (15, 30), 2)
        # self.top_segment.elasticity = 0.3
        # self.top_segment.friction = 0.7

        # # Segmento inferior (en el MISMO body)  
        # self.bottom_segment = pymunk.Segment(self.body, (-15, -30), (15, -30), 2)
        # self.bottom_segment.elasticity = 0.1
        # self.bottom_segment.friction = 1.0

    def cambiar_frame_salto(self,frame = 1):
        if self.direccion_d:
            self.texture = self.textures[4]
        else:
            self.texture = self.textures[5]
                

    def cambiar_frame_derecha(self,frame = 1,forzar = False):
        
        if not self.pisando:
            self.cambiar_frame_salto()
        elif not forzar:
            self.frame_d=(self.frame_d+frame)%4
            if self.frame_d <2: 
                self.texture = self.textures[0]
            else :
                self.texture = self.textures[1]
        else:
            self.texture = self.textures[0]


    def cambiar_frame_izquierda(self,frame = 1,forzar = False):
        if not self.pisando:
            self.cambiar_frame_salto()
        elif not forzar:
            self.frame_i=(self.frame_i+frame)%4
            if self.frame_i <2: 
                self.texture = self.textures[2]
            else :
                self.texture = self.textures[3]
        else:
            self.texture = self.textures[2]
        


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
        self.pisando = False
        self.cambiar_frame_salto()

    def mover_izquierda(self):
        self.body.velocity = (-200, self.body.velocity.y)

    def mover_derecha(self):
        self.body.velocity = (200, self.body.velocity.y)

    def stop(self):
        self.body.velocity = (0, self.body.velocity.y)