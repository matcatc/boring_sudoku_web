#!/usr/bin/env python3
'''
Boring Sudoku Web
So simple, it's almost boring.

This is a simple web app that generates sudoku puzzles that can be played in
the browser.

@author Matthew Todd
@date 2023-12-21

Copyright 2024 Matthew Todd

This file is part of Boring Sudoku Web.

Boring Sudoku Web is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

Boring Sudoku Web is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with
Boring Sudoku Web. If not, see <https://www.gnu.org/licenses/>.
'''

# We are using cherrypy since it's built-in server is robust enough for simple
# production environments. This is compared to flask, bottle, and others that
# say to gunincorn, uWSGI, or some other webapp, even cherrypy, which would be
# another dependency. Also, cherrypy gives future flexibility to put a nginx
# reverse proxy in front of it.
import cherrypy

import os
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
                    <input type="range" value="20" name="num_blank_spaces" min="0" max="81" oninput="this.nextElementSibling.value = this.value"/>
                    <output>20</output>
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
    cherrypy.config.update('server.conf')
    app = cherrypy.tree.mount(BoringSudokuWeb(), config='server.conf')
    app.merge({
            '/favicon.ico':
            {
                'tools.staticfile.on': True,
                'tools.staticfile.filename': os.path.join( os.path.abspath(os.path.dirname(__file__)), 'favicon.png' )
            }
        })
    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == '__main__':
    main()

