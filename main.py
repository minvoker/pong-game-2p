from ball import Ball
from slab import Slab
import pygame
# Improvements: collision system(corners of slabs), ball physics
# Setup 
WIDTH = 1200
HEIGHT = 700
BLACK = (0,0,0)
WHITE = (255,)*3
FPS = 400

pygame.init()
pygame.display.set_caption('Pong')
window = pygame.display.set_mode((WIDTH, HEIGHT ))
clock = pygame.time.Clock()  
font = pygame.font.Font(None, 46) 

ball  = Ball([400,300], [0.7,0.4], window, 10, (0,0), (WIDTH,HEIGHT))
slab  = Slab(window, [15,100], [1150,300], 1, (0,0), (600,HEIGHT))
slab2 = Slab(window, [15,100], [50,300], 2, (0,0), (600,HEIGHT))

print("Controls: (W/S) Player 1 | (UP/DOWN) Player 2")
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    scores = ball.getScore()
    p1score = font.render(str(scores[0]), True, WHITE)
    p2score = font.render(str(scores[1]), True, WHITE)

    keys = pygame.key.get_pressed()
    window.fill(BLACK)
    window.blit(p1score, (WIDTH // 4, 50))
    window.blit(p2score, (WIDTH * 3 // 4, 50))  

    ball.borderCollisionCheck()
    ball.checkSlabCollision(slab.getCoords())
    ball.checkSlabCollision(slab2.getCoords())
    ball.updatePos()
    ball.drawBall()

    slab.updatePos()
    slab.draw()
    slab2.updatePos()
    slab2.draw()

    pygame.display.update()

pygame.quit()