from PPlay.window import *
from PPlay.sprite import *

_height = 455
_width = 802

wind = Window(_width, _height)

keyboard = wind.get_keyboard()

img = Sprite("image.png")

palette = [[(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0)],
            [(0, 0, 0), (128, 128, 128), (255, 128, 0), (0, 255, 255)]]
# Define more palettes as needed

def apply_palette(img, pale):
    img = pygame.image.load(img)
    new_ima = img.copy()

    for x in range(new_ima.get_width()):
        for y in range(new_ima.get_height()):
            pix_color = img.get_at((x, y))
            if pix_color == (27, 27, 27):
                new_color = pale[0]
            elif pix_color == (91, 91, 91):
                new_color = pale[1]
            elif pix_color == (168, 168, 168):
                new_color = pale[2]
            elif pix_color == (255, 255, 255):
                new_color = pale[3]
            else:
                new_color = pix_color
            
            new_ima.set_at((x, y), new_color)
    
    return new_ima
cur_palette = 0

while True:
    wind.set_background_color([0,12,24])

    


    #Inputs
    if keyboard.key_pressed("1"):
        cur_palette = 0
        img.image = apply_palette("image.png", palette[cur_palette])
    if keyboard.key_pressed("2"):
        cur_palette = 1
        nimg = apply_palette("image.png", palette[cur_palette])
        img.image = nimg

    if keyboard.key_pressed("ESC"):
        wind.close()

    img.draw()

    wind.update()