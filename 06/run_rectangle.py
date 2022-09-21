from pico2d import *

open_canvas()

# fill here

close_canvas()

from pico2d import *
open_canvas()
grass = load_image('grass.png')
character=load_image('character.png')


x=0
while(x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x=x+2
    delay(0.01)
   
y=90
while(y<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(800,y+90)
    y=y+2
    delay(0.01)
     
x=80
while(x>0):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,800)
    x=x-2
    delay(0.01)
    
y=800
while(y>90):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(0,y)
    y=y-2
    delay(0.01)
    


    

grass.draw_now(400,30)
character.draw_now(400, 90)

delay(5)

close_canvas()
