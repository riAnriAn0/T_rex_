import pygame

IMAGEM_OVER = pygame.image.load('src/img/game_over.png')

class Over:

    IMAGEM = IMAGEM_OVER

    def __init__(self):
        self.x = 600 - (self.IMAGEM.get_width() / 2)
        self.y = 200
        self.imagem = self.IMAGEM
        self.sprite_width = self.IMAGEM.get_width()
        self.sprite_height = self.IMAGEM.get_height()

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x,self.y))