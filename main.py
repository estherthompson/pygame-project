import pygame, sys
from button import Button
from pygame import mixer
import options_conf

pygame.init()

WIDTH, HEIGHT = 1250, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Load background image
BG = pygame.transform.scale(pygame.image.load("assets/apartment_night.png"), (WIDTH, HEIGHT))
# Load button background image
button_background = pygame.transform.scale(pygame.image.load("assets/btn_background_2.png"), (300, 300))

mixer.music.load("assets/background_music.mp3")    
mixer.music.play(-1)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/Pixeled.ttf", size)


def start():
    mixer.music.stop()
    while True:
        start_mouse_pos = pygame.mouse.get_pos()
        WIN.fill((0, 0, 0))

        PLAY_BACK = Button(image=None, pos=(640, 460), width=500, height=500,
                            text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(start_mouse_pos)
        PLAY_BACK.update(WIN)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(start_mouse_pos):
                        mixer.music.play(-1)
                        main_menu()

        pygame.display.update()
def options():

    user_name = "Player"  # Default username

    graphics = [("Low", "low"), 
                ("Medium", "medium"), 
                ("High", "high"), 
                ("Ultra High", "ultra high")] 
  
    # List that is displayed while selecting the window resolution level 
    resolution = [("800x600", "800x600"),
                    ("1024x768", "1024x768"),
                  ("1280x720", "1280x720"),
                  ("1440x900", "1440x900")] 
  
    # List that is displayed while selecting the difficulty 
    difficulty = [("Easy", "Easy"), 
                  ("Medium", "Medium"), 
                  ("Expert", "Expert")] 

    selected_graphics = graphics[0][1]
    selected_resolution = resolution[0][1]
    selected_difficulty = difficulty[0][1]
    music_volume = 0.5  # Default music volume
    # Define other settings variables here with their default values

    music_slider = options_conf.Slider(pos=(500, 630), size=(200, 20), initial_val=music_volume, min_val=0, max_val=1)
    # Create a list of tuples for each option in the options menu

    options_conf_instance = options_conf.OptionsConf()  # Create an instance of the OptionsConf class

    while True: 
        options_mouse_pos = pygame.mouse.get_pos()

        opBg = pygame.transform.scale(pygame.image.load("assets/op_bg.png"), (WIDTH, HEIGHT))

        # Clear the screen
        WIN.blit(opBg, (0, 0))  # Blue background for options menu  


        # Update the music slider with mouse events
        music_slider.update(pygame.event.get())

        volume = music_slider.get_value()
        mixer.music.set_volume(volume)

        # Render music slider
        music_slider.render(WIN)

        # Draw dropdown menus
        options_conf_instance.draw_dropdown_menu("Graphics Level:", graphics, selected_graphics, 200, 225, get_font, WIN)
        options_conf_instance.draw_dropdown_menu("Window Resolution:", resolution, selected_resolution, 200, 350, get_font, WIN)
        options_conf_instance.draw_dropdown_menu("Difficulty:", difficulty, selected_difficulty, 200, 475, get_font, WIN)
        options_conf_instance.draw_dropdown_menu("Music Volume:", [], str(round(volume * 100)) + "%", 200, 600, get_font, WIN)

        # Render and update the back button
        options_back = Button(image=button_background, pos=(WIDTH // 2, HEIGHT - 100), width=200, height=50,
                              text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green", elevation=5, hover_radius=50)
        options_back.changeColor(options_mouse_pos)
        options_back.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_back.checkForInput(options_mouse_pos):
                    print("Back button clicked")
                    main_menu()
        pygame.display.update()

def main_menu():
    pygame.display.set_caption("Main Menu")

                
    while True:
        events = pygame.event.get()

        WIN.blit(BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()
        menu_text = get_font(75).render("UNTITLED PROJECT", True, "WHITE")
        menu_rect = menu_text.get_rect(center=(640, 100))

        start_button = Button(image=button_background, pos=(640, 350), width=500, height=500,
                            text_input="PLAY", font=get_font(25), base_color="#d7fcd4", hovering_color="Blue", elevation=5, hover_radius=50)
        options_button = Button(image=button_background, pos=(640, 500), width=500, height=500,
                                text_input="OPTIONS", font=get_font(25), base_color="#d7fcd4", hovering_color="Blue", elevation=5, hover_radius=50)    
        exit_button = Button(image=button_background, pos=(640, 650), width=500, height=500,
                            text_input="QUIT", font=get_font(25), base_color="#d7fcd4", hovering_color="Blue", elevation=5, hover_radius=50)

        WIN.blit(menu_text, menu_rect)
        
        for button in [start_button, options_button, exit_button]:

                button.changeColor(menu_mouse_pos)
                button.update(WIN)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.checkForInput(menu_mouse_pos):
                        start()
                    if options_button.checkForInput(menu_mouse_pos):
                        options()
                    if exit_button.checkForInput(menu_mouse_pos):
                        print("Quit button clicked")
                        pygame.quit()
                        sys.exit()

        pygame.display.update()


main_menu()

