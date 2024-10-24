import pygame

IMAGEM_DINO_REBAIXADO = pygame.image.load('src/img/dino_rebaixado.png')
IMAGEM_DINO = pygame.image.load('src/img/dino.png')

class Dino:

    IMAGEM = IMAGEM_DINO
    IMAGEM_REBAIXADO = IMAGEM_DINO_REBAIXADO

    def __init__(self):
        self.x = 150
        self.y = 265
        self.imagem = self.IMAGEM
        self.sprite_atual = 1
        self.sprite_width = self.IMAGEM.get_width()
        self.sprite_height = self.IMAGEM.get_height()
        self.velocidade = 3
        self.gravidade = 3
        self.pulando = False
        self.colidir = False
        self.abaixar = False

    def desenhar(self, tela):
        
        if self.abaixar:
            self.sprite_atual += 1
            if self.sprite_atual > 1:
                self.sprite_atual = 0
        elif self.colidir:
            self.sprite_atual = 3
        elif not self.pulando:
            self.sprite_atual += 1
            if self.sprite_atual > 2:
                self.sprite_atual = 1
        elif self.pulando:
            self.sprite_atual = 0

        if self.abaixar:   
            self.imagem = self.IMAGEM_REBAIXADO
            tela.blit( self.imagem,(self.x, 300), (self.sprite_atual * 118.5, 0, 118.5, 59))
        else:
            self.imagem = self.IMAGEM
            tela.blit( self.imagem,(self.x, self.y), (self.sprite_atual * 87.5, 0, 87.5, 94))

    def pular(self):

        if  not self.pulando:
            self.pulando = True
            self.y -= 200 

        if self.y < 270:
                self.y += self.velocidade
                self.velocidade += self.gravidade
                if self.y > 265:
                    self.y = 265
                    self.pulando = False
                    self.velocidade = 0

    def mask(self):
        if self.abaixar:
            dino_frame_surface = self.imagem.subsurface((self.sprite_atual * 118.5, 0, 118.5, 59))
        else:
            dino_frame_surface = self.imagem.subsurface((self.sprite_atual * 87.5, 0, 87.5, 94))
        
        return pygame.mask.from_surface(dino_frame_surface)
    
    def colisao(self, obstaculo):

        offset_x = obstaculo.x - self.x
        offset_y = obstaculo.y - (self.y if not self.abaixar else 300)
        mask_dino = self.mask()

        if mask_dino.overlap(obstaculo.mask(),(offset_x, offset_y)):
            obstaculo.velocidade = 0
            self.colidir = True
