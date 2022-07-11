import pygame
from typing import Tuple

pygame.font.init()

class Dim:
    def __init__(
        self, 
        color: str, 
        width: int, 
        height: int, 
        px_size: int, 
        dimension_pos: Tuple[int, int, int]
    ):
        self.color = color
        self.width = width
        self.height = height
        self.px_size = px_size
        self.d_pos = dimension_pos

        self.bg = pygame.Surface((self.width, self.height))
        self.bg.fill(self.color)

        if not self.d_pos[0]:
            pygame.draw.line(self.bg, "red", (0, 0), (0, self.height), 2)
        else:
            pygame.draw.line(self.bg, "red", (self.width - 2, 0), (self.width - 2, self.height), 2)
        
        if not self.d_pos[1]:
            pygame.draw.line(self.bg, "red", (0, 0), (self.width, 0), 2)
        else:
            pygame.draw.line(self.bg, "red", (0, self.height - 2), (self.width, self.height - 2), 2)

        font = pygame.font.SysFont("comicsans", 20)
        number = font.render(str(self.d_pos[2]), True, "red")
        
        self.bg.blit(number, number.get_rect(topleft = (5, 0)))
        self.rect = self.bg.get_rect()
        
    def draw(self, screen):
        screen.blit(self.bg, self.rect)