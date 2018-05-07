import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Racing')
display_width = 800
display_height = 600
clock = pygame.time.Clock()
crashed = False
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
raceCar = pygame.image.load('Sprites/RaceCar.png')
highWay = pygame.image.load('Sprites/Highway.png')
car_x = 380
car_y = 450
x_change = 0
def car(x,y):
    gameDisplay.blit(raceCar, (x,y))


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -15
            elif event.key == pygame.K_RIGHT:
                x_change = 15
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    car_x += x_change
    gameDisplay.blit(highWay, (0,0))
    car(car_x, car_y)
    pygame.display.update()
    clock.tick(60)
