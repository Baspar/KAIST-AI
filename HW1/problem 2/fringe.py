# coding: utf-8

import collections

def calculate_manhattan_distance(location1, location2):
    # [Problem 2 - A]
    # calculate and return a Manhattan distance between location1 and location2
    pass

def calculate_total_manhattan_distance(state1, state2):
    # [Problem 2 - B]
    # calculate and return a total Manhattan distance between state1 and state2
    pass

# [Problem 2 - C]
class GreedyBestFirstSearchFringe(object): # a fringe for the greedy best-first search
    def __init__(self, goal_state, elements=None):
        if not elements:
            elements = []

        # store the goal_state to calculate heuristic values
        pass
        # initialize a queue with the given elements
        pass

    def is_empty(self):
        # return true only if there are no more elements in the queue
        pass

    def front(self):
        # return the first element of this queue
        pass

    def remove_front(self):
        # return self.front() and remove it from the queue
        # HINT: you can use the heapq library in python
        # https://docs.python.org/2/library/heapq.html
        pass

    def insert(self, element):
        # insert an element into the queue (consider a type of queue you will use for this fringe)
        pass

    def insert_all(self, elements):
        # insert a set of elements into the queue
        pass

    def heuristic_function(self, node):
        # calculate and return a heuristic value of the node
        # use the calculate_total_manhattan_distance function as a heuristic function
        # HINT: use this function as a priority of an element(an instance of Node)
        pass

# [Problem 2 - D]
class AStarSearchFringe(object): # a fringe for the a-star search
    def __init__(self, goal_state, elements=None):
        if not elements:
            elements = []

        # store the goal_state to calculate heuristic values
        pass
        # initialize a queue with the given elements
        pass

    def is_empty(self):
        # return true only if there are no more elements in the queue
        pass

    def front(self):
        # return the first element of this queue
        pass

    def remove_front(self):
        # return self.front() and remove it from the queue
        # HINT: you can use the heapq library in python
        # https://docs.python.org/2/library/heapq.html
        pass

    def insert(self, element):
        # insert an element into the queue (consider a type of queue you will use for this fringe)
        pass

    def insert_all(self, elements):
        # insert a set of elements into the queue
        pass

    def heuristic_function(self, node):
        # calculate and return a heuristic value of the node
        # use the calculate_total_manhattan_distance function as a heuristic function
        # HINT: use this function as a priority of an element(an instance of Node)
        pass