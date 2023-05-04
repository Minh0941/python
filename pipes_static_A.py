from graphics import graphics

def main():
    gui= graphics(500,500,"win")
    tile1= draw_tile(gui,0,0,"False","True","True","False","False")
    tile2=draw_tile(gui,0,100,"True","False","True","False","False")
    tile3=draw_tile(gui,0,200,"False","True","True","True","False")
    tile4=draw_tile(gui,0,300,"False","True","True","False","True")
    tile5=draw_tile(gui,0,400,"False","False","True","False","False")
    tile6=draw_tile(gui,100,0,"False","True","False","True","False")
    tile7=draw_tile(gui,100,100,"False","False","True","False","True")
    tile8=draw_tile(gui,100,200,"True","True","True","False","True")
    tile9=draw_tile(gui,100,300,"True","True","False","True","True")
    tile10=draw_tile(gui,100,400,"True","False","False","True","False")
    tile11=draw_tile(gui,200,0,"False","True","False","False","False")
    tile12=draw_tile(gui,200,100,"False","False","False","True","False")
    tile13=draw_tile(gui,200,200,"True","False","True","True","True")
    tile14=draw_tile(gui,200,300,"True","True","False","False","True")
    tile15=draw_tile(gui,200,400,"False","True","False","False","False")
    tile16=draw_tile(gui,300,0,"False","False","True","True","False")
    tile17=draw_tile(gui,300,100,"True","True","False","True","False")
    tile18=draw_tile(gui,300,200,"False","True","True","True","False")
    tile19=draw_tile(gui,300,300,"True","True","True","False","False")
    tile20=draw_tile(gui,300,400,"False","False","True","False","False")
    tile21=draw_tile(gui,400,0,"False","False","True","False","False")
    tile22=draw_tile(gui,400,100,"False","True","False","False","False")
    tile23=draw_tile(gui,400,200,"False","False","False","True","False")
    tile24=draw_tile(gui,400,300,"True","True","False","True","False")
    tile25=draw_tile(gui,400,400,"False","False","True","False","False")

    gui.line(0,100,500,100,"white")
    gui.line(0,200,500,200,"white")
    gui.line(0,300,500,300,"white")
    gui.line(0,400,500,400,"white")
    gui.line(100,0,100,500,"white")
    gui.line(200,0,200,500,"white")
    gui.line(300,0,300,500,"white")
    gui.line(400,0,400,500,"white")
    gui.mainloop()

def draw_tile(gui,x,y,north,east,south,west,blue):

        gui.rectangle(x,y,100,100,"grey")
        color=""
        if blue =="True":
            color="blue"
        elif blue== "False":
            color="black"
        if north=="True" and east== "False" and south=="False" and west =="False":
            gui.rectangle(x+40,y+40,20,20,color)
        if north=="False" and east== "True" and south=="False" and west =="False":
            gui.rectangle(x+40,y+40,20,20,color)
        if north=="False" and east== "False" and south=="True" and west =="False":
            gui.rectangle(x+40,y+40,20,20,color)
        if north=="False" and east== "False" and south=="False" and west =="True":
            gui.rectangle(x+40,y+40,20,20,color)
        if north=="True" and east== "False" and south=="True" and west =="True":
            gui.rectangle(x+40,y+40,20,20,color)
        if north== "True":
            gui.rectangle(x+45,y+50,10,-50,color)
        if east=="True":
            gui.rectangle(x+50,y+45,50,10,color)
        if south=="True":
            gui.rectangle(x+45,y+50,10,50,color)
        if west=="True":
            gui.rectangle(x+50,y+45,-50,10,color)
        

if __name__== "__main__":
    main()
