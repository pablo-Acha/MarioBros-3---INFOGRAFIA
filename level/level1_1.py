from .levels import Level
import pymunk
from configuraciones import WIDTH, HEIGHT, TITLE
import arcade
from entities.bloques import Bloques
from .chunks.chunks_nivel_1_1.primer_chunk import Primer_Chunk

class Level1(Level):
    def __init__(self, personaje, extension_imagen = "png",left=0, center_y=450):
        super().__init__("level_1_1",personaje,extension_imagen,left, center_y)
        self.enemigos =  self.setEnemigos()
        self.plataformas =  self.setPlataformas()
        
        #codigo temporal 
        # Piso principal
        # self.piso = pymunk.Segment(self.piso_body,(-50,100),(WIDTH+500,100),50)

        # =======================
        # MUROS EXTRA
        # =======================
        # Muro izquierdo
        #self.muro_izq = pymunk.Segment(self.piso_body, (150,300), (300,150), 10)
        # Muro derecho
        #self.muro_der = pymunk.Segment(self.piso_body, (WIDTH,150), (WIDTH,400), 10)
        # Plataforma flotante
        # Otra plataforma más alta
        # self.plataforma_1 = pymunk.Segment(self.piso_body, (720,280), (860,280), 5)
        # self.plataforma_2 = pymunk.Segment(self.piso_body, (530,280), (625,280), 5)
        # self.plataforma_3 = pymunk.Segment(self.piso_body, (530,330), (625,330), 5)
        # self.plataforma_4 = pymunk.Segment(self.piso_body, (530,425), (625,425), 5)
        # self.plataforma_5 = pymunk.Segment(self.piso_body, (530,475), (625,475), 5)

        self.chunk = Primer_Chunk(0)
        self.chunk.agregar_todo(self.space,self.piso_body)
        #añadri bloque
        # self.bloque = Bloques(center_x = 550,center_y= 310)
        # self.bloque_1 = Bloques(center_x = 600,center_y= 310)

        # Añadir todos los muros al espacio
        # self.space.add(self.piso_body,self.piso, self.plataforma_1, self.plataforma_2, self.plataforma_3, self.plataforma_4, self.plataforma_5)
        # self.space.add(self.bloque.body_bloque,self.bloque.bloque_box)
        # self.space.add(self.bloque_1.body_bloque,self.bloque_1.bloque_box)

    def setEnemigos(self):
        #crear enemigos
        pass
    
    def setPlataformas(self):
        #crear Plataformas
        pass

    def on_draw(self):
        super().on_draw()    
        
        for i in range(0,800,20):
            arcade.draw_line(0,i,WIDTH,i,arcade.color.ROSE,2)              
        for i in range(0,WIDTH,20):
            arcade.draw_line(i,0,i,HEIGHT,arcade.color.ROSE,2)             
        for i in range(0,800,100):
            arcade.draw_line(0,i,WIDTH,i,arcade.color.BLACK,3)             
        for i in range(0,WIDTH,100):
            arcade.draw_line(i,0,i,HEIGHT,arcade.color.BLACK,3)            
        self.chunk.draw_todo()
        # Piso
        arcade.draw_polygon_outline([(-50,150),(WIDTH+50,150)
                             ,(WIDTH+50,100),(-50,100)],arcade.color.BLACK)    

        arcade.draw_line(720,280,860,280,arcade.color.BLUE,3)               # plataforma 1
        arcade.draw_line(530,280,625,280,arcade.color.GREEN,3)              # plataforma 2
        arcade.draw_line(530,330,625,330,arcade.color.PURPLE,3)              # plataforma 3
        arcade.draw_line(530,425,625,425,arcade.color.PURPLE,3)              # plataforma 4
        arcade.draw_line(530,475,625,475,arcade.color.PURPLE,3)              # plataforma 5


    def update(self, delta_time):
        self.chunk.update_todo(self.fondo.left,self.space, self.personaje.hide_box)
        if self.fondo.left <-1000:
            self.chunk.eliminar_todo(self.space)
        
        
        super().update(delta_time)

    def mover_plataformas(self, dx):
        self.chunk.mover_todo(dx,self.piso_body)

    # def evitar_desborde(self):
    #     for shape in self.chunk.lista_plataformas:
    #         if self.personaje.center_y > shape.a[1] and self.personaje.center_y - shape.a[1] < 30 and self.personaje.center_x > shape.a[0] and self.personaje.center_x < shape.b[0]:
    #             self.personaje.body.velocity  = (self.personaje.body.velocity.x,-10)

