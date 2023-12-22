'''
Generate the HTML webpage that has the puzzle.
'''

import json
import string
import textwrap

def get_html_template():
    '''
    Return the HTML template.
    '''
    return string.Template(textwrap.dedent(
        '''
        <!doctype html>
        <head>
            <title>Boring Sudoku Web</title>
            <meta name="author" content="Matthew Todd">
            <meta name="description" content="Play a simple sudoku puzzle in your browser.">

        <style>
        table{
            border-collapse: collapse;
            border: solid;
        }
        td {
            width: 3em;
            height: 3em;
            text-align: center; 
            vertical-align: center;
            border: 1px solid;
            cursor: pointer;
        }
        td:nth-child(3n) {
            border-right: solid;
        }
        tr:nth-child(3n) {
            border-bottom: solid;
        }
        input {
            width: 3em;
            height: 3em;
            cursor: pointer;
        }
        </style>
        <script type="text/javascript">
            // Number rows and columns in a sudoku grid.
            const NUM_ROWS = 9;
            const NUM_COLS = 9;

            /* auto-generated starting position and solved puzzle */
            const startingPuzzle = ${starting_puzzle};
            const solvedPuzzle = ${solved_puzzle};

            function cellClicked() {
                cell = this;
                const num = document.querySelector('input[name="num"]:checked').value;
                const row = cell.getAttribute("data-row");
                const col = cell.getAttribute("data-col");

                console.assert(row != null, "row is null");
                console.assert(col != null, "col is null");

                const numCorrect = num == solvedPuzzle[row-1][col-1];

                if( numCorrect ) {
                    cell.innerText = num
                }
            }

            function setupSudokuGrid() {
                const cellList = document.querySelectorAll('td');

                // Setup callbacks
                for( let i = 0; i < cellList.length; i++ ) {
                    cellList[i].addEventListener("click", cellClicked);
                }

                // Setup initial starting values
                for( let row = 1; row <= NUM_ROWS; row++ ) {
                    for( let col = 1; col <= NUM_COLS; col++ ) {
                        cell = document.querySelector("td[data-row='"+row+"'][data-col='"+col+"']");
                        cell.innerText = startingPuzzle[row-1][col-1];
                    }
                }
            }
        </script>
        </head>
        <body onload="setupSudokuGrid()">
            <center>
            <!-- TODO: link to home page? -->
            <h1>Boring Sudoku Web</h1>

            <noscript> This site requires javascript. Please enable it. <br><br> </noscript>

            <!-- Sudoku grid / playfield -->
            <table>
                <tr> <td data-row="1" data-col="1"></td> <td data-row="1" data-col="2"></td> <td data-row="1" data-col="3"></td> <td data-row="1" data-col="4"></td> <td data-row="1" data-col="5"></td> <td data-row="1" data-col="6"></td> <td data-row="1" data-col="7"></td> <td data-row="1" data-col="8"></td> <td data-row="1" data-col="9"></td> </tr>
                <tr> <td data-row="2" data-col="1"></td> <td data-row="2" data-col="2"></td> <td data-row="2" data-col="3"></td> <td data-row="2" data-col="4"></td> <td data-row="2" data-col="5"></td> <td data-row="2" data-col="6"></td> <td data-row="2" data-col="7"></td> <td data-row="2" data-col="8"></td> <td data-row="2" data-col="9"></td> </tr>
                <tr> <td data-row="3" data-col="1"></td> <td data-row="3" data-col="2"></td> <td data-row="3" data-col="3"></td> <td data-row="3" data-col="4"></td> <td data-row="3" data-col="5"></td> <td data-row="3" data-col="6"></td> <td data-row="3" data-col="7"></td> <td data-row="3" data-col="8"></td> <td data-row="3" data-col="9"></td> </tr>
                <tr> <td data-row="4" data-col="1"></td> <td data-row="4" data-col="2"></td> <td data-row="4" data-col="3"></td> <td data-row="4" data-col="4"></td> <td data-row="4" data-col="5"></td> <td data-row="4" data-col="6"></td> <td data-row="4" data-col="7"></td> <td data-row="4" data-col="8"></td> <td data-row="4" data-col="9"></td> </tr>
                <tr> <td data-row="5" data-col="1"></td> <td data-row="5" data-col="2"></td> <td data-row="5" data-col="3"></td> <td data-row="5" data-col="4"></td> <td data-row="5" data-col="5"></td> <td data-row="5" data-col="6"></td> <td data-row="5" data-col="7"></td> <td data-row="5" data-col="8"></td> <td data-row="5" data-col="9"></td> </tr>
                <tr> <td data-row="6" data-col="1"></td> <td data-row="6" data-col="2"></td> <td data-row="6" data-col="3"></td> <td data-row="6" data-col="4"></td> <td data-row="6" data-col="5"></td> <td data-row="6" data-col="6"></td> <td data-row="6" data-col="7"></td> <td data-row="6" data-col="8"></td> <td data-row="6" data-col="9"></td> </tr>
                <tr> <td data-row="7" data-col="1"></td> <td data-row="7" data-col="2"></td> <td data-row="7" data-col="3"></td> <td data-row="7" data-col="4"></td> <td data-row="7" data-col="5"></td> <td data-row="7" data-col="6"></td> <td data-row="7" data-col="7"></td> <td data-row="7" data-col="8"></td> <td data-row="7" data-col="9"></td> </tr>
                <tr> <td data-row="8" data-col="1"></td> <td data-row="8" data-col="2"></td> <td data-row="8" data-col="3"></td> <td data-row="8" data-col="4"></td> <td data-row="8" data-col="5"></td> <td data-row="8" data-col="6"></td> <td data-row="8" data-col="7"></td> <td data-row="8" data-col="8"></td> <td data-row="8" data-col="9"></td> </tr>
                <tr> <td data-row="9" data-col="1"></td> <td data-row="9" data-col="2"></td> <td data-row="9" data-col="3"></td> <td data-row="9" data-col="4"></td> <td data-row="9" data-col="5"></td> <td data-row="9" data-col="6"></td> <td data-row="9" data-col="7"></td> <td data-row="9" data-col="8"></td> <td data-row="9" data-col="9"></td> </tr>
            </table>

            <!-- Make it easier to click radio buttons -->
            <br>

            <!-- User selects what numbers they want to enter -->
            <div>
                <input type="radio" name="num" value="1" checked>
                <label for="1">1</label>
                <input type="radio" name="num" value="2">
                <label for="2">2</label>
                <input type="radio" name="num" value="3">
                <label for="3">3</label>
                <input type="radio" name="num" value="4">
                <label for="4">4</label>
                <input type="radio" name="num" value="5">
                <label for="5">5</label>
                <input type="radio" name="num" value="6">
                <label for="6">6</label>
                <input type="radio" name="num" value="7">
                <label for="7">7</label>
                <input type="radio" name="num" value="8">
                <label for="8">8</label>
                <input type="radio" name="num" value="9">
                <label for="9">9</label>
            </div>
            </center>
        </body>
        '''
        ))

def format_js_2d_array_variable(array_2d):
    '''
    Format a 2D Python array as a 2D javascipt array
    '''
    return json.dumps(array_2d)

def generate_puzzle_page(starting_puzzle, solved_puzzle):
    '''
    @param [in] starting_puzzle Starting puzzle position as an array of arrays of strings
    @param [in] solved_puzzle Solved puzzle
    @return HTML webpage for playing the puzzle
    '''
    starting_puzzle_js = format_js_2d_array_variable(starting_puzzle)
    solved_puzzle_js = format_js_2d_array_variable(solved_puzzle)
    d = dict( starting_puzzle = starting_puzzle_js
            , solved_puzzle = solved_puzzle_js
            )
    return get_html_template().substitute(d)

