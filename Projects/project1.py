import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("space")

# TLB = Top Left Backgroud

TLB = codesters.Square(100, 100, 200, 'blue')
TRB = codesters.Square(-100, 100, 200, 'pink')
BLB = codesters.Square(-100, -100, 200, 'red')
BRB = codesters.Square(100, -100, 200, 'purple')

# TLS = Top Left Sprite

TLS = codesters.Sprite("Q1", 100, 100)
TLS.set_size(0.25)

TRS = codesters.Sprite("Q2", -100, -100)
TRS.set_size(0.125)

BLS = codesters.Sprite("Q3", 100, -100)
BLS.set_size(0.25)

BRS = codesters.Sprite("Q4", -100, 100)
BRS.set_size(0.125)

# TB Text Background
TB = codesters.Rectangle(0, 220, 100, 35, "black")
Text = codesters.Text("Ethan", 0, 220, "white")

TB = codesters.Rectangle(0, -220, 100, 35, "black")
Text = codesters.Text("Bottom Text", 0, -220, "white")
