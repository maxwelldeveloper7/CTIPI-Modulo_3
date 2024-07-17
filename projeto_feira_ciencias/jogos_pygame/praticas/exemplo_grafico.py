import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Exemplo de Renderização de Gráficos com Pygame")

# Definindo cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Define a cor de fundo (branco)
    screen.fill(WHITE)

    # Desenha um retângulo vermelho
    pygame.draw.rect(screen, RED, (100, 100, 200, 100))

    # Desenha um círculo azul
    pygame.draw.circle(screen, BLUE, (400, 300), 50)

    # Desenha uma linha verde
    pygame.draw.line(screen, GREEN, (600, 100), (700, 200), 5)

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
sys.exit()
