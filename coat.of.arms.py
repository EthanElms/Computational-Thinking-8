###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")


q1 = codesters.Square(-100,100,200, 'DarkSlateBlue')
q2 = codesters.Square(100,100,200, 'LightBlue')
q3 = codesters.Square(-100,-100,200, 'Plum')
q4 = codesters.Square(100,-100,200, 'SlateBlue')


s1 = codesters.Sprite ("flower2", 100, 100)
s2 = codesters.Sprite ("dog", -100, -100)
s2.set_size(0.2)
s3 = codesters.Sprite ("flowers", 100,-100)
s3.set_size(2.0)
s4 = codesters.Sprite("22lana-review1-articleLarge", -100,100)
s4.set_size(0.2)


message1 = codesters.Text ("My name is Ayana",0,220,"red")
message2 = codesters.Text ("live laugh love",0,-220,"black")