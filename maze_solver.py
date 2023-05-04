import os
class TreeNode:
 '''
 This class represents a tree node and its creation.
 The constructor will create the root and the array of
 children.
 '''
 def __init__(self, start):
    '''
    This constructor will create the root and the
    array of children for the parent node.
    '''
    self.start = start
    self.children = []
class Dump:
    '''
    This class will create the dump actions and create the
    tree and set of cells.
    The constructor will create numerous variables to help with
    these dump actions.
 '''
def __init__(self, file_name):
    '''
    This constructor will create numerous variables to help with
    the dump actions.
    file_name = name of the inputted file
    '''
    self._x = 0
    self._y = 0
    self._start = 0
    self._end = 0
    self._file_name = file_name
    self._cells = set()
    self._dups = []
    def create_cells(self):
        '''
        This method will create the set of cells that the
        program will use to solve the maze.
        '''
    file = open(self._file_name, 'r')
    create = set()
    temp = []
    for line in file:
        for character in line:
            temp.append(character)
    for i in temp:
        ## This will check to see if the character is
        ## a #, S, or an E, and then set coordinates to
        ## them.

        if i != '\n' and i != ' ':
            if i == 'S':
                i = (self._x,self._y)
                self._start = i
            elif i == 'E':
                i = (self._x,self._y)
                self._end = i
            i = (self._x, self._y)
            create.add(i)
            self._x += 1
        else:
            if i == '\n':
                self._x = 0
                self._y += 1
            elif i == ' ':
                self._x += 1
                self._cells = create
 def create_tree(self):
 '''
 This method will create the tree.
 '''
 pass
 def dumpcells(self):
 '''
 This function will print out the cells from the
 set in sorted order and locate the start and end
 coordinates.
 '''
 for i in sorted(self._cells):
 ## checks for start and end coordinates
 ## and prints out the rest in sorted order
 if i == self._start:
 print(' ', i, ' START')
 elif i == self._end:
 print(' ', i, ' END')
 else:
 print(' ', i)
 def dumptree(self):
 '''
 This function will print out the tree using
 different levels to display the levels of the tree
 and its paths.
 '''
 pass
 def dumpsol(self):
 '''
 This function will print out the path from
 the start coordinate to the end coordinate.
 '''
 pass
 def dumpsize(self):
 '''
 This function will print out the width and the
 height of the maze.

 '''
 max_x = 0
 max_y = 0
 for i in sorted(self._cells):
 if i[0] > max_x:
 max_x = i[0]
 if i[1] > max_y:
 max_y = i[1]
 print(' wid:', max_x + 1)
 print(' hei:', max_y + 1)
 def printmaze():
 '''
 This function will print out the solved maze with
 the path from start to end being periods.
 '''
 pass
def actions(file_name):
 '''
 This function will ask for the action input and
 call each function in the class based on the input.
 file_name = name of the file
 '''
 try:
 action = input()
 dump = Dump(file_name)
 dump.create_cells()
 ## making the class a variable lets you pass
 ## the parameters throught it to the methods inside.
 if action == 'dumpCells':
 print('DUMPING OUT ALL CELLS FROM THE MAZE:')
 dump.dumpcells()
 elif action == 'dumpTree':
 print('DUMPING OUT THE TREE THAT REPRESENTS THE MAZE:')
 dump.dumptree()
 elif action == 'dumpSolution':
 print('PATH OF THE SOLUTION:')
 dump.dumpsol()
 elif action == 'dumpSize':
 print('MAP SIZE:')
 dump.dumpsize()
 elif action == '':
 print('SOLUTION:')
 dump.printmaze()
 else:
 print('ERROR: Unrecognized command NOT_A_VALID_COMMAND')
 except:
 pass
def main():
 try:
 file_name = input()
 file = open(file_name, 'r')
 count_s = 0
 count_e = 0
 characters = ['S', 'E', '#']
 ## This loop will check for any errors in the file
This study source was downloaded by 100000850255890 from CourseHero.com on 08-08-2022 00:21:57 GMT -05:00
https://www.coursehero.com/file/137209822/maze-solverpy/
 ## and then proceed to the action function.
 for line in file:
 for word in line.split():
 for i in word:
 if i == 'S':
 count_s += 1
 elif i == 'E':
 count_e += 1
 elif i not in characters:
 print('ERROR: Invalid character in the map')
 if count_s > 1:
 print('ERROR: The map has more than one START position')
 elif count_e > 1:
 print('ERROR: The map has more than one END position')
 elif count_s == 0 or count_e == 0:
 print('ERROR: Every map needs exactly one START and exactly one END
position')
 actions(file_name)
 except FileNotFoundError:
 print('ERROR: Could not open file:', file_name)
main()