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

health = 3

# objectlist = []

#object
objectSpeed = random.randint(3,5)
def changespeed():
    objectSpeed = random.randint(3,5)
stage.event_interval(changespeed , 2)

AsteroidList = ["a1","a2","a3"]

def FallingObject():
    object = codesters.Sprite(random.choice(AsteroidList),250,random.randint(-250,250))
    object.set_size(0.5)
    # objectlist.append(object)
    object.set_x_speed(-objectSpeed)

stage.event_interval(FallingObject,3)

#object removing
# def CleanStage(objectlist):
#     for object in objectlist:
#         if (object.get_x() <  -250):
#             stage.remove_sprite(object)
# stage.event_interval(CleanStage(objectlist),5)

def MoveUp():
    if(player.get_y() > 230):
        player.set_y(230)
    player.move_up(5)

def MoveDown():
    if(player.get_y() < -230):
        player.set_y(-230)
    player.move_down(5)

#Collision

def collision(player,object,health):
    print(health)

#player.event_collision(collision(player,object,health))

#controls
player.event_key("w",MoveUp)
player.event_key("s",MoveDown)