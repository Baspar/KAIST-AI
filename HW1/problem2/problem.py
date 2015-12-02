# coding: utf-8

from search import Node

####################################################
#                                                  #
#       YOU DO NOT HAVE TO MODIFY THIS FILE!       #
#                                                  #
####################################################

# 8-puzzle formulation
# - states: a state description specifies the location of each of the eight tiles and the blank in one of the nine squares.
# - initial state: any state can be designated as the initial state. Note that any given goal can be reached from exactly half of the possible inital states.
# - successor function: this generates the legal states that result from trying the four actions (blank moves Left, Right, Up or Down).
# - goal test: this checks whether the state matches the goal configuration.
# - path cost: each step costs 1, so the path cost is the number of steps in the path.

class EightPuzzle(object):
    class State(object):
        def __init__(self, tiles, blank_location):
            self.tiles = tiles # the tiles of this state, 3x3 2-dimension list
            self.blank_location = blank_location # the location of the blank tile in self.tiles

        def __eq__(self, other):
            # return true only if self.tile and other.tile are equal
            return (self.tiles == other.tiles) and (self.blank_location == other.blank_location)

        def __repr__(self):
            lines = []
            for row in self.tiles:
                lines.append('\t'.join(map(str, row)))

            return '\n'.join(lines)

    class Exception(RuntimeError):
        pass # YOU DO NOT HAVE TO MODIFY THIS PASS STATEMENT

    def __init__(self, initial_state, goal_state, allowed_max_depth):
        self.initial_state = initial_state # the initial state of the eight puzzle
        self.goal_state = goal_state # the goal state of the eight puzzle
        self.allowed_max_depth = allowed_max_depth # the allowed maximum depth to prevent infinite-loop

        self.actions = { # the actions of the eight puzzle
            'left': self._build_action((0, -1)),
            'right': self._build_action((0, +1)),
            'up': self._build_action((-1, 0)),
            'down': self._build_action((+1, 0)),
        }

        self.reset_statistics()

    def goal_test(self, state):
        # return true only if the state is the goal state
        return state == self.goal_state

    def successor_function(self, node):
        # generate the legal states that result from trying the four actions (blank moves left, right, up or down)
        for action in self._legal_actions(node.state):
            yield action, self.actions[action](node.state)

    def expand(self, node):
        # expand the node by applying the successor function and return them.
        successors = []

        for action, next_state in self.successor_function(node):
            successor = Node(
                state=next_state,
                parent=node,
                action=action,
                path_cost=node.path_cost + self._step_cost(node.state, action),
                depth=node.depth + 1,
            )
            self.generated_nodes += 1
            self.max_depth = max(self.max_depth, node.depth + 1)

            if self.max_depth > self.allowed_max_depth:
                raise EightPuzzle.Exception('exceeds the allowed max depth')

            successors.append(successor)

        return successors

    def reset_statistics(self):
        self.generated_nodes = 1 # root node
        self.max_depth = 0

    def _step_cost(self, current_state, action):
        return 1

    def _legal_actions(self, state):
        actions = ['left', 'right', 'up', 'down']

        if state.blank_location[0] == 0:
            actions.remove('up')

        if state.blank_location[0] == 2:
            actions.remove('down')

        if state.blank_location[1] == 0:
            actions.remove('left')

        if state.blank_location[1] == 2:
            actions.remove('right')

        return actions

    def _build_action(self, direction):
        def move_blank(state):
            new_blank_location = (state.blank_location[0] + direction[0], state.blank_location[1] + direction[1])

            new_tiles = [
                state.tiles[0][:],
                state.tiles[1][:],
                state.tiles[2][:],
            ]
            new_tiles[state.blank_location[0]][state.blank_location[1]], new_tiles[new_blank_location[0]][new_blank_location[1]] = new_tiles[new_blank_location[0]][new_blank_location[1]], new_tiles[state.blank_location[0]][state.blank_location[1]]

            return EightPuzzle.State(new_tiles, new_blank_location)

        return move_blank