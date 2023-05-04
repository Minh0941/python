'''
Author: Minh Le
File: dijkstra_on_grid.py
Purpose: find the fastest way around the maze. I have never cried over a 
coding project. Congrats btw. I have rewrote this program 7 complete times
trying queues, recursion, and just while loops. Can you pleaseeee posta solution

ALso can you help me debugg if you can??

'''
from dijkstra_node import *
import inspect
def main():
    '''
    purpose: to open the files and recurse through the file to turn itinto a 2d array
    Also to call other functions
    '''
    file_name = input("Please give the grid file:")
    file = open(file_name, 'r')
    temp = [] #turn it into 2d array
    for line in file:
        retval=[]
        for character in line.strip():
            retval.append(character)
        temp.append(retval)

    rows=[] # coordinate system with ints
    for items in range(len(temp)):
        col=[]
        for char in range(len(temp[0])):
            col.append(char)
        rows.append(col)
    start= input("Where to start?")
    start = start.split(" ")
    start[0] = int(start[0])
    start[1] = int(start[1])  

    operation= input("What type of operation?")
    if operation =="animate":
        solve(temp[0],start[0],start[1],temp[1],temp[2],"True")
    if operation=="fill":
        temp=map(temp,start)
        solve(temp[0],start[0],start[1],temp[1],temp[2],"False")
        initialize_q(temp[0])
        fill(temp)


def map(temp,cur):

    '''
    Purpose: to create a new map with dijstra nodes

    temp:2d array with no nodes
    cur= start coord
    '''
    cur_x = cur[0]
    cur_y = cur[1]
    

    temp_wid = len(temp[0]) - 1 
    temp_hei = len(temp) - 1
    for items in range(len(temp)):#checking and turning nodes
        for chars in range(len(temp[items])):
            if temp[items][chars] =='#':
                temp[items][chars]= DijkstraNode()

    return [temp, temp_wid,temp_hei]

def initialize_q(temp):
    '''
    To make the ToDo lists

    param: The 2d Array containing everything
    '''
    array=[] # uncallable used for toDO list
    for items in range(len(temp)):#checking and turning nodes
        for chars in range(len(temp[items])):
            if type(temp[items][chars])==DijkstraNode: #check type
                temp[items][chars].update_dist(0)
                distance= temp[items][chars].get_dist()
                tpl=(distance,items,chars)
                array.append(tpl)
                
    
def solve(temp,start_x,start_y,hei,wid,operator):
    '''
    It tries to solve the maze using dijsktra's alg

    temp:2d array with nodes,
    start_x: x -coord
    start_y=y-coord
    hei=hei of maze
    wid:wid of maze
    operator:animate and fill condition
    '''
    # q= queue()
    # q.enqueue(temp)
    # queue = q.deque([[start]])
    # seen = set([start])
    # ToDo=[]
    # while not queue.is_empty():
    #     path = queue.popleft()
    #     x, y = path[-1]

    #     for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
    #          if 0 <= x2 < wid and 0 <= y2 < hei and temp[y2][x2] != ' ' and (x2, y2) not in seen:
    #             temp[y2][x2].update_dist(0)
    #             distance= temp[y2][x2].get_dist()
    #             queue.append(path + [(x2, y2)])
    #             ToDo.append((distance,x2,y2))
    #             temp[y2][x2]=distance
    #             print(temp)
    #             print(Todo)
    #             seen.add((x2, y2))


    if inspect.isclass(temp[start_x][start_y]) == True: # checking clas type
        if temp[start_x][start_y].is_reached() == "False":
            print('0')
            temp[start_x][start_y].update_dist(0)
            dist= temp[start_x][start_y].get_dist()
            temp[start_x][start_y] =dist
            print(dist)
            temp[start_x][start_y].set_done()
        if operator==True:
            print(temp)
            q=queue()
            q.enqueue(array)
            distance =0
            while not q.is_empty():# queue for todo List
                cur=q.dequeue
                x= cur.get(distance)
                x+=1
                print(f"ToDo List: {x}")
        if start_x <=wid and start_x >=0:
            if start_y<=hei and start_y>=0:

                if temp[start_x][start_y].is_reached() == "False":
                    solve(temp,start_x-1,start_y,wid,hei) # recursion to check 4 directions
                    solve(temp,start_x+1,start_y,wid,hei)
                    solve(temp,start_x,start_y+1,wid,hei)
                    solve(temp,start_x,start_y-1,wid,hei)
        check= final_step_check(temp)
        if check== "True":
            return(temp)
def final_step_check(temp):
    for items in temp:
        for char in items:
            if char !=" " or type(char) != int:
                return False
    return True


def solve_one_step(temp):
    ''''''
def fill(temp):
    print(temp)
    

def animate():
    ''''''


if __name__== "__main__":
    main()