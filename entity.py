import pygame



class Player(pygame.sprite.Sprite):
    def __init__(self, x,y,health,image):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()#geting sprite position (x,y) #MAIN CHARACTER, NPC
        self.rect.center=[x,y]
        self.last_shot=pygame.time.get_ticks()
        self.health_start=health
        self.health_remaining=health
    
    def draw(self, screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
        
        
        
        
class Enemy(pygame.sprite.Sprite):
            def __init__(self, x,y,image):
                pygame.sprite.Sprite.__init__(self)
                self.image=image
                self.rect=self.image.get_rect()
                self.rect.center=[x,y]
                self.move_dir=1
                self.counter=0


            def update(self):
               
                self.rect.x +=self.move_dir
                self.counter+=1
                #print(self.rect.x)
                if abs(self.counter)>250:
                    self.move_dir *= -1
                    self.counter*=self.move_dir
                if abs(self.counter)<=0:
                    self.move_dir *=-1
                    self.counter *=self.move_dir
        
def create_aliens(rows, cols, alien_group,image):
    for x in range(rows):
        for y in range(cols):
            enemy=Enemy(50+y*100,100+x*70,image)
            alien_group.add(enemy)

                    
        