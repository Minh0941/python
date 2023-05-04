def annoying_fibonacci_sequence(n):
    '''Prints out a fibonacci sequence reciursively based on 
    several hard inputs and user input
    Param: n= user input of number of fibonacci sequence to print

    '''
    if n ==0:
        return []
    if n==1:
        return[0]
    if n==2:
        return[0,1]
    if n==3:
        return[0,1,1]
    if n==4:
        return annoying_fibonacci_sequence(n-1)+ [2]
    if n==5:
        return annoying_fibonacci_sequence(n-1)+ [3]
    if n==6:
        return annoying_fibonacci_sequence(n-1)+[5]
    if n>6:
        temp= annoying_fibonacci_sequence(n-1)
        return temp +[temp[-1]+temp[-2]]
