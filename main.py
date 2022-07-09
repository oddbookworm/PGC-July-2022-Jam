import pygame
import asyncio

from dim import Dim
from snek import Snek

async def main():
    WIDTH, HEIGHT = (512, 512)
    pixel_size = 8

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    
    Dimension1 = Dim("white", WIDTH, HEIGHT, pixel_size, (0, 0, 0))

    Player = Snek("red", pixel_size, (256, 256), 20)

    direction = "right"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    direction = "up"
                elif event.key == pygame.K_d:
                    direction = "right"
                elif event.key == pygame.K_s:
                    direction = "down"
                elif event.key == pygame.K_a:
                    direction = "left"

        Player.move(direction)

        screen.fill("black")
        Dimension1.draw(screen)
        Player.draw(screen)
        pygame.display.flip()
        clock.tick(10)
        await asyncio.sleep(0)

def run():
    asyncio.run(main())

if __name__ == "__main__":
    run()