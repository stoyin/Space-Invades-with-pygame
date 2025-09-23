import pygame
from background import Back
from entity import Player, Enemy, create_aliens
from utilities import font_30, draw_text




back_img=pygame.image.load("assets\\images\\background.png")
back_img=pygame.transform.scale(back_img ,(800,600))
back_obj=Back(0,0,back_img)

ship=pygame.image.load("assets\\images\\ship.png")
ship=pygame.transform.scale(ship ,(50,50))

oaak=pygame.image.load("assets\\images\\bugy1.png")
oaak=pygame.transform.scale(oaak ,(50,50))

oaak_npc=Enemy(100,100,oaak)

oaak_group=pygame.sprite.Group()
#oaak_group.add(oaak_npc)
create_aliens(3,3,oaak_group,oaak)

player=Player(400,400,5,ship)

class Scene:
    def __init__(self,app):
        self.app=app
       
        oaak_group
        
    def draw(self):
        self.app.screen.fill("yellow")
        #self.app.screen.blit(back_img,(0,0))
        back_obj.draw(self.app.screen)
        player.draw(self.app.screen)
        
        oaak_group.draw(self.app.screen)
        
        draw_text("Let the game begin",font_30, self.app.screen,(255,0,0),200,200)
        
        
        
        
    def update(self):
        oaak_group.update()
        player.update(self.app.screen)