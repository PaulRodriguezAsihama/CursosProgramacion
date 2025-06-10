import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ejemplo de Sprites")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clase para el Jugador (Sprite)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()  # Inicializar la clase base Sprite
        # Crear una imagen (en este caso, un rectángulo verde)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        # Definir el rectángulo (posición y tamaño)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self):
        # Movimiento del jugador con teclas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Limitar movimiento dentro de la pantalla
        self.rect.clamp_ip(screen.get_rect())

# Clase para el Enemigo (Sprite)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Crear una imagen (un rectángulo rojo)
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        # Definir el rectángulo
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.direction = 1  # 1 para derecha, -1 para izquierda

    def update(self):
        # Movimiento simple del enemigo (ida y vuelta)
        self.rect.x += self.speed * self.direction
        if self.rect.right > 800 or self.rect.left < 0:
            self.direction *= -1  # Cambiar dirección al tocar bordes


# Crear grupos de sprites
all_sprites = pygame.sprite.Group()  # Grupo para todos los sprites
enemies = pygame.sprite.Group()      # Grupo solo para enemigos

# Crear instancias de los sprites
player = Player(400, 300)  # Jugador en el centro
enemy = Enemy(100, 200)    # Enemigo en otra posición

# Añadir sprites a los grupos
all_sprites.add(player, enemy)
enemies.add(enemy)

# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar todos los sprites
    all_sprites.update()

    # Detectar colisiones entre el jugador y los enemigos
    if pygame.sprite.spritecollide(player, enemies, False):
        print("¡Colisión detectada! Has chocado con un enemigo.")

    # Dibujar
    screen.fill(WHITE)  # Limpiar pantalla
    all_sprites.draw(screen)  # Dibujar todos los sprites
    pygame.display.flip()  # Actualizar pantalla

    # Controlar framerate
    clock.tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()
