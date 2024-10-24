import pygame
pygame.font.init()


FONTE_PONTOS = pygame.font.SysFont('fonts/PressStart2P-Regular.ttf', 30)

class Text:

    FONTE = FONTE_PONTOS
    MELHOR_PONTUACAO = 0

    def __init__(self,tela):
        self.pontos = 0 
        self.melhor_pontuação = self.MELHOR_PONTUACAO
        self.font = self.FONTE
        self.tela = tela
    def showPontos(self):
        
        texto = self.font.render(f"{self.pontos}", 0,(83,83,83))
        texto_mpv = self.font.render(f"HI {self.melhor_pontuação}", 0,(166,166,166))

        self.tela.blit(texto,(1000 , 100))
        self.tela.blit(texto_mpv,(900 , 100))

    def gameOver(self):
        
        msg_retorono = self.font.render(f"Precione 'R' para reiniciar", 0,(64,64,64))
        self.tela.blit(msg_retorono,( 470 ,240))

        