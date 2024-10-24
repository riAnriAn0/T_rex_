import pygame

IMAGEM_CACTO = pygame.image.load('src/img/cacto.png')

class Cactos:

    IMAGEM = IMAGEM_CACTO
    SPRITE_WIDTH = 25
    SPRITE_HEIGHT = 47
    FRAME_X = 0
    FRAME_Y = 0

    def __init__(self, x):
        self.x = x
        self.y = 275  
        self.imagem = self.IMAGEM
        self.velocidade = 25
        self.sprite_width = self.IMAGEM.get_width()
        self.sprite_height = self.IMAGEM.get_height()
        self.passou = False

    def animacao(self):

        self.x -= self.velocidade
        if self.x < -100:
            self.passou = True
    
    def mask(self):
        return pygame.mask.from_surface(self.imagem)

    def desenhar(self, tela):    
        tela.blit( self.imagem,(self.x, self.y))

    def remover(self, vetor, indice):
            if self.passou:
                vetor.pop(indice)