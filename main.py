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

import textwrap

import puzzle_generator
import puzzle_page

class BoringSudokuWeb(object):
    @cherrypy.expose
    def index(self):
        return textwrap.dedent(
            '''
            <!doctype html>
            <head>
                <title>Boring Sudoku Web</title>
                <meta name="author" content="Matthew Todd">
                <meta name="description" content="Play a simple sudoku puzzle in your browser.">
            </head>
            <body>
                <center>
                <h1>Boring Sudoku Web</h1>
                So simple, it's almost boring!<br>
                <br>
                <form method="get" action="puzzle">
                    <input type="number" value="20" name="num_blank_spaces" min="0" max="81"/>
                    <button type="submit">Generate Puzzle</button>
                </form>
                </center>
            </body>
            '''
            )

    @cherrypy.expose
    def puzzle(self, num_blank_spaces):
        num_blank_spaces = int(num_blank_spaces)
        (starting_puzzle, solved_puzzle) = puzzle_generator.generate_puzzle(num_blank_spaces)
        return puzzle_page.generate_puzzle_page(starting_puzzle, solved_puzzle)

def main():
    cherrypy.quickstart(BoringSudokuWeb(), config='server.conf')

if __name__ == '__main__':
    main()

