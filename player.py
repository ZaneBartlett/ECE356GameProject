import pygame


class Player:
    def __init__(self, play_number, is_leader):
        self.vel = 1
        self.number = play_number
        self.leader = is_leader
        self.is_typing = True
        self.last_entered_text = ''
        self.game_number = -1

    def enter_text(self, text, x_pos, y_pos, win):
        font = pygame.font.Font("freesansbold.ttf", 14)
        input_box = pygame.Rect(x_pos, y_pos, 140, 32)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if self.is_typing:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                        self.is_typing = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        # Render the current text.
        txt_surface = font.render(text, True, (255, 255, 255))
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        win.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(win, (255, 255, 255), input_box, 2)

        self.last_entered_text = text

        return self.last_entered_text
