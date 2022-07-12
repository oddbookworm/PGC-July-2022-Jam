import pygame

pygame.font.init()


class GameOver:
    def __init__(self, width, height):
        self.surf = pygame.Surface((width, height))
        self.surf.fill("black")
        self.font = pygame.font.SysFont("comicsans", 72)
        

    def draw(self, screen, length):
        self.surf.fill("black")
        self.text = self.font.render("Game Over", True, "red")
        self.text_rect = self.text.get_rect(center=self.surf.get_rect().center)
        self.surf.blit(self.text, self.text_rect)
        self.length = self.font.render(str(length), True, "red")
        self.length_rect = self.length.get_rect(
            top=self.text_rect.bottom, centerx=self.text_rect.centerx
        )

        self.surf.blit(self.length, self.length_rect)
        screen.blit(self.surf, self.surf.get_rect())
