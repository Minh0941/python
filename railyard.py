''' File: railyard.py
    Author: Minh Le
    Purpose: The purpose of this program is to read a file inputted
    by the user. The code will then loop through and ask a series of
    inputs until there is an error or the user inputs 'quit". The inputs
    from the user will define the number of cars on each railroad and
    whether or not a train is departing.
'''

def main():
    '''
    This function will read the input file given by the user. It
    will then loop through and call the other functions and give
    a result depending on what the user's input was. If there is a
    typo in the input or if the user types "quit", the loop will break.
    :return: Call the other functions which print the strings needed
    to play the game
    '''

    # check if file exsists
    try:
        file_input = open(input('Please give the yard file:\n'), 'r')
    except FileNotFoundError:
        print('ERROR: Could not open the yard file')
        return

    railroad_list = file_input.readlines()
    railroad = []
    active = True
    depart = False

    # print track base from file
    print_railroad(railroad_list)

    # check if input is quit
    while active:
        depart = False
        # command
        command_input = input('What is your next command?\n')
        if command_input == 'quit':
            print('')
            print("Quitting!")
            return

        # check the input for errors
        command_list = command_input.split()
        if check_command(command_list, railroad_list) == False:
            print('')
            pass
        else:

            # print string after command is typed
            move = command_list[0]
            count = command_list[1]
            track_from = command_list[2]
            track_to = command_list[3]
            print("\nThe locomotive on track", track_from, "moved", count,
                  "cars to track",  track_to + '.\n')

            # swap cars
            take_cars(command_list, railroad_list, railroad)
            place_cars(command_list, railroad)

            # modify railroad so it can be checked for departure
            temp_rail = []
            for element in railroad:
                new_element = ''.join(element)
                temp_rail.append(new_element)
            railroad = temp_rail

            # check for departure
            depart_check(railroad, active, depart)


def take_cars(command_list, railroad_list, railroad):
    '''
    This function will find the cars inside railroad_list and
    will append them to the end of the list, so they can be
    used in the place_cars function.
    :param command_list: Should be a list of the input command
    :param railroad_list: Should be a list from the read file.
    :param railroad: Should be an empty list
    :return: Should return a list with the cars appended at the end
    '''
    count = int(command_list[1])
    track_from = int(command_list[2])

    # create 2D list of characters in the read file
    for line in railroad_list:
        new_line = list(line)
        railroad.append(new_line)

    # find the cars in the track and add them to list
    cars = ''
    temp_count = 0
    track = railroad[track_from - 1]
    i = len(track) - 1
    while i > 0:
        if track[i].islower():
            cars += track[i]
            track.remove(track[i])
            temp_count += 1
            if temp_count == count:
                i = 0
        elif track[i] == 'T':
            track.remove(track[i])
        i -= 1
    railroad.append(cars)

    # fill the list again so it matches the other tracks
    i = 0
    while i < count + 1:
        track.insert(0, '-')
        i += 1


def place_cars(command_list, railroad):
    '''
    This function should take the list from take_cars and
    add the cars to the track the user wants the cars to move to.
    :param command_list: Should be a list of the input command
    :param railroad: Should be a 2D list separated by each character
    in the read file.
    :return: Should return a 2D list with the updated tracks
    '''
    count = int(command_list[1])
    track_to = int(command_list[3])
    cars = railroad[len(railroad) - 1]
    railroad.remove(cars)
    end = ['T', '-', '\n']

    # remove the '-' and '\n'
    track = railroad[track_to - 1]
    track.pop()
    track.pop()

    # flip cars and append them to track
    cars = cars[::-1]
    for char in range(len(cars)):
        track.append(cars[char])

    # put the locomotive and track back
    track.extend(end)

    # fill the track
    for i in range(count + 1):
        track.remove(track[0])


