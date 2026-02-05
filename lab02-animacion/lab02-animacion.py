import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Mi Juego")
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
    
    def on_draw(self):
        self.clear()
        # Poner aquí el código del dibujo
        # Cambiar la posición y/o tamaño del dibujo para crear animación
        

if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()
