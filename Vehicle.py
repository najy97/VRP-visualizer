import pygame
from pygame.locals import *
from pygame.rect import *

import numpy as np

class Vehicle():
    def __init__(self,screen,start,target,rad=25):
        self.rad=rad
        self.completes = 0
        self.speed = 10
        self.node_current = np.array(start)
        self.targets = np.array(target)
        self.set_target()
        
        self.vehicle = Rect(list(self.node_current-[rad,rad])+[2*rad,2*rad])
        self.screen = screen
        
        pygame.draw.ellipse(self.screen,(0, 0, 255),self.vehicle)
        
    def move(self):
        if len(self.targets)!=0:
            self.set_target()
            self.vehicle.move_ip(self.velocity)
            self.node_current = self.vehicle.center
        pygame.draw.ellipse(self.screen,(0, 0, 255),self.vehicle)
        
        
    def isArrived(self):
        if len(self.targets)!=0:
            distance = self.node_current - self.targets[0]
            distance = np.linalg.norm(distance)
            if distance < self.speed:
                self.completes+=1
                if len(self.targets==0):
                    self.targets=self.targets[1:]
                else : 
                    return True
            else:
              return False
        else:
            return True
    
    def set_target(self):
        self.velocity = (np.array(self.targets[0])-np.array(self.node_current)+[0.0001,0.0001])
        self.velocity = list((self.velocity/np.linalg.norm(self.velocity))*self.speed)

