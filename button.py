class Button():
    def __init__(self, image, pos, width, height, text_input, font, base_color, hovering_color, elevation=0, hover_radius=10):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.width = width
        self.height = height
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        # Calculate the position of the text to center it within the button background
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        # Manually adjust text position to be centered within button background
        self.text_rect.center = (self.x_pos, self.y_pos - 25)
        self.elevation = elevation
        self.hover_radius = hover_radius

    def update(self, screen):
        if self.image is not None:
            # Adjust button rectangle position based on elevation
            rect_pos = (self.rect.x, self.rect.y - self.elevation)
            screen.blit(self.image, rect_pos)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        # Calculate the center of the button rectangle
        button_center = (self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2)
        # Calculate the distance between the mouse position and the center of the button rectangle
        distance = ((position[0] - button_center[0]) ** 2 + (position[1] - button_center[1]) ** 2) ** 0.5
        # Check if the distance is less than the hover radius
        if distance < self.hover_radius:
            return True
        return False

    def changeColor(self, position):
        if self.checkForInput(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
