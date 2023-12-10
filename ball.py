import pygame
# SFX
pygame.mixer.init()
scoreSound = pygame.mixer.Sound("score_sound.mp3")
bounceSound = pygame.mixer.Sound("bounce_sound.mp3")
scoreSound.set_volume(0.7)
bounceSound.set_volume(0.4)

class Ball:

    def __init__(self, pos, velocity, window, rad, minCoord, maxCoord):
        self.pos = pos
        self.velocity = velocity
        self.window = window
        self.rad = rad
        self.minCoord = minCoord
        self.maxCoord = maxCoord
        self.score1 = 0
        self.score2 = 0

    def drawBall(self):
        pygame.draw.circle(self.window, (255,)*3, self.pos, self.rad, 0)

    def HorizontalFlip(self):
        self.velocity[0] *= -1.1
        pygame.mixer.Sound.play(bounceSound)

    def VerticalFlip(self):
        self.velocity[1] *= -1.1

    def resetPos(self, resetVelocity):
        self.pos = [600, 300]
        self.velocity = resetVelocity

    def borderCollisionCheck(self):
        if (self.pos[0] <= self.minCoord[0]):  
            self.score2 += 1
            self.resetPos([1,0.3])
            pygame.mixer.Sound.play(scoreSound)

        elif (self.pos[0] >= self.maxCoord[0]):
            self.score1 += 1
            self.resetPos([-1,-0.3])
            pygame.mixer.Sound.play(scoreSound)

        if (self.pos[1] <= self.minCoord[1]) or (self.pos[1] >= self.maxCoord[1]):
            self.VerticalFlip()
            pygame.mixer.Sound.play(bounceSound)
        
    def updatePos(self):
        self.pos = [self.pos[0]+self.velocity[0], self.pos[1]+self.velocity[1]]

    def checkSlabCollision(self, slabPos):  # slab pos = [xmin, ymin, xmax, ymax]
        collideHorizontally = (self.pos[0] + self.rad > slabPos[0] and self.pos[0] - self.rad < slabPos[2])
        collideVertically = (self.pos[1] + self.rad > slabPos[1] and self.pos[1] - self.rad < slabPos[3])

        if collideHorizontally and collideVertically:
            # Check if the ball collided with the sides of the slab
            if self.pos[0] < slabPos[0] or self.pos[0] > slabPos[2]:
                self.HorizontalFlip()

            # Check if the ball collided with the top or bottom of the slab
            if self.pos[1] < slabPos[1] or self.pos[1] > slabPos[3]:
                self.VerticalFlip()


    def getScore(self):
        return [self.score1, self.score2]