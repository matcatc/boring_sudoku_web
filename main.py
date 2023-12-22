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
        return puzzle_page.generate_puzzle_page()

def main():
    cherrypy.quickstart(BoringSudokuWeb())

if __name__ == '__main__':
    main()

