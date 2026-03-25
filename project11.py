import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

bg_color = (0, 0, 0)          
rect_color = (0, 255, 0)     
text_color = (255, 255, 255)  

font = pygame.font.Font(None, 36)

text = font.render("Hello, Pygame!", True, text_color)
text_rect = text.get_rect(center=(320, 50))

rect_width = 200
rect_height = 100
rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_color)

    pygame.draw.rect(screen, rect_color, rectangle)

    screen.blit(text, text_rect)
    
    pygame.display.update()
