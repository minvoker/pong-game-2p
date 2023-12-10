import pygame

class Slab:
    def __init__(self, window, size, pos, player, minPos, maxPos):
        self.window = window
        self.size = size
        self.pos = pos
        self.player = player # p 1 or 2
        self.minPos = minPos
        self.maxPos = maxPos
        self.moveSpeed = 1.5
        
    def draw(self):
        pygame.draw.rect(self.window, (255, 255, 255), (self.pos[0], self.pos[1], self.size[0], self.size[1]))
        
    def getCoords(self):
        return [self.pos[0], self.pos[1], self.pos[0] + self.size[0], self.pos[1] + self.size[1]]
    
    def updatePos(self):
        keys = pygame.key.get_pressed()
        if self.player == 1:
            if keys[pygame.K_UP] and self.getCoords()[1]> self.minPos[1]:
                self.pos[1] -= self.moveSpeed
            if keys[pygame.K_DOWN] and self.getCoords()[3]< self.maxPos[1]:
                self.pos[1] += self.moveSpeed
        else:
            if keys[pygame.K_w] and self.getCoords()[1]> self.minPos[1]:
                self.pos[1] -= self.moveSpeed
            if keys[pygame.K_s] and self.getCoords()[3]< self.maxPos[1]:
                self.pos[1] += self.moveSpeed

    def getHeight(self):
        return self.size[1]  