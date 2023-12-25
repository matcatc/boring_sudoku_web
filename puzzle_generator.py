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

def generate_symbol_puzzle():
    '''
    Generate a solved puzzle position with symbols A-I instead of 1-9.
    '''
    puzzle = [
        ['2', '3', '5', '7', '1', '9', '6', '8', '4'],
        ['8', '9', '6', '4', '5', '2', '1', '7', '3'],
        ['1', '4', '7', '3', '6', '8', '9', '2', '5'],
        ['7', '8', '9', '6', '2', '3', '5', '4', '1'],
        ['5', '1', '3', '8', '9', '4', '7', '6', '2'],
        ['6', '2', '4', '1', '7', '5', '3', '9', '8'],
        ['9', '7', '8', '2', '3', '1', '4', '5', '6'],
        ['3', '5', '2', '9', '4', '6', '8', '1', '7'],
        ['4', '6', '1', '5', '8', '7', '2', '3', '9'],
    ]
    return puzzle

def transform_puzzle(puzzle):
    '''
    Perform transformations on the puzzle such as flipping, rotating, etc.
    '''
    # TODO
    return puzzle

def convert_symbol_to_number_puzzle(puzzle):
    '''
    Replace the symbols A-I in a puzzle with numbers 1-9.
    '''
    # TODO
    return puzzle

def get_starting_puzzle(solved_puzzle, num_blank_spaces):
    '''
    Given a solved puzzle position, generate a starting puzzle position from it
    by removing some entries.
    '''
    # TODO
    starting_puzzle = [
        ['', '', '5', '7', '', '', '6', '8', ''],
        ['8', '', '', '', '', '2', '', '', ''],
        ['1', '', '', '3', '6', '', '', '', '5'],
        ['', '8', '', '', '2', '', '5', '', '1'],
        ['', '', '3', '8', '', '4', '7', '', ''],
        ['6', '', '4', '', '7', '', '', '9', ''],
        ['9', '', '', '', '3', '1', '', '', '6'],
        ['', '', '', '9', '', '', '', '', '7'],
        ['', '6', '1', '', '', '7', '2', '', ''],
    ]
    return starting_puzzle

def generate_puzzle(num_blank_spaces):
    '''
    @param [in] num_blank_spaces Number of blank spaces to have in the starting
    puzzle position. Controls / influences difficulty.
    @return (starting_puzzle, solved_puzzle)
    '''
    solved_puzzle = convert_symbol_to_number_puzzle(transform_puzzle(generate_symbol_puzzle()))
    starting_puzzle = get_starting_puzzle(solved_puzzle, num_blank_spaces)
    return (starting_puzzle, solved_puzzle)


