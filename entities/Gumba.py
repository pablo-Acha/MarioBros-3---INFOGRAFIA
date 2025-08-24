import arcade
import pymunk


class Gumba(arcade.Sprite):
    def __init__(self, personaje,space,path_or_texture = None, scale = 2.9, center_x = 0, center_y = 0, angle = 0):
        super().__init__("assets/images/enemigos/cupa I.png", scale, center_x, center_y, angle)
        self.frame = 0
        self.vacio = False
        self.space = space
        self.personaje = personaje
        self.body_gumba = pymunk.Body(mass=100,moment=1000)    
        self.body_gumba.position = center_x, center_y 
        self.original_x = center_x
        self.original_y = center_y
        self.fondo_x = 0
        self.vida = True
        self.estar_en_espacio = False
        self.animacion_pisado = 0
        self.gumba_box = pymunk.Poly.create_box(self.body_gumba, size=(40, 50))
        self.textures = [
            arcade.load_texture("assets/images/enemigos/cupa I.png"),
            arcade.load_texture("assets/images/enemigos/cupa D.png"),
            arcade.load_texture("assets/images/enemigos/cupa pisado.png")
        ]
        self.sensor_shape = pymunk.Poly.create_box(self.body_gumba, size=(15, 25))  # más pequeño y delgado
        self.sensor_shape.sensor = True  # No afecta físicamente
        self.sensor_shape.offset = (0, 35)  # 30 píxeles arriba del centro del body_gumba



    def soltar_objeto(self):
        if not self.vacio:
            self.vacio = True
    
    def draw(self):
        if (self.vida or self.animacion_pisado>0) and self.estar_en_espacio: 
            self.animacion_pisado-=1
            arcade.draw_sprite(self)
    
    def update(self,fondo_pos_x):
        if self.estar_en_espacio:
            self.fondo_x = fondo_pos_x
            self.detectar_pisada()
            # if self.body_gumba.position.y <150:
            #     self.body_gumba.position = (self.body_gumba.position.x,150)
            self.center_x,self.center_y = self.body_gumba.position
            if self.body_gumba.velocity.y<-200:
                self.body_gumba.velocity = (self.body_gumba.velocity.x,-200) 
            if self.vida:
                self.frame=(self.frame+1)%30
                if self.frame<15:
                    self.texture = self.textures[0]
                elif self.frame < 30:
                    self.texture = self.textures[1]


    def derecha(self):
        self.body.velocity = (+200, self.body.velocity.y)
        

    def izquierda(self):
        self.body.velocity = (-200, self.body.velocity.y)
    
    def morir(self):
        self.vida = False
        self.space.remove(self.body_gumba,self.gumba_box,self.sensor_shape)

    def detectar_pisada(self):
        if self.vida:
            colisiones = self.space.shape_query(self.sensor_shape)
            for col in colisiones:
                if col.shape == self.personaje.hide_box:
                    self.texture = self.textures[2]
                    self.animacion_pisado = 20
                    self.personaje.jump()
                    self.morir()
            
    def agregar_al_espacio(self):
        if self.vida:
            self.space.add(self.body_gumba,self.gumba_box,self.sensor_shape)
            self.estar_en_espacio = True
    def borrar_del_espacio(self):
        if self.vida:
            if self.body_gumba.space is not None:
                self.space.remove(self.body_gumba,self.gumba_box,self.sensor_shape)
                self.estar_en_espacio = False
            