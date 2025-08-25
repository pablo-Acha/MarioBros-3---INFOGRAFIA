import arcade
import pymunk


class Bloques(arcade.Sprite):
    def __init__(self, item,space,personaje,path_or_texture = None, scale = 2.9, center_x = 0, center_y = 0, angle = 0):
        super().__init__("assets/images/Items/bloque item 1.png", scale, center_x, center_y, angle)
        self.frame = 0
        self.vacio = False
        self.item =item
        self.space = space
        self.personaje = personaje
        self.hay_item = True
        self.tiempo_moneda = 0
        self.body_bloque = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.body_bloque.position = center_x, center_y-22
        self.original_x = center_x
        self.original_y = center_y
        self.estar_en_espacio = False
        self.moneda = arcade.Sprite("assets/images/Items/moneda base.png",scale=2.5)
        self.moneda.center_x,self.moneda.center_y = (self.center_x,self.center_y+24)
        
        self.bloque_box = pymunk.Poly.create_box(self.body_bloque, size=(45, 44))
        self.linea_costado_iz = pymunk.Segment(self.body_bloque,(-20,+22),(-20,-22),10)
        self.linea_costado_iz.sensor = True
        self.linea_costado_der = pymunk.Segment(self.body_bloque,(20,+22),(20,-22),10)
        self.linea_costado_der.sensor = True
        # # self.linea_costado_der.offset = (100, 0)
        self.sensor_bloque = pymunk.Segment(self.body_bloque,(-15,-22),(15,-22),10)
        self.sensor_bloque.sensor = True
        self.textures = [
            arcade.load_texture("assets/images/Items/bloque item 1.png"),
            arcade.load_texture("assets/images/Items/bloque item 2.png"),
            arcade.load_texture("assets/images/Items/bloque item 3.png"),
            arcade.load_texture("assets/images/Items/bloque item vacio.png")
        ]
        self.lista_shapes = [self.bloque_box,self.sensor_bloque,self.linea_costado_iz]

    def soltar_objeto(self):
        if self.hay_item and self.vacio:
            self.hay_item = False
            if self.item == "moneda":
                self.tiempo_moneda = 8
            elif self.item == "hongo":
                pass

    def draw(self):
        if self.body_bloque.space is not None:
            arcade.draw_sprite(self)
            if self.tiempo_moneda>0:
                self.tiempo_moneda-=1
                self.moneda.center_x,self.moneda.center_y = (self.center_x,self.center_y+44)
                arcade.draw_sprite(self.moneda)

            x,y = self.body_bloque.position
            y+=22
        # arcade.draw_polygon_outline([(x-20,y+22),(20+x,y+22)
        #                      ,(x+20,y-22),(x-20,y-22)],arcade.color.BLACK)    
        # arcade.draw_line(x-20,y+22, x-20,y-22,arcade.color.BLUE,10)               # plataforma 1

    
    def update(self,space,personaje_shape):
        self.salto()
        self.colisiones_paredes()
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

    def salto(self):
        # verificar colision con personaje si existe cambie a estado vacio
        if not self.vacio:
            colisiones = self.space.shape_query(self.sensor_bloque)
            for col in colisiones:
                if col.shape == self.personaje.hide_box:
                    self.vacio = True
                    self.soltar_objeto()
                    self.personaje.rebote(self.personaje.body.velocity.x,-500)

    def colisiones_paredes(self):
        colisiones_iz = self.space.shape_query(self.linea_costado_iz)
        colisiones_der = self.space.shape_query(self.linea_costado_der)
        for col in colisiones_iz:
            if col.shape == self.personaje.hide_box:
                self.personaje.rebote(-10,self.personaje.body.velocity.y)


        for col in colisiones_der:
            if col.shape == self.personaje.hide_box:
                self.personaje.rebote(10,self.personaje.body.velocity.y)
                



    def unirse_al_espacio(self):
        if self.body_bloque.space is None:
            self.space.add(self.body_bloque,*self.lista_shapes)
        self.estar_en_espacio = True



    def borrar_del_espacio(self):
        if self.body_bloque.space is not None:
            self.space.remove(self.body_bloque,*self.lista_shapes)
        self.estar_en_espacio = False
        