import arcade
class Player:
    def __init__(self,pos_init_x, pos_init_y):
        self.x = pos_init_x
        self.y = pos_init_y
        self.vertices = [(self.x+20,self.y+30),(self.x-20,self.y+30),
                         (self.x-20,self.y-30),(self.x+20,self.y-30)]

    def draw(self):
        arcade.draw_polygon_outline(self.vertices, arcade.color.AERO_BLUE, 5)


