import pygame
from utils.constants import WHITE, screen

class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font(None, 36)

    def increase(self):
        self.value += 1

    def display(self):
        score_display = self.font.render(f"Puntuación: {self.value}", True, WHITE)
        screen.blit(score_display, (10, 10))
