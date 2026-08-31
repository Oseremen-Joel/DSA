import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class Leaderboard:
    def __init__(self, max):
        self.capacity = 10
        self.size = 0
        self.page = 0
        self.players = []
    
    def Add(self, name, score):
        if self.size == self.capacity:
            return False
        self.players[self.size] = [name, score]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.display.flip()

    clock.tick(60)
