import pygame
from pygame.locals import *
from pygame.rect import *

import numpy as np

class Vehicle():
    def __init__(self,screen,start,target,rad=25):
        self.completes = 0
        self.speed = 10
        self.node_current = np.array(start)
        self.targets = np.array(target)
        self.set_target()
        
        self.vehicle = Rect(list(self.node_current-[rad,rad])+[2*rad,2*rad])
        self.screen = screen
        
        pygame.draw.ellipse(self.screen,(0, 0, 255),self.vehicle)
        
    def move(self):
        self.vehicle.move_ip(self.velocity)
        self.node_current = self.vehicle.center
        pygame.draw.ellipse(self.screen,(0, 0, 255),self.vehicle)
        
    def isArrived(self):
        distance = self.node_current - self.targets[0]
        distance = np.linalg.norm(distance)
        print('distance',distance)
        if distance < self.speed:
            self.targets=self.targets[1:]
            self.set_target()
            self.completes+=1
            print('completes:',self.completes)
            return True
        else:
            return False
    
    def set_target(self):
        self.velocity = (self.targets[0]-self.node_current)
        self.velocity = list((self.velocity/np.linalg.norm(self.velocity))*self.speed)
