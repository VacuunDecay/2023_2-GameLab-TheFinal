from PPlay.window import *
from PPlay.sprite import *

from Scripts.player import Player
from Scripts.camera import Camera
from Scripts.backGround import backGround
from Scripts.E_states import State

_height = 460
_width = 802

wind = Window(_width, _height)

keyboard = wind.get_keyboard()

jog = Player(wind)
bk = backGround("Images\\beackGround.png")

cam = Camera(bk, jog)

grama = Sprite("Images\\MissingTexture.png")
grama.set_position(200, 200)



while True:
    wind.set_background_color([0,12,24])

   

    jog.move()

    if keyboard.key_pressed("ESC"):
        wind.close()

    if keyboard.key_pressed("LEFT") or keyboard.key_pressed("RIGHT") or keyboard.key_pressed("UP") or keyboard.key_pressed("DOWN"):
        jog.set_state(State.WALK)
    else:
        jog.set_state(State.IDLE)

    if keyboard.key_pressed("Z"):
        jog.set_state(State.JAB)


    if keyboard.key_pressed("LEFT_SHIFT"):
        jog.set_state(State.CROUCH)

    cam.updade()
    cam.draw()

    wind.update()