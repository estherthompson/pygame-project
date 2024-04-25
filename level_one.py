import pygame
import sys
from scripts.utils import load_image, load_images
from scripts.entities import PhysicsEntity

class LevelOne:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1250, 800))
        self.display = pygame.Surface((625,400))

        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Level One")

        self.movement = [False, False]

        
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png')
        }
        

        print(self.assets)

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))


    def run(self):
        while True:
                self.display.fill((14,219,248))

                self.player.update((self.movement[1]- self.movement[0], 0))
                self.player.render(self.display)
                

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.movement[0] = True
                        if event.key == pygame.K_RIGHT:
                            self.movement[1] = True
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            self.movement[0] = False
                        if event.key == pygame.K_RIGHT:
                            self.movement[1] = False

                
                self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
                pygame.display.update()
                self.clock.tick(60)

LevelOne().run()