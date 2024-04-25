import pygame
import sys
from button import Button
from pygame import mixer


class StartScreen:
    def __init__(self, WIDTH, HEIGHT, WIN):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.WIN = WIN

    def start(self):
        mixer.music.stop()
        font = pygame.font.Font("assets/retro_computer_personal_use.ttf", 30)
        timer = pygame.time.Clock()
        messages = ["Esther is so cool!" , "She is the best!", 
                    "She is the best programmer!", "She is the best artist!", 
                    "She is the best friend!", "She is the best person!", "Are you still reading this?",
                      "I hope so cause she put alot of effort into this", "oh..", 
                      "you don't think she's the best?", "well..", 
                      "I guess you're entitled to your own opinion", 
                      "but..", "actually..", "uh..",
                        "ur wrong", "and a hater", "so..", "yeah..", "bye!"]
        snip = font.render("", True, "White")
        counter = 0
        speed = 3
        active_message = 0 
        message = messages[active_message]
        done = False
        typewriter_sound_effect = mixer.Sound("assets/sound_effect_AZ.mp3")
        run = True
        while run:
            start_mouse_pos = pygame.mouse.get_pos()
            self.WIN.fill((0, 0, 0))
            timer.tick(60)
            pygame.draw.rect(self.WIN, "Blue", [0,550,1250,300])
            if counter < speed * len(message):
                counter += 1
                if not pygame.mixer.get_busy():
                        typewriter_sound_effect.play()
            elif counter >= speed * len(message):
                done = True
                typewriter_sound_effect.stop()  # Stop typewriter sound when message is fully displayed


            PLAY_BACK = Button(image=None, pos=(1000, 100), width=500, height=500,
                                text_input="BACK", font=self.get_font(25), base_color="White", hovering_color="Green", elevation=0, hover_radius=50)
            PLAY_BACK.changeColor(start_mouse_pos)
            PLAY_BACK.update(self.WIN)

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_BACK.checkForInput(start_mouse_pos):
                            mixer.music.play(-1)
                            return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and done and active_message < len(messages)-1:
                            
                            active_message += 1
                            done = False
                            message = messages[active_message]
                            counter = 0
                            typewriter_sound_effect.stop()
            snip = font.render(message[0:int(counter // (speed))], True, "White")
            self.WIN.blit(snip, (10, 600))
            pygame.display.flip()

    pygame.quit()
    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/Pixeled.ttf", size)
