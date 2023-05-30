import pygame

import random

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Awesome Game")

x = 0
y = 0
width = 25
height = 25
vel = 25

positionX = random.randrange(0, 475, 25)

positionY = random.randrange(0, 475, 25)


run = True
while run:

    pg = pygame
    pygame.time.delay(100)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    for i in range(1):
        if keys[pygame.K_LEFT]:
            for i in range(1):
                x -= vel
        elif keys[pygame.K_RIGHT]:
            for i in range(1):
                x += vel
        elif keys[pygame.K_UP]:
            for i in range(1):
                y -= vel
        elif keys[pygame.K_DOWN]:
            for i in range(1):
                y += vel

    for i in range(1):
        win.fill((0, 0, 0))

    if x < 0:
        x = 475
    elif x > 475:
        x = 0

    if y < 0:
        y = 475
    elif y > 475:
        y = 0



    snakeimg = pg.image.load('snake.png')
    width2 = snakeimg.get_rect().width
    height2 = snakeimg.get_rect().height

  
    rect = snakeimg.get_rect()
    rect.center = (x, y)
    image = pygame.transform.scale(snakeimg,(int(width2*0.5), int(height2*0.5)))
    
    pygame.Surface.blit(win, image, (x - 117, y - 85))




    apple = pygame.draw.rect(win, (255, 0, 0), (positionX, positionY, width, height))

    snake = pygame.draw.rect(win, (255, 255, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
