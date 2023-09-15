from enum import Enum


class State(Enum):
    IDLE = 0,
    WALK = 1,
    CROUCH = 2,
    JAB = 3,
    PU = 4