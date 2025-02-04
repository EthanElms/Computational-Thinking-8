import codesters
from codesters import StageClass
stage = StageClass()


stage.set_background("moon")
s1 = codesters.Sprite("person1", 0,-200)
s1.set_size(0.5)

speed = 2


def move_up(sprite):
    sprite.move_up(speed)


def move_down(sprite):
    sprite.move_down(speed)

def move_left(sprite):
    sprite.move_left(speed)

def move_right(sprite):
    sprite.move_right(speed)

def hide(sprite):
   sprite.hide()

def show(sprite):
   sprite.show()

def turn_left(sprite):
    heading = sprite.heading
    sprite.set_heading(heading + 1)

def turn_right(sprite):
    heading = sprite.heading
    sprite.set_heading(heading - 1)



def erase(sprite):
    sprite.pen_clear()

def pen_up(sprite):
    sprite.pen_up()

def pen_down(sprite):
    sprite.pen_down()

def red_pen(sprite):
    sprite.set_color("red")

def black_pen(sprite):
    sprite.set_color("black")




s1.event_key("w", move_up)
s1.event_key("s", move_down)
s1.event_key("a", move_left)
s1.event_key("d", move_right)

s1.event_key("up", move_up)
s1.event_key("down", move_down)
s1.event_key("left", move_left)
s1.event_key("right", move_right)

s1.event_key("h", hide)
s1.event_key("g", show)

s1.event_key("q", turn_left)
s1.event_key("e", turn_right)


s1.event_key("z", pen_down)
s1.event_key("x", pen_up)

s1.event_key("space", erase)

s1.event_key("e", red_pen)
s1.event_key("q", black_pen)