#
import pygame
from math import pi
#
pygame.init()
#
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
pygame.init()
#
size = (100, 100)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
#
done = False
#
clock = pygame.time.Clock()
#
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(20)
    screen.fill(white)
    #pygame.draw.ellipse(screen, (255, 230, 0), (15, 10, 70, 70), 0)
    pygame.draw.rect(screen, (150, 150 ,150), (40, 20, 21, 22), 0)
    pygame.draw.line(screen, black, [50, 43], [50, 75], 3)
    pygame.draw.line(screen, black, [43, 57], [49, 75], 3)
    pygame.draw.line(screen, black, [57, 57], [51, 75], 3)
    pygame.draw.line(screen, black, [50, 25], [50, 37], 3)
    pygame.draw.line(screen, black, [45, 29], [55, 29], 3)
    #Arms
    pygame.draw.line(screen, black, [50, 50], [30, 30], 4)
    pygame.draw.line(screen, black, [50, 50], [70, 30], 4)
    #Squares
    pygame.draw.rect(screen, black, (40, 20, 21, 22), 3)
    pygame.draw.rect(screen, white, (43, 44, 15, 16), 0)
    pygame.draw.rect(screen, black, (43, 44, 15, 16), 3)
    #Sun
    pygame.draw.ellipse(screen, (255, 0, 0), (45, 46, 12, 12), 0)
    pygame.draw.ellipse(screen, (255, 230, 0), (46, 47, 10, 10), 0)
    
    
pygame.quit()