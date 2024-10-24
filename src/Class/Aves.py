import pygame

IMAGEM_AVES = pygame.image.load('src/img/aves.png')

class Aves:

    IMAGEM = IMAGEM_AVES
    SPRITE_WIDTH = 184
    SPRITE_HEIGHT = 79
    FRAME_X = 92
    FRAME_Y = 79

    def __init__(self, x):
        self.x = x
        self.y = 200
        self.imagem = self.IMAGEM
        self.velocidade = 30
        self.sprite_width = self.IMAGEM.get_width()
        self.sprite_height = self.IMAGEM.get_height()
        self.sprite_atual = 1
        self.passou = False

    def animacao(self):
        self.x -= self.velocidade
        if self.x < 5:
            self.passou = True
    
    def mask(self):
        return pygame.mask.from_surface(self.imagem)

    def desenhar(self, tela): 
        self.sprite_atual += 1
        if self.sprite_atual > 1:
            self.sprite_atual = 0

        tela.blit(self.imagem,(self.x, self.y), (self.sprite_atual * self.FRAME_X, 0, self.FRAME_X, self.FRAME_Y))

    def remover(self, vetor, indice):
            if self.passou:
                vetor.pop(indice)