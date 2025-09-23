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
        
        
    def update(self, screen):
        #game_over=0
        #cool=500
        bar_x=self.rect.x
        bar_y=self.rect.bottom+10
        bar_width=self.rect.width
        bar_height=15
        bar_ratio=self.health_remaining/self.health_start
        key=pygame.key.get_pressed()
        time_now=pygame.time.get_ticks()
        self.mask=pygame.mask.from_surface(self.image)

        if key[pygame.K_LEFT] and self.rect.left>=0:
            self.rect.x -=5
        if key[pygame.K_RIGHT]and self.rect.right<=800:
            self.rect.x +=5
        if key[pygame.K_UP] and self.rect.top>=0:
            self.rect.y-=5
        if key[pygame.K_DOWN] and self.rect.bottom<=600:
            self.rect.y+=5
        
        '''
        if key[pygame.K_SPACE] and time_now -self.last_shot>cool:
            laser_fx.play()
        
            bullet=Bullet(self.rect.centerx,self.rect.top)
            bullet_group.add(bullet)
            self.last_shot=time_now
            
          if self.health_remaining <=0 or pygame.sprite.spritecollide(self, enemy_group,True):
            ex=Explosion(self.rect.centerx, self.rect.centery,3)
            exp_group.add(ex)
            self.kill()
            game_over=-1
        return game_over
        
        '''    
            
        pygame.draw.rect(screen, (255,0,0), (bar_x,bar_y,bar_width,bar_height))

        if self.health_remaining >0:
            pygame.draw.rect(screen, (0,255,0), (bar_x,bar_y, bar_width * bar_ratio, bar_height))
            
  
        
      
        
        
        
        
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

                    
        