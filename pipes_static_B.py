from pipes_static_A import *
from graphics import graphics
import random

def main():
    gui= graphics(500,500,"win")
    gui.rectangle(0,0,500,500,"grey")
    for x in range(5):
        
        for y in range(5):
            north=random.choice(["True","False"])
            east=random.choice(["True","False"])
            south=random.choice(["True","False"])
            west=random.choice(["True","False"])
            color=random.choice(["True","False"])
            draw_tile(gui,x*100,y*100,north,east,south,west,color)
    gui.line(0,100,500,100,"white")
    gui.line(0,200,500,200,"white")
    gui.line(0,300,500,300,"white")
    gui.line(0,400,500,400,"white")
    gui.line(100,0,100,500,"white")
    gui.line(200,0,200,500,"white")
    gui.line(300,0,300,500,"white")
    gui.line(400,0,400,500,"white")
    gui.mainloop()

if __name__== "__main__":
    main()