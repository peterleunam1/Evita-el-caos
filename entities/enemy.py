import random
from utils.constants import WIDTH

class Enemy:
    def __init__(self, image, spacing):
        self.image = image
        self.size = 50
        self.speed = 2
        self.spacing = spacing  # Separación entre enemigos
        self.x = random.randint(0, WIDTH - self.size)
        self.y = 0

