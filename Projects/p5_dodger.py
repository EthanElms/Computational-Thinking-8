# Section 1 - Setup

import codesters, random
from codesters import StageClass
stage = StageClass()

player = codesters.Sprite("turtle")
player.set_size(0.2)
player.go_to(0,-200)
stage.set_background("winter")
stage.disable_floor()

gameOver = False
lives = 3


# Section 2 - Objects

def falling_object():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("soccerball", x_position, 250)
        object.set_size(0.4)
        object.set_y_speed(-10)
    
stage.event_interval(falling_object, 0.5)

# Section 3 - Collision

def collision(player, object):
    global lives, gameOver

    if object.get_image_name() == "soccerball":
        stage.remove_sprite(object)
        lives -= 1
        if lives == 0:
            gameOver = True
            player.say(f"Out of lives - you lose!",5)
        else:
            player.say(f"{lives} lives",0.5)
        
player.event_collision(collision)



# Section 4 - Controls

# Right Key
def go_right():
    player.move_right(10)
    
player.event_key("right", go_right)
        
# Left Key
def go_left():
    player.move_left(10)
        
player.event_key("left", go_left)

