# coding: utf-8

class Node(object):
    def __init__(self, state, parent=None, action=None, path_cost=0, depth=0):
        self.state = state # the state in the state space to which the node corresponds
        self.parent = parent # the node in the search tree that generated this node
        self.action = action # the action that was applied to the parent to generate the node
        self.path_cost = path_cost # the cost of the path from the initial state to the node
        self.depth = depth # the number of steps along the path from the initial state

    def solution(self):
        # return a sequence of actions obtained by following parent pointers back to the root
        if self.parent == None:
            return []
        else:
            return self.parent.solution() + [self.action]

def tree_search(problem, fringe):
    # [Problem 1 - B]
    # implement TREE-SEARCH algorithm
    # return a solution(an instance of list) or 'failure'(an instance of str)
    pass

def depth_limited_search(problem, limit):
    # [Problem 1 - C]
    # implement DEPTH-LIMITED-SEARCH algorithm
    # return a solution(an instance of list), 'cutoff'(an instance of str) or 'failure'(an instance of str)
    pass

def iterative_deepening_search(problem):
    # [Problem 1 - D]
    # implement ITERATIVE-DEEPENING-SEARCH algorithm
    # return a solution(an instance of list), 'cutoff'(an instance of str) or 'failure'(an instance of str)
    pass