def print_railroad(railroad_list):
    '''
    This function will take a 2D list, iterate through the
    lists and print each line. It will also give the number of
    locomotives as well as the number of cars going to a different
    destination.
    :param railroad_list: Should be a 2D list, separated by characters
    :return: Should return a string of the track as well as the
    locomotive and destination count.
    '''

    # loop through lists and count locomotives
    # also count the different cars depending on destination
    destinations = []
    locomotive_count = 0
    destination_count = 0
    i = 1
    for road in railroad_list:
        for track in range(len(road)):
            if road[track] == 'T':
                locomotive_count += 1
            if road[track].isalpha() and road[track] != 'T':
                if road[track] not in destinations:
                    destinations.append(road[track])
                    destination_count += 1
        print(str(i) + ':', str(road), end='')
        i += 1
    print('Locomotive count:', locomotive_count)
    print('Destination count:', destination_count, '\n')


def depart_check(railroad, active, depart):
    '''
    This function will a 2D list and check to see if
    a track in the railroad has cars all going to
    one destination. If that is true and if it has a
    locomotive, it will depart. It will then print the
    outcome.
    :param railroad: Should be a 2D list
    :param active: Should be a boolean that determines if
    the loop stops.
    :param depart: Should be a boolean that determines
    whether it departs
    :return: Should return strings of the railroad that
    causes a train to depart.
    '''

    # loop through and check if the train needs to depart
    cars = 0
    car = ''
    locomotive_count = 0
    destination_count = 0
    for rails in railroad:
        destinations = {}
        for char in range(len(rails)):
            if rails[char].isalpha() and rails[char] not in destinations:
                destinations[rails[char]] = 1
            elif rails[char].isalpha() and rails[char] in destinations:
                destinations[rails[char]] += 1
        if len(destinations) == 2 and 'T' in destinations:
            depart = True
            if depart:
                i = 1
                for rails in railroad:
                    print(str(i) + ':', rails, end='')
                    i += 1
            for keys in destinations.keys():
                if keys != 'T':
                    cars = destinations[keys]
                    car = keys
            location = railroad.index(rails)
            length = len(rails) - 1
            railroad.remove(rails)
            railroad.insert(location, ('-' * length))
            print('*** ALERT***  The train on track', str(location + 1) +
                  ', which had', str(cars), 'cars, departs for destination',
                  car + '.\n')

            # check if the last locomotive has departed
            des = []
            for element in railroad:
                if 'T' in element:
                    locomotive_count += 1
                for char in range(len(element)):
                    if element[char].islower() and element[char] not in des:
                        des.append(element[char])
                        destination_count += 1
            if locomotive_count == 0:
                print('The last locomotive has departed!\n')

            # gives locomotive and destinations count
            i = 1
            for rails in railroad:
                print(str(i) + ':', rails, end='')
                i += 1
            print('')

            print('Locomotive count:', locomotive_count)
            print('Destination count:', destination_count, '\n')
            if locomotive_count == 0:
                active = False
                return active

    # prints railroad if it doesn't depart
    if not depart:
        print_railroad(railroad)

def check_command(command_list, railroad):
    '''
    This function will check to see if there are typos
    or errors in the input. If so, it will repeat the loop
    and tell the user what is wrong.
    :param command_list: Should be a list of input
    :param railroad: Should be a 2D list
    :return: Should the railroad and the error.
    '''
    move = str(command_list[0])

    # if there is a negative count
    if int(command_list[1]) <= 0:
        print('ERROR: Cannot move a negative number of cars.')
        print_railroad(railroad)
        return False

    # if the first item in command is wrong
    if move == 'move' or move == 'quit':
        pass
    else:
        print('ERROR: The only valid command formats are (where each'
              ' X represents an integer):')
        print('move X X X')
        print('quit')
        print_railroad(railroad)
        return False

    # if command is too long
    if len(command_list) != 4:
        print('')
        print('ERROR: The only valid command formats are '
              '(where each X represents an integer):')
        print('move X X X')
        print('quit')
        print_railroad(railroad)
        return False

    # if the track it moves cars to is same as where it got it from
    if len(command_list) == 4:
        if int(command_list[2]) == int(command_list[3]):
            print("ERROR: The 'to' track is the same as the 'from' track.")
            print_railroad(railroad)
            return False


main()
