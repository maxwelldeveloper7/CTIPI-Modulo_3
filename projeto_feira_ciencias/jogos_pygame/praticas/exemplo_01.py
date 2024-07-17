import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Exemplo Pygame")

# Loop principal
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Define a cor de fundo (RGB)
    screen.fill((0, 128, 255))
    
    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
sys.exit()