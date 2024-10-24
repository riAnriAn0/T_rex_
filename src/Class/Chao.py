import pygame

IMAGEM_CHAO = pygame.image.load('src/img/chao.png')

class Chao:

    IMAGEM = IMAGEM_CHAO
    FRAME_X = 0
    FRAME_Y = 0

    def __init__(self):
        self.imagem = self.IMAGEM
        self.x = 0
        self.y = 340
        self.x_2 = 1200
        self.y_2 = 340
        self.velocidade = 20
        self.sprite_width = self.IMAGEM.get_width()
        self.sprite_height = self.IMAGEM.get_height()

    def animacao(self):
        self.x -= self.velocidade
        self.x_2 -= self.velocidade

        if self.x < -1200:
            self.x = 1200

        if self.x_2 < -1200:
            self.x_2 = 1200
    
    def desenhar(self, tela):
        tela.blit( self.imagem,(self.x, self.y))
        tela.blit( self.imagem,(self.x_2, self.y_2))
