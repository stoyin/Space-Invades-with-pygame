import pygame
import sys
from variables import *

from scene import Scene



class Game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        self.running=True
        self.clock=pygame.time.Clock()
        self.scene=Scene(self)
        
    def run(self):
        while self.running:
            self.update()
            self.draw()
        self.close()
    
    def update(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running=False
                
        
        self.scene.update()      
        pygame.display.update()
        self.clock.tick(FPS)
        
        
    def draw(self):
        #self.screen.fill("red")
        self.scene.draw()
       
        
    def close(self):
        pygame.quit()
        sys.exit()

if __name__=="__main__":
    game=Game()
    game.run()