from PPlay.sprite import *
from Scripts.E_states import State



class Player:
    sp = 0.15
    state = State.IDLE
    animacoes = []

    def __init__(self, wind):
        self.animacoes = [
            Sprite("Images\\Player\\Idle.png", 1),
            Sprite("Images\\Player\\Walk.png", 6),
            Sprite("Images\\Player\\Crouch.png", 3),
            Sprite("Images\\Player\\Jab.png", 2)
        ]

        self.configAnimations()

        self.x = self.get_sprite().x
        self.y = self.get_sprite().y

        self.screenH = wind.height
        self.screenW = wind.width

    def configAnimations(self):
        self.get_sprite_byName(State.WALK).set_total_duration(4000*self.sp)
        self.get_sprite_byName(State.CROUCH).set_total_duration(500)
        #self.get_sprite_byName(State.CROUCH).set_loop(False)

        self.get_sprite_byName(State.JAB).set_total_duration(500)
        #self.get_sprite_byName(State.JAB).set_loop(False)

        self.get_sprite_byName(State.IDLE).set_total_duration(10000)

    def set_state(self, state):
        x = self.get_sprite().x
        y = self.get_sprite().y

        self.state = State(state)

        self.get_sprite().x = x
        self.get_sprite().y = y

    def get_sprite_byName(self, sprite):
        return self.animacoes[sprite.value[0]]

    def get_sprite(self):
        return self.animacoes[self.state.value[0]]

    def move_key_x(self, speed):
        currSprite = self.get_sprite()
        currSprite.move_key_x(speed)

    def move_key_y(self, y):
        self.get_sprite().move_key_y(y)

    def get_y(self):
        return self.get_sprite().y

    def get_x(self):
        return self.get_sprite().x

    def set_x(self, x):
        self.get_sprite().x = x
        
    def set_y(self, y):
        self.get_sprite().y = y

    def move(self):
        if self.get_x() >= 0 or self.get_x() <= self.screenW:
            self.move_key_x(self.sp)
        if self.get_y() >= self.screenH - (self.screenH*0.25) or self.get_y() <= self.screenH:
            self.get_sprite().move_key_y(self.sp)
        

    def draw(self):
        self.get_sprite().draw()
        self.get_sprite().update()