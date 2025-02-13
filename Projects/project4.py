#setup
import codesters
import time
import random
from codesters import StageClass
stage = StageClass()
stage.disable_left_wall()


stage.set_background("space2")

player = codesters.Sprite("ShipEngineOn",-120,0)
player.set_size(0.05)

objectSpeed = 10

AsteroidList = ["a1","a2","a3"]

def FallingObject():
    x = random.choice(AsteroidList)
    object = codesters.Sprite(x,250,random.randint(-250,250))

    object.set_x_speed(objectSpeed)

def MoveUp():
    if(player.get_y() > 230):
        player.set_y(230)
    player.move_up(5)

def MoveDown():
    if(player.get_y() < -230):
        player.set_y(-230)
    player.move_down(5)

player.event_key("w",MoveUp)
player.event_key("s",MoveDown)

stage.event_interval(FallingObject,4)