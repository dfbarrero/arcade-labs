import arcade

WIDTH = 800
HEIGHT = 600

arcade.open_window(WIDTH, HEIGHT, "Ejemplo")

arcade.draw_text("Hola, mundo", 350, 300, arcade.color.WHITE)

arcade.run()