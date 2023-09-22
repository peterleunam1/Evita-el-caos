import pygame
import os 
WIDTH, HEIGHT = 1000, 600
WHITE = (255, 255, 255)
PURPLE=(17,9,24,255)
RED = (255, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
assets_folder = os.path.join(os.path.dirname(__file__), '..', 'assets')