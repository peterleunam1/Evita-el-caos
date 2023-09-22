import pygame
import os
import sys 
from utils.constants import WIDTH, HEIGHT, screen, assets_folder, RED, WHITE, PURPLE

def show_instructions_screen():
    background = pygame.image.load(os.path.join(assets_folder, "images", "inner.jpg"))
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    screen.blit(background, (0, 0))

    # Fuente y colores
    title_font = pygame.font.Font("assets/fonts/Arcadia.otf", 60)
    subtitle_font = pygame.font.Font(None, 25)
    instructions_font = pygame.font.Font("assets/fonts/Arcadia.otf", 20)
    #agregar otro tipo de fuente

    # Textos
    title_text = title_font.render("¡Esquiva los obstáculos!", True, PURPLE)
    description_title_text = instructions_font.render("Instrucciones:", True, WHITE)
    description_text1 = instructions_font.render("- Usa las teclas izquierda y derecha para moverte", True, WHITE)
    description_text2 = instructions_font.render("- Esquiva los obstáculos que caen", True, WHITE)
    subtitle_text = subtitle_font.render("Presiona cualquier tecla para empezar", True, RED)

    # Posiciones centradas
    title_rect = title_text.get_rect(center=(WIDTH // 2, 150))
    subtitle_rect = subtitle_text.get_rect(center=(WIDTH // 2, 300))
    description_title_rect = description_title_text.get_rect(center=(WIDTH // 2, 400))
    description_text1_rect = description_text1.get_rect(center=(WIDTH // 2, 450))
    description_text2_rect = description_text2.get_rect(center=(WIDTH // 2, 500))

    # Dibujar textos en pantalla
    screen.blit(title_text, title_rect)
    screen.blit(subtitle_text, subtitle_rect)
    screen.blit(description_title_text, description_title_rect)
    screen.blit(description_text1, description_text1_rect)
    screen.blit(description_text2, description_text2_rect)

    pygame.display.update()

    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return True
    return False