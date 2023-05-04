from turtle import back
from graphics import graphics
'''
File:guitar_hero.py
Author: Minh Le
Purpose: To animate a guitar player that shines in the middle of his moment

'''
def main():
    '''
    Purpose: Compiles all the various helper functions into the main to create one cohesive 
    animation. It also sets up the inital graphic window for this image.
    '''
    gui=graphics(500,500,"win")
    position =100
    while not gui.is_destroyed(): #The animation loop that allowed the image to "move"
        position +=1
        if position >401:
            position=100
        gui.clear()
        if position ==250: #at half way ,the image changes into the rockstar going off
            background(gui,"True")
            stick_figure(gui, 250,250,"False")
            light(gui,20,20,40,40,"True")
            light(gui,125,20,150,40,"True")
            light(gui,250,20,250,40,"True")
            light(gui,375,20,350,40,"True")
            light(gui,480,20,460,40,"True")
            gui.update_frame(1)
        elif position == 400: # End Celebration
            jumping(gui,position,250)
        elif position %2 ==0: # Allows for the guitar to be animated by alternating the hand position
            background(gui,"False")
            stick_figure(gui,position,250,"False")
            light(gui,20,20,40,40,"False")
            light(gui,125,20,150,40,"False")
            light(gui,250,20,250,40,"False")
            light(gui,375,20,350,40,"False")
            light(gui,480,20,460,40,"False")
        else:
            background(gui,"False")
            stick_figure(gui,position,250,"True")
            light(gui,20,20,40,40,"False")
            light(gui,125,20,150,40,"False")
            light(gui,250,20,250,40,"False")
            light(gui,375,20,350,40,"False")
            light(gui,480,20,460,40,"False")
        gui.update_frame(50)

def jumping(gui,x,y):
    '''
    This makes the end celebration where the guitarist jumps up and down 4 times.
    
    gui: The graphic imported from graphics.py
    x= The current x-position the stick figure is referenced from.
    y= The current y-position the stick figure is referenced from.
    '''
    i=0
    while i <= 8: # Jumping up and down 4 times
        gui.clear()
        if i%2==0:
            background(gui,"True")
            stick_figure(gui, x,y,"False")
            light(gui,20,20,40,40,"False")
            light(gui,125,20,150,40,"False")
            light(gui,250,20,250,40,"False")
            light(gui,375,20,350,40,"False")
            light(gui,480,20,460,40,"False")
        else: # Stick figure in the air
            background(gui,"True") 
            light(gui,20,20,40,40,"True")
            light(gui,125,20,150,40,"True")
            light(gui,250,20,250,40,"True")
            light(gui,375,20,350,40,"True")
            light(gui,480,20,460,40,"True")
            gui.ellipse(x,y-100,20,20,"white")
            gui.line(x,y-90,x,y-20,"black",1)
            gui.line(x,y-80,x-20,y-120,"black",1)
            gui.line(x,y-80,x+20,y-120,"black",1)
            gui.line(x,y-20,x-20,y,"black",1)
            gui.line(x,y-20,x+20,y,"black",1)
        gui.update_frame(5)
        i+=1

def background(gui,on):
    '''
    This decides what time of backlighting the canvas has.

    gui:The graphic imported from graphics.py
    on: Boolean that decides if the lights is shining
    '''
    if on == "True":
        gui.rectangle(0,0,500,500,"pale goldenrod")
        gui.rectangle(0,350,500,150,"chocolate3")
        gui.rectangle(0,350,500,10,"grey13")
    else:
        gui.rectangle(0,0,500,500,"grey")
        gui.rectangle(0,350,500,150,"chocolate3")
        gui.rectangle(0,350,500,10,"grey13")

def stick_figure(gui,x,y,up):
    '''
    The standard stick figure... Essentially the helper function the
    same way the tiles were in the pipes_static_A.py

    This makes the end celebration where the guitarist jumps up and down 4 times.
    
    gui: The graphic imported from graphics.py
    x= The current x-position the stick figure is referenced from. Also allows it to move across
    y= The current y-position the stick figure is referenced from.
    '''
    gui.ellipse(x,y,20,20,"white")
    gui.line(x,y+10,x,y+70,"black",1)
    guitar(gui,x,y) # guitar helper function to make the function a little shorter
    gui.line(x,y+20,x-20,y+50,"black",1)
    gui.line(x,y+20,x+20,y+50,"black",1)
    if up =="True": # Moving the hand of the guitar
        gui.line(x-20,y+50,x-10,y+45,"black")
    else:
        gui.line(x-20,y+50,x-10,y+55,"black",1)
    gui.line(x+20,y+50,x+30,y+22,"black",1)
    gui.line(x,y+70,x-20,y+100,"black")
    gui.line(x,y+70,x+20,y+100,"black")
    
def guitar(gui,x,y):
    '''
    Drawing the guitar from which the stick figure plays

    This makes the end celebration where the guitarist jumps up and down 4 times.
    
    gui: The graphic imported from graphics.py
    x= The current x-position the stick figure is referenced from.
    y= The current y-position the stick figure is referenced from.
    '''
    gui.line(x,y+38,x+30,y+22,"bisque2",5)
    gui.triangle(x-40,y+50,x-20,y+50,x+5,y+35,"red")
    gui.triangle(x-15,y+70,x-20,y+50,x+5,y+35,"red")
    gui.ellipse(x-10,y+48,8,8,"white")
    gui.line(x-20,y+47,x-5,y+52,"black",1)
    
    
def light(gui,x,y,x2,y2,on):
    '''
    Depending on the input the light fixtures turn on or off.

    This makes the end celebration where the guitarist jumps up and down 4 times.
    
    gui: The graphic imported from graphics.py
    x= The current x-position the stick figure is referenced from.
    y= The current y-position the stick figure is referenced from.
    x1=The current end x-position the stick figure is referenced from.
    y2=The current end y-position the stick figure is referenced from.
    '''
    gui.ellipse(x,y,20,20,"dark grey")
    gui.line(x,y,x2,y2,"dark grey",20)
    if on == "True": # Various light rays
        gui.line(x2,y2,x2-10,y2+30,"light goldenrod",20)
        gui.line(x2,y2,x2,y2+30,"gold",20)
        gui.line(x2,y2,x2+10,y2+30,"light goldenrod",20)

if __name__== "__main__":
    main()
