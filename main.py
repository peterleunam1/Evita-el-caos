import pygame
import random
import sys
import os
from entities.player import Player
from entities.enemy import Enemy
from utils.helpers import Score
from screens.game_over import show_game_over_screen
from screens.instructions import show_instructions_screen
from utils.constants import WIDTH, HEIGHT, WHITE, assets_folder, screen


pygame.init()
pygame.display.set_caption("Esquiva los obstáculos")


# Cargar imágenes y sonidos
enemy1_img = pygame.image.load(os.path.join(assets_folder, "images", "enemy1.png"))
enemy1_img = pygame.transform.scale(enemy1_img, (120, 120))
enemy2_img = pygame.image.load(os.path.join(assets_folder, "images", "enemy2.png"))
enemy2_img = pygame.transform.scale(enemy2_img, (140, 140))
enemy3_img = pygame.image.load(os.path.join(assets_folder, "images", "enemy3.png"))
enemy3_img = pygame.transform.scale(enemy3_img, (110, 110))
collision_sound = pygame.mixer.Sound(os.path.join(assets_folder, "sounds", "15.mp3"))
game_background_image = pygame.image.load(os.path.join(assets_folder, "images", "bg.jpg"))
game_background_image = pygame.transform.scale(game_background_image, (WIDTH, HEIGHT))


# Estados del juego
show_instructions = True
game_active = False
game_over = False
restart_game = False

# Inicialización de objetos
player = Player()
enemies = []
score = Score()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if game_active:
        screen.blit(game_background_image, (0, 0))
        
        if keys[pygame.K_LEFT]:
            player.move("left")
        if keys[pygame.K_RIGHT]:
            player.move("right")

        current_time = pygame.time.get_ticks()
        if current_time - last_enemy_time > next_enemy_time:

            num_enemies_to_spawn = random.randint(1, 3)  # Modifica la cantidad de enemigos
            spacing = 150 
            for i in range(num_enemies_to_spawn):
                if i == 0:
                    enemy1 = Enemy(enemy1_img, spacing)
                    enemies.append(enemy1)
                elif i == 1:
                    enemy2 = Enemy(enemy2_img, spacing)
                    enemies.append(enemy2)
                elif i == 2:
                    enemy3 = Enemy(enemy3_img, spacing)
                    enemies.append(enemy3)
                spacing += 100  
            last_enemy_time = current_time
            next_enemy_time -= 50

        for enemy in enemies:
            enemy.y += enemy.speed
            screen.blit(enemy.image, (enemy.x, enemy.y))

        for enemy in enemies[:]:
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
                score.increase()

        for enemy in enemies:
            if (player.x < enemy.x + enemy.size and player.x + player.size > enemy.x and
                player.y < enemy.y + enemy.size and player.y + player.size > enemy.y):
                game_active = False
                game_over = True
                collision_sound.play()

        player.move(keys)
        screen.blit(player.image, (player.x, player.y))
        score.display()

        pygame.display.update()

    elif show_instructions:
        show_instructions = not show_instructions_screen()
        game_active = True
        next_enemy_time = 2000
        last_enemy_time = pygame.time.get_ticks()
        enemies = []
        score.value = 0
        player.x = WIDTH // 2 - player.size // 2
        player.y = HEIGHT - 2 * player.size

    elif game_over:
        if restart_game:
            player.x = WIDTH // 2 - player.size // 2
            player.y = HEIGHT - 2 * player.size
            score.value = 0
            enemies = []
            game_active = True
            game_over = False
            restart_game = False
            next_enemy_time = 2000
            last_enemy_time = pygame.time.get_ticks()
        else:
            restart_game = show_game_over_screen(score)

pygame.quit()
sys.exit()