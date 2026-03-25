import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")

bg_color = (58, 58, 58)

image = pygame.image.load("background.png")

image = pygame.transform.scale(image, (300, 300))

image_rect = image.get_rect(center=(250, 250))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_color)

    screen.blit(image, image_rect)

    pygame.display.update()