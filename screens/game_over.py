import pygame
import sys
from utils.constants import WIDTH, HEIGHT, WHITE, screen

def show_game_over_screen(score):
    text_font = pygame.font.Font("assets/fonts/Arcadia.otf", 20)
    title_font = pygame.font.Font("assets/fonts/Arcadia.otf", 32)
    background_image = pygame.image.load("assets/images/bg.jpg")
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))
    game_over_text = title_font.render("¡Juego terminado!", True, WHITE)  # Cambia "player.font" por "score.font"
    score_text = text_font.render(f"Puntuación: {score.value}", True, WHITE)
    restart_text = text_font.render("Presiona R para jugar de nuevo", True, WHITE)
    quit_text = text_font.render("Presiona Q para salir", True, WHITE)

    screen.blit(game_over_text, (WIDTH // 2 - 170, HEIGHT // 2 - 80))
    screen.blit(score_text, (WIDTH // 2 - 90, HEIGHT // 2 - 10))
    screen.blit(restart_text, (WIDTH // 2 - 190, HEIGHT // 2 + 60))
    screen.blit(quit_text, (WIDTH // 2 - 120, HEIGHT // 2 + 100))

    pygame.display.update()
    waiting_for_key = True

    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
    return False