import pygame
import os
from utils.constants import WIDTH, HEIGHT, assets_folder

player_img = pygame.image.load(os.path.join(assets_folder, "images", "player.webp"))
player_img = pygame.transform.scale(player_img, (140, 140))

class Player:
    def __init__(self):
        self.image = player_img
        self.size = 90
        self.x = WIDTH // 2 - self.size // 2
        self.y = HEIGHT - 2 * self.size
        self.speed = 1

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - self.size:
            self.x += self.speed