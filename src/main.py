import pygame
import random
from sys import exit
from pygame.locals import *

from Class.Dino import Dino
from Class.Aves import Aves
from Class.Chao import Chao
from Class.Nuvem import Nuvem
from Class.Cacto import Cactos
from Class.Over import Over
from Class.Text import Text

pygame.init()
pygame.mixer.init()

def desenhar(tela, chao, nuvens, cactos, aves, dino, text):
    text.showPontos()
    
    if not dino.colidir:
        for cacto in cactos:
            cacto.animacao()
        for ave in aves:
            ave.animacao()
        for nuvem in nuvens:
            nuvem.animacao()
        chao.animacao()

    chao.desenhar(tela)
    dino.desenhar(tela)

    for nuvem in nuvens:
        nuvem.desenhar(tela)

    for cacto in cactos:
        cacto.desenhar(tela)
    
    for ave in aves:
        ave.desenhar(tela)

def retornar(tela, game_over, dino, text):
    if dino.colidir:
        game_over.desenhar(tela)
        text.gameOver()
        if text.pontos > text.melhor_pontuação:
            text.melhor_pontuação = text.pontos

def main():
    DISPLAY_WIDTH = 1200
    DIPLAY_HEIGHT = 500
    display = pygame.display.set_mode((DISPLAY_WIDTH, DIPLAY_HEIGHT))
    clock = pygame.time.Clock()
    
    text = Text(display)

    while True: # LOOP PRINCIPAL DO APLICATIVO
        game_over = Over()
        chao = Chao()
        nuvens = [Nuvem(1100, 100)]
        cactos = []
        aves = []
        dino = Dino()
        text.pontos = 0 

        jogando = True
        while jogando: # LOOP DA PARTIDA ATUAL
            clock.tick(30) 
            display.fill((247, 247, 247))

            # Captura o estado das teclas para o pulo variável
            keys = pygame.key.get_pressed()
            espaco_pressionado = keys[pygame.K_SPACE]

            # --- ÚNICO LOOP DE EVENTOS ---
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == pygame.KEYDOWN:
                    # Inicia o pulo apenas no momento do clique
                    if event.key == pygame.K_SPACE and not dino.colidir:
                        dino.pular(espaco_pressionado)

            # --- LÓGICA CONTÍNUA (FORA DO EVENT LOOP) ---
            
            # Executa a física do pulo enquanto estiver no ar
            if dino.pulando:
                dino.pular(espaco_pressionado)
            
            # Lógica de Agachar (Seta para Baixo)
            if keys[pygame.K_DOWN]:
                if not dino.abaixar:
                    dino.sprite_atual = 0 
                dino.abaixar = True
            else:
                dino.abaixar = False

            # Gerenciamento de Nuvens
            if nuvens[0].x < 700 and len(nuvens) < 2:
                x = random.randrange(1100, 1300, 100)
                y = random.randrange(190, 270, 20)
                nuvens.append(Nuvem(x, y - 10))

            # Sorteio de Obstáculos
            if len(aves) == 0 and len(cactos) == 0:
                num = random.randrange(0, 10, 1)
                if num <= 8: 
                    num_cactos = random.randrange(1, 4, 1)
                    for i in range(num_cactos):
                        cactos.append(Cactos(1200 + (i * 50)))
                else: 
                    aves.append(Aves(1300)) 
            
            desenhar(display, chao, nuvens, cactos, aves, dino, text)
               
            for cacto in cactos:
                dino.colisao(cacto) 
            
            for ave in aves:
                dino.colisao(ave)

            if not dino.colidir:
                text.pontos += 1
                if text.pontos % 100 == 0:
                    chao.velocidade += 1 
                    # Atualiza a velocidade dos obstáculos existentes
                    for c in cactos: c.velocidade += 2
                    for a in aves: a.velocidade += 2

            # Remoção de objetos
            for i, cacto in enumerate(cactos[:]):
                cacto.remover(cactos, i)
            for i, ave in enumerate(aves[:]):
                ave.remover(aves, i)
            for i, nuvem in enumerate(nuvens[:]):
                nuvem.remover(nuvens, i)

            retornar(display, game_over, dino, text)
            pygame.display.flip()

            if dino.colidir:
                jogando = False 

        # LOOP DE ESPERA (GAME OVER)
        esperando = True
        while esperando:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r: 
                        esperando = False
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        exit()

if __name__ == "__main__":
    main()