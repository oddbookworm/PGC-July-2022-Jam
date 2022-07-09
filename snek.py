import pygame
from random import choice

from typing import Tuple

class Snek:
    def __init__(
        self, 
        color: str, 
        px_size: int, 
        pos = Tuple[int, int], 
        length = int
    ):
        self.color = color
        self.px_size = px_size
        self.pos = pos
        self.length = length

        direction = choice(["up", "down", "left", "right"])
        if direction == "up":
            offset = (0, -px_size)
        elif direction == "down":
            offset = (0, px_size)
        elif direction == "left":
            offset = (-px_size, 0)
        else:
            offset = (px_size, 0)
        
        self.segments = []
        for i in range(self.length):
            position = (self.pos[0] + offset[0] * i, self.pos[1] + offset[1] * i)
            self.segments.append(pygame.Rect(*position, px_size, px_size))

    def move(self, direction):
        new_segments = []
        # move the head
        if direction == "right":
            new_segments.append(self.segments[0].move(self.px_size, 0))
        elif direction == "left":
            new_segments.append(self.segments[0].move(-self.px_size, 0))
        elif direction == "up":
            new_segments.append(self.segments[0].move(0, -self.px_size))
        else:
            new_segments.append(self.segments[0].move(0, self.px_size))
        
        for i, segment in enumerate(self.segments):
            if not i:
                continue

            new_x = self.segments[i - 1].x
            new_y = self.segments[i - 1].y
            new_segments.append(pygame.Rect(new_x, new_y, self.px_size, self.px_size))
        
        self.segments = new_segments

    def draw(self, screen):
        for segment in self.segments:
            pygame.draw.rect(screen, self.color, segment)