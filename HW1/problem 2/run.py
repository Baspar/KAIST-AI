# coding: utf-8

import time

from problem import *
from fringe import *
from search import *

####################################################
#                                                  #
#             DO NOT MODIFY THIS FILE!             #
#                                                  #
####################################################

def run_search(search_name, puzzle, search_function, *args):
    try :
        print '##', search_name
        puzzle.reset_statistics()

        start_time = time.time()
        solution = search_function(*args)
        end_time = time.time()

        print '- execution time: {0:.10f}s'.format(end_time - start_time)
        print '- number of generated nodes:', puzzle.generated_nodes
        print '- max depth:', puzzle.max_depth
        print '- action sequence:', solution
    except EightPuzzle.Exception as exception:
        print '-', exception
    finally:
        print ''

puzzles = [
    EightPuzzle(
        initial_state=EightPuzzle.State([
            [1, 0, 8],
            [4, 3, 2],
            [7, 6, 5],
        ], blank_location=(0, 1)),
        goal_state=EightPuzzle.State([
            [1, 3, 8],
            [4, 6, 2],
            [7, 0, 5],
        ], blank_location=(2, 1)),
        allowed_max_depth=10
    ),
    EightPuzzle(
        initial_state=EightPuzzle.State([
            [1, 5, 0],
            [4, 3, 2],
            [7, 8, 6],
            ], blank_location=(0, 2)),
        goal_state=EightPuzzle.State([
            [1, 5, 2],
            [4, 8, 3],
            [7, 6, 0],
            ], blank_location=(2, 2)),
        allowed_max_depth=20
    ),
    EightPuzzle(
        initial_state=EightPuzzle.State([
            [4, 1, 3],
            [7, 2, 6],
            [0, 5, 8],
        ], blank_location=(2, 0)),
        goal_state=EightPuzzle.State([
            [0, 2, 6],
            [1, 3, 4],
            [7, 5, 8],
        ], blank_location=(0, 0)),
        allowed_max_depth=20
    ),
    EightPuzzle(
        initial_state=EightPuzzle.State([
            [2, 3, 6],
            [1, 4, 8],
            [7, 5, 0],
        ], blank_location=(2, 2)),
        goal_state=EightPuzzle.State([
            [4, 2, 6],
            [3, 7 ,8],
            [0, 1, 5],
        ], blank_location=(2, 0)),
        allowed_max_depth=20
    ),
    EightPuzzle(
        initial_state=EightPuzzle.State([
            [0, 2, 3],
            [1, 7, 6],
            [5, 4, 8],
        ], blank_location=(0, 0)),
        goal_state=EightPuzzle.State([
            [1, 2, 7],
            [5, 6, 3],
            [0, 4, 8],
        ], blank_location=(2, 0)),
        allowed_max_depth=20
    )
]

for index, puzzle in enumerate(puzzles):
    print '# Test', (index + 1)
    run_search('Greedy best-first search', puzzle, tree_search, puzzle, GreedyBestFirstSearchFringe(puzzle.goal_state))
    run_search('A-star search', puzzle, tree_search, puzzle, AStarSearchFringe(puzzle.goal_state))
    print ''