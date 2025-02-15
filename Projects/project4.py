#setup
import codesters
import random
from codesters import StageClass

stage = StageClass()
stage.disable_left_wall()
stage.set_background("space2")



player = codesters.Sprite("ShipEngineOn",-120,0)
player.set_size(0.05)


# objectlist = []

#object
objectSpeed = random.randint(2,4)
def changespeed():
    objectSpeed = random.randint(2,4)
stage.event_interval(changespeed , 2)

AsteroidList = ["a1","a2","a3"]

def FallingObject():
    global asteroidLeft

    if (asteroidLeft !=0):
        object = codesters.Sprite(random.choice(AsteroidList),250,random.randint(-250,250))
        object.set_size(0.5)
        object.get_image_name()
        # objectlist.append(object)
        object.set_x_speed(-objectSpeed)
        asteroidLeft -= 1
        print(asteroidLeft)
    if (asteroidLeft == 0):
        if(health > 0):
            player.say(f"you dodged {15-(4-health)} asteroids")
        else:
            player.say("you died")
        
asteroidLeft = 15

stage.event_interval(FallingObject,3)

#object removing
# def CleanStage(objectlist):
#     for object in objectlist:
#         if (object.get_x() <  -250):
#             stage.remove_sprite(object)
# stage.event_interval(CleanStage(objectlist),5)

#Collision

def collision(player, object):
    global health
    if (object.get_image_name() == "a1" or object.get_image_name() == "a2" or object.get_image_name() == "a3"):
        stage.remove_sprite(object)
        if (health != 0):  
            health -= 1
        if (health == 0):
            destroy()
            player = codesters.Sprite("explosion",-180, 0)
        print(health) 
        print("collision")
        if (health == 0):
            player.say("ship destroyed",5)
            print("destroyed")

        else:
            player.say(f"{health} health", 2)
health = 4
player.event_collision(collision)


#movement functions
def MoveUp():
    if(player.get_y() > 230):
        player.set_y(230)
    if(health != 0):
        player.move_up(5)

def MoveDown():
    if(player.get_y() < -230):
        player.set_y(-230)
    if(health != 0):
        player.move_down(5)

def destroy():
    player.goto(-120,0)

#controls
player.event_key("w",MoveUp)
player.event_key("s",MoveDown)
player.event_key("up",MoveUp)
player.event_key("down",MoveDown)