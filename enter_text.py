import pygame as pg


def enter_text(text, x_pos, y_pos, win):
    font = pg.font.Font("freesansbold.ttf", 14)
    input_box = pg.Rect(x_pos, y_pos, 140, 32)
    active = True
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                        active = False
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        # Render the current text.
        txt_surface = font.render(text, True, (255, 255, 255))
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        win.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(win, (255, 255, 255), input_box, 2)
        return text


