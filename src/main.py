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

    display = pygame.display.set_mode((DISPLAY_WIDTH,DIPLAY_HEIGHT))
    clock = pygame.time.Clock()
    rodando = True
    game_over = Over()
    chao = Chao()
    nuvens = [Nuvem(1100,100)]
    cactos = [Cactos(1400)]
    aves = [Aves(3000)]
    dino = Dino()
    text = Text(display)

    while rodando:
    
        clock.tick(17) 
        display.fill((247,247,247))

        for event in pygame.event.get():
            if event.type == QUIT:
                rodando = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:    
                    dino.pular()
                if event.key == pygame.K_r and dino.colidir:
                    main() 
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            dino.abaixar = True
        else:
            dino.abaixar = False

        if dino.pulando:
            dino.pular()

        if nuvens[0].x < 700 and len(nuvens) < 2:
            x = random.randrange(1100,1300,100)
            y = random.randrange(190,270,20)
            nuvens.append(Nuvem(x, y - 10))

    # Sortei a saida do cacto(3 ou 2 ou 1) ou aves
        num = random.randrange(0,10,1)
        num_cactos = random.randrange(1,3,1)

        if  len(aves) == 0 and len(cactos) == 0:
            if num <= 9 :
                if num_cactos == 1:
                    cactos.append(Cactos(1200))
                elif num == 2: 
                    cactos.append(Cactos(1205))
                    cactos.append(Cactos(1245))
                else:
                    cactos.append(Cactos(1205))
                    cactos.append(Cactos(1245))
                    cactos.append(Cactos(1290))
            
            else:
                aves.append(Aves(1300)) 
                aves.append(Aves(1300)) 
        
        desenhar(display,chao, nuvens, cactos, aves, dino, text)
           
        for cacto in cactos:
            dino.colisao(cacto) 
        
        for ave in aves:
            dino.colisao(ave)

        for i,cacto in enumerate(cactos):
            cacto.remover(cactos, i)

        for i,ave in enumerate(aves):
            ave.remover(aves, i)

        for i, nuvem in enumerate(nuvens):
            nuvem.remover(nuvens, i)

        if not dino.colidir:
            text.pontos += 1
        if text.pontos % 100 == 0:
            chao.velocidade += 10
            for cacto in cactos:
                cacto.velocidade  += 10

        retornar(display, game_over, dino, text )
        
        pygame.display.flip()

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()


