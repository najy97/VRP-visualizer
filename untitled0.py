import pygame
from pygame.locals import *
from pygame.rect import *

import numpy as np

import Vehicle

target_node = [[0,0],[500,500],[200,50],[300,500]]

size = width, height = 800,600
screen = pygame.display.set_mode(size)
 
vehicle = Vehicle.Vehicle(screen,[500,500],target_node)
# vehicle2 = Vehicle.Vehicle(screen,[600,0],[0,0])


clock = pygame.time.Clock()
 
pygame.init()
 
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
    screen.fill((127, 127, 127))
    # vehicle2.move()
    vehicle.move()
    pygame.display.flip()
    print('target', vehicle.targets[0])
    print('current:',vehicle.node_current)
    vehicle.isArrived()
    # if(vehicle.isArrived()):
    #     running = False

 
pygame.quit()