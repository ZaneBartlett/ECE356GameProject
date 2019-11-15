import pygame

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)


def display_text(text, window, x, y):

    # create font object
    font = pygame.font.Font('freesansbold.ttf', 20)

    # create text surface object
    text = font.render(text, True, white, black)

    # create rectangular object for the text surface
    text_rect = text.get_rect()

    # set center
    text_rect.center = (x // 2, y // 2)

    # copying text surface object to display surface
    window.blit(text, text_rect)
