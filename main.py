import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
map = pygame.image.load("./assets/map.png")
speed = 5
player = pygame.Rect(640,360,50,50)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)






while running:
   
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        player.y -= speed
    if keys[pygame.K_s]:
        player.y += speed
    if keys[pygame.K_q]:
        player.x -= speed
    if keys[pygame.K_d]:
        player.x += speed
    if(player.x<=0):
        player.x = 0
    if(player.x>=1230):
        player.x = 1230
    if(player.y<=0):
        player.y = 0
    if(player.y>=670):
        player.x = 670
    
    
    screen.blit(map,(0,0))
    pygame.draw.rect(screen,(0,0,255),player)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()