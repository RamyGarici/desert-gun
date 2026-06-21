import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

map = pygame.image.load("./assets/map.png")
pistol_asset = pygame.image.load("./assets/weapons.png")
player_asset = pygame.image.load("./assets/perso.png")

player_right = player_asset.subsurface(0, 64, 32, 32)
player_left = player_asset.subsurface(0, 32, 32, 32)
player_up = player_asset.subsurface(0, 96, 32, 32)
player_down = player_asset.subsurface(0, 0, 32, 32)

scaled_pistol = pistol_asset.subsurface((0, 80, 64, 25))
scaled_pistol = pygame.transform.scale(scaled_pistol, (32, 12))

speed = 5
angle = 0
current_sprite = player_right

player = pygame.Rect(640, 360, 32, 32)
bullets = []
bullet_speed = 10
obstacles = [
    pygame.Rect(105, 80, 250, 227), 
    pygame.Rect(60, 430, 230, 200), 
    pygame.Rect(70, 310, 63, 40), 
    pygame.Rect(624, 10, 350, 180), 
   
]

while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    dx = mouse_x - (player.x + 16)
    dy = mouse_y - (player.y + 16)
    
   
    if abs(dx) > abs(dy):
        if dx > 0:
            current_sprite = player_right
            angle = 0
        else:
            current_sprite = player_left
            angle = 180
    else:  
        if dy > 0:
            current_sprite = player_down
            angle = 270
        else:
            current_sprite = player_up
            angle = 90

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
              
                if angle == 0:
                    dir_x, dir_y = 1, 0
                elif angle == 180:
                    dir_x, dir_y = -1, 0
                elif angle == 90:
                    dir_x, dir_y = 0, -1
                elif angle == 270:
                    dir_x, dir_y = 0, 1
                    
                bullets.append({
                    "x": player.x + 16,
                    "y": player.y + 16,
                    "dx": dir_x,
                    "dy": dir_y,
                })


    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]: 
        player.y -= speed
        for obstacle in obstacles:
            if player.colliderect(obstacle):
                player.y += speed
    if keys[pygame.K_s]: 
        player.y += speed
        for obstacle in obstacles:
            if player.colliderect(obstacle):
                player.y -= speed
    if keys[pygame.K_q]: 
        player.x -= speed
        for obstacle in obstacles:
            if player.colliderect(obstacle):
                player.x += speed
    if keys[pygame.K_d]: 
        player.x += speed
        for obstacle in obstacles:
            if player.colliderect(obstacle):
                player.x -= speed

    if player.x < 0: player.x = 0
    if player.x > 1248: player.x = 1248
    if player.y < 0: player.y = 0
    if player.y > 688: player.y = 688
    

    screen.blit(map, (0, 0))
    screen.blit(current_sprite, player)


    rotated_pistol = pygame.transform.rotate(scaled_pistol, angle)


    center_x = player.x + 16
    center_y = player.y + 16


    if angle == 0:     
        center_x += 15
        center_y += 4    
    elif angle == 180:   
        center_x -= 15
        center_y += 4
    elif angle == 90: 
        center_y -= 15   
    elif angle == 270:   
        center_y += 15   


    pistol_rect = rotated_pistol.get_rect(center=(center_x, center_y))
    screen.blit(rotated_pistol, pistol_rect.topleft)
    

    for bullet in bullets:
        bullet["x"] += bullet_speed * bullet["dx"]
        bullet["y"] += bullet_speed * bullet["dy"]
        pygame.draw.rect(screen, (255, 255, 0), (bullet["x"], bullet["y"], 8, 8))
    for obstacle in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), obstacle, 2)
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()