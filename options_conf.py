import pygame


class OptionsConf:
    selected_option = 'low'
    show_options = False


    def draw_dropdown_menu(self, title, items, selected_item, pos_x, pos_y, get_font, WIN):
        # Render options title
        options_menu_text_background = pygame.transform.scale(pygame.image.load("assets/btn_background_2.png"), (350, 350))
        options_menu_text_background_rect = options_menu_text_background.get_rect(center=(200,115))
        WIN.blit(options_menu_text_background, options_menu_text_background_rect)
        options_title_text = get_font(25).render("OPTIONS MENU", True, "White")
        options_title_rect = options_title_text.get_rect(center=(200, 90))
        WIN.blit(options_title_text, options_title_rect)

        # Render dropdown menu title
        options_background = pygame.transform.scale(pygame.image.load("assets/btn_background_1.png"), (300, 300))
        options_background_rect = options_background.get_rect(center=(pos_x,pos_y))
        WIN.blit(options_background, options_background_rect)
        title_text = get_font(15).render(title, True, "White")
        title_rect = title_text.get_rect(center=(pos_x, pos_y - 20))
        WIN.blit(title_text, title_rect)

        # Render selected item
class Slider:
    def __init__(self, pos: tuple, size: tuple, initial_val: float, min_val: int, max_val: int) -> None:
        self.pos = pos
        self.size = size
        self.min_val = min_val
        self.max_val = max_val

        self.slider_left_pos = self.pos[0] - (self.size[0] // 2)
        self.slider_right_pos = self.pos[0] + (self.size[0] // 2)
        self.slider_top_pos = self.pos[1] - (self.size[1] // 2 + 50)

        # Calculate initial position of the button based on initial value
        self.initial_val = initial_val
        self.button_x = self.slider_left_pos + (self.slider_right_pos - self.slider_left_pos) * self.initial_val
        self.button_rect = pygame.Rect(self.button_x - 5, self.slider_top_pos, 10, self.size[1])

        self.dragging = False

    def update(self, events):
        for event in events:
          if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
               if self.button_rect.collidepoint(event.pos):
                    self.dragging = True
          elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
               self.dragging = False
          elif event.type == pygame.MOUSEMOTION and self.dragging:
               # Update button position while dragging
               new_button_x = event.pos[0]
               # Clamp button position to slider bounds
               new_button_x = max(self.slider_left_pos, min(self.slider_right_pos, new_button_x))
               self.button_x = new_button_x
               # Update button rectangle
               self.button_rect.x = self.button_x - 5

    def get_value(self):
        # Calculate value based on button position
        return (self.button_x - self.slider_left_pos) / (self.slider_right_pos - self.slider_left_pos)

    def render(self, WIN):
        # Draw slider container
        pygame.draw.rect(WIN, (0, 0, 0), (self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1]))
        # Draw slider button
        pygame.draw.rect(WIN, (255, 255, 255), self.button_rect)





