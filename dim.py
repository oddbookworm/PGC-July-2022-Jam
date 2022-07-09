import pygame
from typing import Tuple

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
        
    def draw(self, screen):
        screen.blit(self.bg, self.bg.get_rect())