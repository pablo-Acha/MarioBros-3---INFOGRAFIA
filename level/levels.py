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
        self.fondo.left = 0

        self.fondo.center_y = center_y
        
        self.space = pymunk.Space()
        self.space.gravity = (0, -1500)
        
        self.piso_body  = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.piso_body.position = (0,0)
        self.piso_body.elasticity = 0.0
        self.piso_body.friction = 1.0
        self.space.add(self.piso_body)


        self.piso_body_flotante  = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.piso_body_flotante.position = (0,0)
        self.piso_body_flotante.elasticity = 0.0
        self.piso_body_flotante.friction = 1.0
        self.space.add(self.piso_body_flotante)


        self.paredes_body  = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.paredes_body.position = (0,0)
        self.paredes_body.elasticity = 0.0
        self.paredes_body.friction = 1.0
        self.space.add(self.paredes_body)

        self.plataformas =[]
        self.enemigos = []
        self.salto_presionado = False
        self.tiempo_transcurrido_salto = 0
        self.tiempo_presionando_salto = 0

        self.personaje = personaje
        self.space.add(personaje.body,personaje.hide_box)

    def on_draw(self):
        self.clear()
        arcade.draw_sprite(self.fondo) 
        self.personaje.draw()

    def key_release(self,key,modifiers):
        if key == arcade.key.LEFT:
            self.izquierda_presionado = False
            if self.derecha_presionado:
                self.personaje.mover_derecha()
            else:
                self.personaje.stop()
        elif key == arcade.key.RIGHT:
            self.personaje.cambiar_frame_derecha(0,True)
            self.derecha_presionado = False
            if self.izquierda_presionado:
                self.personaje.mover_izquierda()
            else:
                self.personaje.stop()
        elif key == arcade.key.X:
            self.salto_presionado = False
        
    def on_mouse_press(self, x, y, button, modifiers):
        print(f"(self.pivot_x+{x},{y-10})")

    def key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.personaje.direccion_d = False
            self.personaje.direccion_i = True
            self.izquierda_presionado = True
        elif key == arcade.key.RIGHT :                
            self.personaje.direccion_d = True
            self.personaje.direccion_i = False
            self.derecha_presionado = True
        elif key == arcade.key.X and self.tiempo_transcurrido_salto == 0 and self.check_colision_bottom():
            self.personaje.jump()
            self.salto_presionado = True            
            self.tiempo_transcurrido_salto = 0.0001 
            self.personaje.pisando = False

    def update(self,delta_time):
        self.space.step(delta_time)
        self.personaje.update()
        self.boton_presionado(delta_time)
        self.check_colision_bottom()
        if self.tiempo_transcurrido_salto>0 and self.tiempo_transcurrido_salto < 0.05:
            self.personaje.jump()
            self.tiempo_transcurrido_salto+= delta_time
        elif self.tiempo_transcurrido_salto > 0.05 and self.salto_presionado and self.tiempo_transcurrido_salto < 0.1:
            self.personaje.jump()
            self.tiempo_transcurrido_salto += delta_time
        # print(self.tiempo_transcurrido_salto)
        if self.tiempo_transcurrido_salto > 0.05 and not self.salto_presionado:
            self.tiempo_transcurrido_salto = 0

    


    def boton_presionado(self,delt_time):

        if self.izquierda_presionado:
            if self.check_colision_bottom():
                self.personaje.pisando = True
                self.personaje.cambiar_frame_izquierda(1)
            
            if self.personaje.center_x>=150:
                self.personaje.mover_izquierda()
            else:
                self.personaje.body.velocity = (0,self.personaje.body.velocity.y)
                self.fondo.center_x +=5
                self.mover_plataformas(self.fondo.left)
        if self.derecha_presionado:
            if self.check_colision_bottom():
                self.personaje.pisando = True
                self.personaje.cambiar_frame_derecha(1)
            
            if self.personaje.center_x<=300:
                self.personaje.mover_derecha()
            else:
                self.fondo.center_x -=5
                self.personaje.body.velocity = (0,self.personaje.body.velocity.y)
                self.mover_plataformas(self.fondo.left)

    def check_colision_bottom(self):
        colisiones = self.space.shape_query(self.personaje.hide_box)
        for col in colisiones:
            if col.shape != self.personaje.hide_box:
                if col.shape.body == self.piso_body:
                    x,y = self.personaje.body.velocity
                    if abs(y) > 0:
                        self.personaje.body.velocity = (self.personaje.body.velocity.x, 1)
                        # print("yes")
                        # self.personaje.position = (self.personaje.position.x, col.shape.body.position.y+20)
                    return True
        return False or self.check_colision_bottom_flotante()

    def check_colision_bottom_flotante(self):
        colisiones = self.space.shape_query(self.personaje.hide_box)
        for col in colisiones:
            if col.shape != self.personaje.hide_box:
                if col.shape.body == self.piso_body_flotante:
                    x,y = self.personaje.body.velocity
                    if y < 0:
                        self.personaje.body.velocity = (self.personaje.body.velocity.x, 1)
                        col.shape.sensor = False
                    elif y > 0:
                        col.shape.sensor = True
                    return True
        return False



    def evitar_desborde(self):
        pass


    def mover_plataformas(self):
        #plataforma
        pass