import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Clique para Mudar de Cor")

# Posição e cor do quadrado
x, y = 100, 100
cor = (0, 0, 255)
largura, altura = 50, 50

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Evento de clique do mouse
            mouse_x, mouse_y = event.pos
            if x <= mouse_x <= x + largura and y <= mouse_y <= y + altura:
                cor = (255, 0, 0)  # Muda a cor para vermelho

    # Preenche a tela com branco
    screen.fill((255, 255, 255))

    # Desenha o quadrado com a cor atual
    pygame.draw.rect(screen, cor, (x, y, largura, altura))

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
sys.exit()
