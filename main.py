#!/usr/bin/env python3
'''
Boring Sudoku Web
So simple, it's almost boring.

This is a simple web app that generates sudoku puzzles that can be played in
the browser.

@author Matthew Todd
@date 2023-12-21
'''

# We are using cherrypy since it's built-in server is robust enough for simple
# production environments. This is compared to flask, bottle, and others that
# say to gunincorn, uWSGI, or some other webapp, even cherrypy, which would be
# another dependency. Also, cherrypy gives future flexibility to put a nginx
# reverse proxy in front of it.
import cherrypy

import puzzle_page

class BoringSudokuWeb(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def puzzle(self):
        starting_puzzle = [
            ['1', '', '', '', '', '', '', '', ''],
            ['2', '', '', '', '', '', '', '', ''],
            ['3', '', '', '', '', '', '', '', ''],
            ['4', '', '', '', '', '', '', '', ''],
            ['5', '', '', '', '', '', '', '', ''],
            ['6', '', '', '', '', '', '', '', ''],
            ['7', '', '', '', '', '', '', '', ''],
            ['8', '', '', '', '', '', '', '', ''],
            ['9', '', '', '', '', '', '', '', ''],
        ]
        solved_puzzle = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['2', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['3', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['4', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['5', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['6', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['7', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['8', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['9', '2', '3', '4', '5', '6', '7', '8', '9'],
        ]
        return puzzle_page.generate_puzzle_page(starting_puzzle, solved_puzzle)

def main():
    cherrypy.quickstart(BoringSudokuWeb())

if __name__ == '__main__':
    main()

