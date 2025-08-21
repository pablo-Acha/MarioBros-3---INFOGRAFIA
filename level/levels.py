import arcade
import pymunk
from configuraciones import WIDTH, HEIGHT, TITLE



class Level(arcade.View):
    def __init__(self,nombre_imagen,personaje,extension_imagen = "png",left = 0,center_y = 450):
        super().__init__()
        self.x = 0
        self.y = 0
        self.izquierda_presionado = False
        self.derecha_presionado = False
        self.fondo = arcade.Sprite(f"./assets/images/levels/{nombre_imagen}.{extension_imagen}",scale=3)
        self.fondo.left = left
        self.fondo.center_y = center_y
        
        self.plataformas =[]
        self.enemigos = []
        #metros recorridos
        self.metros = 0


        #control del salto
        self.salto_presionado = False
        self.tiempo_transcurrido_salto = 0
        self.tiempo_presionando_salto = 0

        self.personaje = personaje
        self.space = pymunk.Space()
        self.space.gravity = (0, -900)
        self.space.add(personaje.body,personaje.hide_box,personaje.bottom_segment,personaje.top_segment)

    def on_draw(self):
        self.clear()
        arcade.draw_sprite(self.fondo) 
        self.personaje.draw()
        # arcade.draw_sprite(self.personaje)

    def key_release(self,key,modifiers):
        if key == arcade.key.LEFT:
            self.izquierda_presionado = False
            if self.derecha_presionado:
                self.personaje.mover_derecha()
            else:
                self.personaje.stop()
        elif key == arcade.key.RIGHT:
            self.derecha_presionado = False
            if self.izquierda_presionado:
                self.personaje.mover_izquierda()
            else:
                self.personaje.stop()
        elif key == arcade.key.X:
            self.salto_presionado = False
        

    def key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.izquierda_presionado = True
        elif key == arcade.key.RIGHT :                
            self.derecha_presionado = True
        elif key == arcade.key.X and self.tiempo_transcurrido_salto == 0 and self.check_colision_bottom():
            self.salto_presionado = True            
            self.tiempo_transcurrido_salto = 0.0001 

    def update(self,delta_time):
        self.space.step(delta_time)
        self.personaje.update()
        self.boton_presionado(delta_time)
        if self.tiempo_transcurrido_salto>0 and self.tiempo_transcurrido_salto < 0.2:
            self.personaje.jump()
            self.tiempo_transcurrido_salto+= delta_time
        elif self.tiempo_transcurrido_salto > 0.2 and self.salto_presionado and self.tiempo_transcurrido_salto < 0.5:
            self.personaje.jump()
            self.tiempo_transcurrido_salto += delta_time
        print(self.tiempo_transcurrido_salto)
        if self.tiempo_transcurrido_salto > 0.2 and not self.salto_presionado:
            self.tiempo_transcurrido_salto = 0

    def boton_presionado(self,delt_time):
        if self.izquierda_presionado:
            if self.personaje.center_x>=150:
                self.personaje.mover_izquierda()
            else:
                self.fondo.center_x +=5
        
        if self.derecha_presionado:
            if self.personaje.center_x<=400:
                self.personaje.mover_derecha()
            else:
                self.fondo.center_x -=5
            ##self.fondo.center_x = 1000


    def check_colision_bottom(self):
        colisiones = self.space.shape_query(self.personaje.bottom_segment)
        for col in colisiones:
            # col.shape es el shape con el que colisionó
            if col.shape != self.personaje.hide_box:
                return True
        return False