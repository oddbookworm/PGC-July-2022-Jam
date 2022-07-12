import pygame
import asyncio
import sys
import os
from random import randint, choice

try:
    from .dim import Dim
    from .snek import Snek
    from .gameover import GameOver
except ImportError:
    from dim import Dim
    from snek import Snek
    from gameover import GameOver


def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename


nuggets = []


def load_easter():
    surf = pygame.image.load(get_path("pygame.png")).convert_alpha()
    return surf


def spawn_nugget(dim: Dim):
    pos = (
        randint(0, dim.width // dim.px_size) * dim.px_size,
        randint(0, dim.height // dim.px_size) * dim.px_size,
    )
    rect = pygame.Rect(*pos, dim.px_size, dim.px_size)
    nuggets.append([rect, dim])


def draw_nuggets(screen, player):
    for nugget in nuggets:
        if nugget[1] == player.curr_dim:
            pygame.draw.rect(screen, "yellow", nugget[0])

def set_up(pixel_size, Dimensions):
    Player = Snek("yellow", pixel_size, (256, 256, Dimensions[0]), 10, Dimensions)
    direction1 = "right"
    direction2 = None
    loaded = False

    return (Player, direction1, direction2, loaded)

async def main():
    WIDTH, HEIGHT = (512, 512)
    pixel_size = 8
    number_nuggets = 16

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    game_over = GameOver(WIDTH, HEIGHT)

    Dimensions = [
        Dim("black", WIDTH, HEIGHT, pixel_size, (0, 0, 0)),
        Dim("black", WIDTH, HEIGHT, pixel_size, (1, 0, 0)),
        Dim("black", WIDTH, HEIGHT, pixel_size, (0, 1, 0)),
        Dim("black", WIDTH, HEIGHT, pixel_size, (1, 1, 0)),
        Dim("blue", WIDTH, HEIGHT, pixel_size, (0, 0, 1)),
        Dim("blue", WIDTH, HEIGHT, pixel_size, (1, 0, 1)),
        Dim("blue", WIDTH, HEIGHT, pixel_size, (0, 1, 1)),
        Dim("blue", WIDTH, HEIGHT, pixel_size, (1, 1, 1)),
    ]

    # Player = Snek("yellow", pixel_size, (256, 256, Dimensions[0]), 10, Dimensions)

    # direction1 = "right"
    # direction2 = None

    # loaded = False

    Player, direction1, direction2, loaded = set_up(pixel_size, Dimensions)

    restart = False
    while True:
        old_direction = direction1
        if len(nuggets) < number_nuggets:
            spawn_nugget(choice(Dimensions))

        direction2 = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if old_direction != "down":
                        direction1 = "up"
                elif event.key == pygame.K_d:
                    if old_direction != "left":
                        direction1 = "right"
                elif event.key == pygame.K_s:
                    if old_direction != "up":
                        direction1 = "down"
                elif event.key == pygame.K_a:
                    if old_direction != "right":
                        direction1 = "left"
                elif event.key == pygame.K_e:
                    direction2 = "out"
                elif event.key == pygame.K_q:
                    direction2 = "in"

                if Player.dead and event.key == pygame.K_r:
                    restart = True

        if not Player.dead:
            Player.move(direction1, direction2)
            hit_nuggets = Player.nugget_check(nuggets)
            for nugget in hit_nuggets:
                nuggets.remove(nugget)
                Player.add_segment()
            curr_dim = Player.curr_dim

            if Player.easter_egg() and not loaded:
                easter = load_easter()
                loaded = True

            screen.fill("black")
            curr_dim.draw(screen)

            draw_nuggets(screen, Player)
            Player.draw(screen)
            if loaded:
                head_rect_center = Player.segments[0][0].center
                screen.blit(easter, easter.get_rect(center = head_rect_center))

        else:
            screen.fill("black")
            game_over.draw(screen, len(Player.segments))

        pygame.display.flip()

        if restart:
            Player, direction1, direction2, loaded = set_up(pixel_size, Dimensions)
            restart = False

        clock.tick(15)
        await asyncio.sleep(0)


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
