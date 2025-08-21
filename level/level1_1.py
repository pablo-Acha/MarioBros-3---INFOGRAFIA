from .levels import Level
import pymunk
from configuraciones import WIDTH, HEIGHT, TITLE
import arcade


class Level1(Level):
    def __init__(self, personaje, extension_imagen = "png",left=0, center_y=450):
        super().__init__("level_1_1",personaje,extension_imagen,left, center_y)
        self.enemigos =  self.setEnemigos()
        self.plataformas =  self.setPlataformas()
        
        #codigo temporal 
        self.piso_body  = self.space.static_body
        # Piso principal
        self.piso = pymunk.Segment(self.piso_body,(-50,100),(WIDTH+50,100),50)

        # =======================
        # MUROS EXTRA
        # =======================
        # Muro izquierdo
        #self.muro_izq = pymunk.Segment(self.piso_body, (150,300), (300,150), 10)
        # Muro derecho
        #self.muro_der = pymunk.Segment(self.piso_body, (WIDTH,150), (WIDTH,400), 10)
        # Plataforma flotante
        self.plataforma_1 = pymunk.Segment(self.piso_body, (720,280), (860,280), 3)
        # Otra plataforma más alta
        self.plataforma_2 = pymunk.Segment(self.piso_body, (530,280), (625,280), 3)
        self.plataforma_3 = pymunk.Segment(self.piso_body, (530,330), (625,330), 3)
        self.plataforma_4 = pymunk.Segment(self.piso_body, (530,425), (625,425), 3)
        self.plataforma_5 = pymunk.Segment(self.piso_body, (530,475), (625,475), 3)


        # Añadir todos los muros al espacio
        self.space.add(self.piso, self.plataforma_1, self.plataforma_2, self.plataforma_3, self.plataforma_4, self.plataforma_5)


    def setEnemigos(self):
        #crear enemigos
        pass
    
    def setPlataformas(self):
        #crear Plataformas
        pass

    def on_draw(self):
        super().on_draw()    
        # Piso
        arcade.draw_polygon_outline([(-50,150),(WIDTH+50,150)
                             ,(WIDTH+50,100),(-50,100)],arcade.color.BLACK)    

        # Dibujar muros extra
        #arcade.draw_line(0,150,0,400,arcade.color.BRICK_RED,3)              # muro izq
        #arcade.draw_line(WIDTH,150,WIDTH,400,arcade.color.BRICK_RED,3)      # muro der
        arcade.draw_line(720,280,860,280,arcade.color.BLUE,3)               # plataforma 1
        arcade.draw_line(530,280,625,280,arcade.color.GREEN,3)              # plataforma 2
        arcade.draw_line(530,330,625,330,arcade.color.PURPLE,3)              # plataforma 3
        arcade.draw_line(530,425,625,425,arcade.color.PURPLE,3)              # plataforma 4
        arcade.draw_line(530,475,625,475,arcade.color.PURPLE,3)              # plataforma 5
        for i in range(0,800,50):
            arcade.draw_line(0,i,WIDTH,i,arcade.color.RED,3)              # plataforma 2


    def update(self, delta_time):
        super().update(delta_time)



# ==================================================
# ANIMACIÓN DE MARIO: CAMINATA Y SALTO
# ==================================================

# class Mario(arcade.Sprite):
#     def __init__(self):
#         # Textura inicial (parado)
#         super().__init__("assets/images/Mario/Mario base D.png", scale=2.5)

#         # Estado
#         self.facing_right = True
#         self.is_jumping = False
#         self._anim_index = 0
#         self._anim_timer = 0.0

#         # Cargar texturas de idle
#         self.idle_right = arcade.load_texture("assets/images/Mario/Mario base D.png")
#         self.idle_left = arcade.load_texture("assets/images/Mario/Mario base I.png", flipped_horizontally=True)

#         # Cargar texturas de caminar
#         self.walk_right = [arcade.load_texture(f"assets/images/Mario/Mario base 2 D{i}.png") for i in range(1,4)]
#         self.walk_left = [arcade.load_texture(f"assets/images/Mario/Mario base 2 I{i}.png", flipped_horizontally=True) for i in range(1,4)]

#         # Cargar texturas de salto
#         self.jump_right = arcade.load_texture("assets/images/Mario/Mario base salto.png")
#         self.jump_left = arcade.load_texture("assets/images/Mario/Marios base salto.png", flipped_horizontally=True)




#     def update_animation(self, delta_time: float = 1/60):
#         # Orientación
#         if self.change_x > 0:
#             self.facing_right = True
#         elif self.change_x < 0:
#             self.facing_right = False

#         # Animación de salto
#         if self.is_jumping:
#             self.texture = self.jump_right if self.facing_right else self.jump_left
#             return

#         # Animación idle si no se mueve
#         if abs(self.change_x) < 0.1:
#             self.texture = self.idle_right if self.facing_right else self.idle_left
#             return

#         # Animación de caminar
#         self._anim_timer += delta_time
#         if self._anim_timer >= 0.12:
#             self._anim_timer = 0
#             self._anim_index = (self._anim_index + 1) % len(self.walk_right)

#         if self.facing_right:
#             self.texture = self.walk_right[self._anim_index]
#         else:
#             self.texture = self.walk_left[self._anim_index]
