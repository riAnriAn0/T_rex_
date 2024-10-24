import pygame

IMAGEM_NUVEM =  pygame.image.load('src/img/nuvem.png')

class Nuvem:

    IMAGEM = IMAGEM_NUVEM
    FRAME_X = 0
    FRAME_Y = 0

    def __init__(self,x, y):
        self.imagem = self.IMAGEM
        self.x = x
        self.y = y
        self.velocidade = 3
        self.sprite_width = self.IMAGEM.get_width()
        self.sprite_height = self.IMAGEM.get_height()
        self.passou = False

    def animacao(self):
        self.x -= self.velocidade
        if self.x < -5:
            self.passou = True

    def desenhar(self, tela):
        tela.blit( self.imagem,(self.x, self.y))

    def remover(self, vetor, indice):
            if self.passou:
                vetor.pop(indice)