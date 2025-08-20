import arcade
class Player(arcade.Sprite):
    
    def __init__(self, path_or_texture = None, scale = 1, center_x = 0, center_y = 0, angle = 0, **kwargs):
        super().__init__(path_or_texture, scale, center_x, center_y, angle, **kwargs)
    
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = 0
        self.change_y = 0
        
        self.speed = 5
        self.jump_strength = 15
        self.gravity = 0.8
        self.is_on_ground = False


    def draw(self):         
        arcade.draw_polygon_outline([(self.center_x+50,self.center_y+50),(self.center_x-50,self.center_y+50)
                                     ,(self.center_x-50,self.center_y-50),(self.center_x+50,self.center_y-50)],arcade.color.AERO_BLUE)    


    def update(self, delta_time = 1 / 60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        

    
    def jump(self):
        if self.is_on_ground:
            self.change_y = self.jump_strength
            self.is_on_ground = False
            self.is_jumping = True

    def mover_izquierda(self):
        self.change_x = -self.speed

    def mover_derecha(self):
        self.change_x = self.speed

    def stop(self):
        self.change_x = 0