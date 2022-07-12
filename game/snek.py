import pygame
from typing import Tuple, List

try:
    from .dim import Dim
except ImportError:
    from dim import Dim


class Snek:
    def __init__(
        self,
        color: str,
        px_size: int,
        pos: Tuple[int, int, Dim],
        length: int,
        dim_list: List[Dim],
    ):
        self.color = color
        self.px_size = px_size
        self.pos = pos
        self.curr_dim = pos[2]
        self.length = length
        self.dims = dim_list
        self.dead = False

        offset = (-px_size, 0)

        self.segments = []
        for i in range(self.length):
            position = (self.pos[0] + offset[0] * i, self.pos[1] + offset[1] * i)
            self.segments.append(
                [pygame.Rect(*position, px_size, px_size), self.pos[2]]
            )

    def move(self, direction1, direction2):
        new_segments = []
        # move the head
        head = self.segments[0][0]
        if direction1 == "right":
            offset = (self.px_size, 0)
        elif direction1 == "left":
            offset = (-self.px_size, 0)
        elif direction1 == "up":
            offset = (0, -self.px_size)
        elif direction1 == "down":
            offset = (0, self.px_size)
        if direction2 == "out":
            offset = (0, 0)
            new_dim_pos = (self.curr_dim.d_pos[0], self.curr_dim.d_pos[1], 1)
            for dim in self.dims:
                if dim.d_pos == new_dim_pos:
                    self.curr_dim = dim
        elif direction2 == "in":
            offset = (0, 0)
            new_dim_pos = (self.curr_dim.d_pos[0], self.curr_dim.d_pos[1], 0)
            for dim in self.dims:
                if dim.d_pos == new_dim_pos:
                    self.curr_dim = dim

        new_head = head.move(offset)
        if new_head.x < 0:
            if self.curr_dim.d_pos[0]:
                new_dim_pos = (0, self.curr_dim.d_pos[1], self.curr_dim.d_pos[2])
                for dim in self.dims:
                    if dim.d_pos == new_dim_pos:
                        self.curr_dim = dim
                new_head.x = self.curr_dim.width - self.curr_dim.px_size
            else:
                self.die()
                return

        elif new_head.x >= self.curr_dim.width:
            if not self.curr_dim.d_pos[0]:
                new_dim_pos = (1, self.curr_dim.d_pos[1], self.curr_dim.d_pos[2])
                for dim in self.dims:
                    if dim.d_pos == new_dim_pos:
                        self.curr_dim = dim
                new_head.x = 0
            else:
                self.die()
                return

        elif new_head.y < 0:
            if self.curr_dim.d_pos[1]:
                new_dim_pos = (self.curr_dim.d_pos[0], 0, self.curr_dim.d_pos[2])
                for dim in self.dims:
                    if dim.d_pos == new_dim_pos:
                        self.curr_dim = dim
                new_head.y = self.curr_dim.height - self.curr_dim.px_size
            else:
                self.die()
                return

        elif new_head.y >= self.curr_dim.height:
            if not self.curr_dim.d_pos[1]:
                new_dim_pos = (self.curr_dim.d_pos[0], 1, self.curr_dim.d_pos[2])
                for dim in self.dims:
                    if dim.d_pos == new_dim_pos:
                        self.curr_dim = dim
                new_head.y = 0
            else:
                self.die()
                return

        new_segments.append([new_head, self.curr_dim])

        for i, segment in enumerate(self.segments):
            if not i:
                continue

            new_x = self.segments[i - 1][0].x
            new_y = self.segments[i - 1][0].y
            new_dim = self.segments[i - 1][1]

            new_segments.append(
                [pygame.Rect(new_x, new_y, self.px_size, self.px_size), new_dim]
            )

        self.segments = new_segments
        self.self_collison()

    def self_collison(self):
        for i in range(len(self.segments)):
            for j in range(i):
                if self.segments[i] == self.segments[j]:
                    self.die()
                    return True

    def add_segment(self):
        self.segments.append(
            [pygame.Rect(-100, -100, self.px_size, self.px_size), self.curr_dim]
        )

    def draw(self, screen):
        for segment in self.segments:
            if segment[1] == self.curr_dim:
                pygame.draw.rect(screen, self.color, segment[0])

    def die(self):
        self.dead = True

    def nugget_check(self, nuggets):
        nuggs = []
        for nugg in nuggets:
            if nugg == self.segments[0]:
                nuggs.append(nugg)
        return nuggs

    def easter_egg(self):
        if len(self.segments) >= 40:
            return True
        return False
