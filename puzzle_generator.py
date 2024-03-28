'''
This module is reponsible for generating the puzzle.

Here is the high-level algorithm:
    * Generate a completed puzzle using symbols A-I instead of 1-9
    * Perform transforms on the completed puzzle: rotate, flip, etc.
    * Replace symbols with numbers 1-9
    * Removing entries to make the starting puzzle position.

Reasoning:
    * Starting with symbols allows us to replace in different numbers to get
    different puzzles from the same starting solved puzzle. For example,
    replacing A-I with 1-9 vs 9-1 gives two different puzzles from a user
    perspective.
    * Performing transformations allows the same puzzle to look like different
    puzzles to the user.
    * Removing different entries can give a qualatatively different puzzle.
    * Thus we re-use the same A-I symbol puzzles to generate multiple puzzles
    from the user perspective. (Giving the same puzzle 100s of times in a row
    might be too much as the user might notice patterns, but we can definitely
    re-use it some amount.)
'''

import copy
# TODO: seed for all randommness, for testing / debugging / etc.?
import random

def generate_symbol_puzzle():
    '''
    Generate a solved puzzle position with symbols A-I instead of 1-9.
    '''
    puzzle = [
        ['B', 'C', 'E', 'G', 'A', 'I', 'F', 'H', 'D'],
        ['H', 'I', 'F', 'D', 'E', 'B', 'A', 'G', 'C'],
        ['A', 'D', 'G', 'C', 'F', 'H', 'I', 'B', 'E'],
        ['G', 'H', 'I', 'F', 'B', 'C', 'E', 'D', 'A'],
        ['E', 'A', 'C', 'H', 'I', 'D', 'G', 'F', 'B'],
        ['F', 'B', 'D', 'A', 'G', 'E', 'C', 'I', 'H'],
        ['I', 'G', 'H', 'B', 'C', 'A', 'D', 'E', 'F'],
        ['C', 'E', 'B', 'I', 'D', 'F', 'H', 'A', 'G'],
        ['D', 'F', 'A', 'E', 'H', 'G', 'B', 'C', 'I'],
    ]
    return puzzle

def transform_puzzle(puzzle):
    '''
    Perform transformations on the puzzle such as flipping, rotating, etc.
    '''
    # Testing with timeit shows random.choice and random.randrange
    # implementations are roughly equivalent.
    flip_horizontal = random.choice([False, True])
    flip_vertical = random.choice([False, True])
    rotate = random.choice([False, True])

    # An alternative and more general approach to flipping is to shuffle rows
    # and columns. I.e.: shuffle the three rows in a set and/or shuffle the
    # three sets of rows. Likewise for columns. We are not doing that here
    # because it's more complex than just flipping, and from my alpha testing,
    # the flipping is sufficient by itself.

    # horizontal = around y axis
    if flip_horizontal:
        for row in puzzle:
            row.reverse()

    # vertical = around x axis
    if flip_vertical:
        puzzle.reverse()

    # 180 rotation = vertical + horizontal flip. So we only support rotating 25
    # degrees. The direction of rotation doesn't really matter.
    if rotate:
        # From https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
        puzzle = list(zip(*puzzle[::-1]))

    return puzzle

def convert_symbol_to_number_puzzle(symbol_puzzle):
    '''
    Replace the symbols A-I in a puzzle with numbers 1-9.
    '''
    symbol_list = ['A','B','C','D','E','F','G','H','I']
    number_list = ['1','2','3','4','5','6','7','8','9']
    random.shuffle(number_list)
    conversion_dict = dict(zip(symbol_list, number_list))

    num_puzzle = []
    for row in symbol_puzzle:
        num_puzzle.append([conversion_dict[elem] for elem in row])

    return num_puzzle

def get_starting_puzzle(solved_puzzle, num_blank_spaces):
    '''
    Given a solved puzzle position, generate a starting puzzle position from it
    by removing some entries.
    '''
    # Generate list of unique grid coordinates to make blank. Use set to
    # enforce uniqueness.
    coordinates = set()
    while len(coordinates) < num_blank_spaces:
        coord = (random.randrange(9), random.randrange(9))
        coordinates.add( coord )

    starting_puzzle = copy.deepcopy(solved_puzzle)

    for (x,y) in coordinates:
        starting_puzzle[x][y] = ''

    return starting_puzzle

def generate_puzzle(num_blank_spaces):
    '''
    @param [in] num_blank_spaces Number of blank spaces to have in the starting
    puzzle position. Controls / influences difficulty.
    @return (starting_puzzle, solved_puzzle)
    '''
    # Later code assumes num_blank_spaces is reasonable. Client code should
    # have already limited it.
    assert(num_blank_spaces <= (9 * 9))

    solved_puzzle = convert_symbol_to_number_puzzle(transform_puzzle(generate_symbol_puzzle()))
    starting_puzzle = get_starting_puzzle(solved_puzzle, num_blank_spaces)
    return (starting_puzzle, solved_puzzle)


