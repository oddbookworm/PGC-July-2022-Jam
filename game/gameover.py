import pygame

pygame.font.init()


class GameOver:
    def __init__(self, width, height):
        self.surf = pygame.Surface((width, height))
        self.surf.fill("black")
        self.font = pygame.font.SysFont("comicsans", 72)
        self.smaller = pygame.font.SysFont("comicsans", 36)
        

    def draw(self, screen, length):
        self.surf.fill("black")
        self.text = self.font.render("Game Over", True, "white")
        self.text_rect = self.text.get_rect(center=self.surf.get_rect().center)
        self.text_rect.top -= 100
        self.surf.blit(self.text, self.text_rect)
        self.length = self.font.render(str(length), True, "white")
        self.length_rect = self.length.get_rect(
            top=self.text_rect.bottom, centerx=self.text_rect.centerx
        )
        self.restart = self.smaller.render("Press R to restart", True, "white")
        self.r_rect = self.restart.get_rect(
            top = self.length_rect.bottom, centerx = self.length_rect.centerx
        )

        self.surf.blit(self.length, self.length_rect)
        self.surf.blit(self.restart, self.r_rect)
        screen.blit(self.surf, self.surf.get_rect())
