import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("space")
mySprite = codesters.Sprite("cardinal", 0,0)

x = 0
while(True) :
    x+=1
    mySprite.rotate_about(x,0,0)
#mySprite.say("BTW i use arch")