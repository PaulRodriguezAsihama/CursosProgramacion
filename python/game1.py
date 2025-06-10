import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego uno")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Posición inicial del cuadrado
x, y = 400, 300
speed = 5
angle = 0  # Ángulo inicial

# Cargar la imagen del avión
avion_img = pygame.image.load("avion.png").convert_alpha()

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle += 5  # Rotar a la izquierda
    if keys[pygame.K_RIGHT]:
        angle -= 5  # Rotar a la derecha
    if keys[pygame.K_UP]:
        y -= speed  # Mover hacia arriba (vertical)
    if keys[pygame.K_DOWN]:
        y += speed  # Mover hacia abajo (vertical)

    # Pantalla continua (wrap-around)
    if x > 800:
        x = -50
    if x < -50:
        x = 800
    if y > 600:
        y = -50
    if y < -50:
        y = 600

    # Lógica del juego
    screen.fill(WHITE)  # Limpiar pantalla

    # Rotar la imagen del avión
    rotated_avion = pygame.transform.rotate(avion_img, angle)
    rect = rotated_avion.get_rect(
        center=(x + avion_img.get_width() // 2, y + avion_img.get_height() // 2))
    screen.blit(rotated_avion, rect.topleft)

    pygame.display.flip()  # Actualizar pantalla
    pygame.time.Clock().tick(30)  # Control del framerate

# Salir de Pygame
pygame.quit()
sys.exit()
