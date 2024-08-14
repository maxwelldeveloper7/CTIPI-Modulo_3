import pygame
import sys

# Initialize Pygame
pygame.init()

# Configurações da janela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Eventos no Pygame")

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Evento de fechamento da janela
            print(event.__str__()) # Imprime no console o evento de fechamento da janela
            running = False

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
sys.exit()
