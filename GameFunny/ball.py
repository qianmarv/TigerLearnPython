import pgzrun
pgzrun.go()
width=800
height=600
x=width/2
y=height/2
spead_x=3
spead_y=5
r=30
def draw():
    screen.fill('white')
    screen.draw.filled_circle((x,y),r,'red')

def update():
    global x,y,spead_x,spead_y
    x=x+spead_x
    y=y+spead_y
    if x>=width-r or x<=r:
        spead_x=-spead_x
    if y>=height-r or y<=r:
        spead_y=-spead_y
