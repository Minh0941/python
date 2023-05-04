
# Author: Minh Le
# Class: CSC120
#Purpose: These defined classes will take a variety of inputs depending on their problem sets and return 
# various data points with the corresponding problem.

class Simplest:
    # Turns 4 seperate inputs into a condensed single variable
    def __init__(self,a,b,c):
        self.a= a
        self.b=b
        self.c=c

class Rotate:
    def __init__ (self,first,second,third):
        # Turns 4 seperate inputs into a condensed single variable
        self.first= first
        self.second= second
        self.third= third

    def get_first(self):
        # return first value
        return self.first
        
    def get_second(self):
        #return second value
        return self.second

    def get_third(self):
        #return third value
        return self.third

    def rotate(self):
        #changes the order of the values
        tempval=self.third
        self.third=self.first
        self.first=self.second
        self.second=tempval


class Band:
    def __init__(self,singer):
        # Turns 2 seperate inputs into a condensed array
        self.singer= singer
        self.drummer= None
        self.guitar_players=[]

    def get_singer(self):
        #returns name of singer
        return self.singer

    def set_singer(self,new_singer):
        #sets a new singer
        self.singer=new_singer

    def get_drummer(self):
        #return name of drummer
        return self.drummer

    def set_drummer(self,new_drummer):
        #sets new drummer
        self.drummer =new_drummer

    def add_guitar_player(self,new_guitar_player):
        #adds guitar players to the array
        self.guitar_players.append(new_guitar_player)

    def fire_all_guitar_players(self):
        #clears array of guitar names
        self.guitar_players=[]

    def get_guitar_players(self):
        #return names of all guitar players
        player= []
        for guitar in self.guitar_players:
            player.append(guitar)
        return player

    def play_music(self):
        #Depending on the singer, this function will 
        #print out different messages per singer
        if self.singer =="Frank Sinatra":
            print("Do be do be do")
        elif self.singer =="Kurt Cobain":
            print("bargle nawdle zouss")
        else:
            print('La la la')
        if self.drummer is not None:
            print('Bang bang bang!')
        for i in range(len(self.guitar_players)):
            print('Strum!')

class Color:
    def __init__(self,r,g,b,):
        # Turns 4 seperate inputs into a condensed single variable
        self.r=self.bound_values(r)
        self.g=self.bound_values(g)
        self.b=self.bound_values(b)
    def __str__(self):
        # returm rgb values
        return f'rgb({self.r}, {self.g}, {self.b})'

    def bound_values(self,val):
        #ensures rgb values are within range
        if val < 0:
            return 0
        elif val > 255:
            return 255
        else:
            return val
        
    def html_hex_color(self):
        #returns rgb values as a html color set
        return f'#{self.r:02X}{self.g:02X}{self.b:02X}'

    def get_rbg(self):
        #returns rgb vlaues
        return self.r, self.g, self.b

    def set_standard_color(self,name):
        #predefines colors depending on inputs by user
        if name.lower() =="red":
            self.r= 255
            self.g = 0
            self.b= 0
        elif name.lowe()== "yellow":
            self.r=255
            self.g=255
            self.b=0
        elif name.lower()=="black":
            self.r=0
            self.g=0
            self.b=0
        elif name.lower=="white":
            self.r= 255
            self.g=255
            self.b=255

    def remove_red(self):
        #clears any red for rbg value
        self.r= 0

class Room:
    def __init__ (self,name=''):
        self.name= name
        self.n = None
        self.s =None
        self.e= None
        self.w= None


    def set_name(self,name):
        self._name=name
    def get_name(self):
        return self._name
    def collapse_room(self):
        if self.n is not None:
            self.n.s= None
            self.n =None
        elif self.s is not None:
            self.s.n = None
            self.s =None
        elif self.e is not None:
            self.e.w = None
            self.e =None
        elif self.w is not None:
            self.w.e = None
            self.w =None
def build_grid(wid,hei):
    grid= []
    for row in range(int(hei)):
        row = []
        for col in range(int(wid)):
            row.append(Room(f'Room Number {row}, {col}'))
        grid.append(row)

    for row in range(int(hei)):

        for col in range(int(wid)):
            if col >0:
                grid[row][col -1].e = grid[row][col]
                grid[row][col].w= grid[row][col -1]
            elif col < wid -1:
                grid[row][col +1].w = grid[row][col]
                grid[row][col].e= grid[row][col]
            if row > 0:
                grid[row-1][col].s = grid[row][col]
                grid[row][col].s= grid[row-1][col]
            elif row <hei-1:
                grid[row+1][col].n = grid[row][col]
                grid[row][col].s= grid[row+1][col]
    return grid[hei-1][0]