import pygame
pygame.font.init()

green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)

font_30=pygame.font.SysFont(None, 30)
font_40=pygame.font.SysFont(None, 40)

def draw_text(text, font,screen, text_col,x,y):
    img=font.render(text,True, text_col)
    screen.blit(img,(x,y))