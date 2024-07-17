import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Configurações da janela
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Jogo de Nave Interestelar")

# Definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
COLORS = [WHITE, YELLOW, BLUE, RED, GREEN, PINK, ORANGE]

# Criar estrelas
def create_stars(num_stars):
    stars = []
    for _ in range(num_stars):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        radius = random.randint(1, 3)
        color = random.choice(COLORS)
        speed = random.randint(1, 3)
        stars.append([x, y, radius, color, speed])
    return stars

# Desenhar estrelas no fundo
def draw_stars(screen, stars):
    for star in stars:
        pygame.draw.circle(screen, star[3], (star[0], star[1]), star[2])

# Atualizar posição das estrelas
def update_stars(stars):
    for star in stars:
        star[1] += star[4]  # Mover a estrela para baixo
        if star[1] > 1000:
            star[1] = 0  # Reposicionar estrela no topo
            star[0] = random.randint(0, 1000)  # Nova posição horizontal
            star[2] = random.randint(1, 3)  # Novo raio
            star[3] = random.choice(COLORS)  # Nova cor
            star[4] = random.randint(1, 3)  # Nova velocidade

# Número de estrelas
num_stars = 150
stars = create_stars(num_stars)

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(30)  # Define a taxa de frames por segundo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Desenhar fundo preto
        screen.fill(BLACK)
        
        # Atualizar e desenhar estrelas
        update_stars(stars)
        draw_stars(screen, stars)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

game_loop()
