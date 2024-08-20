def desenha_jogador(screen, posicao):
    pygame.draw.rect(screen, BRANCO, (*posicao, 50, 50))

def atualiza_pontuacao(pontuacao):
    texto = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)
    screen.blit(texto, (10, 10))
