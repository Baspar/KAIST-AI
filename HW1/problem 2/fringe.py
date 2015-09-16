# coding: utf-8

import Queue
import math

def calculate_manhattan_distance(location1, location2):
    # [Problem 2 - A]
    # calculate and return a Manhattan distance between location1 and location2
    return math.fabs(location1[0]-location2[0])+math.fabs(location1[1]-location2[1])

def calculate_total_manhattan_distance(state1, state2):
    # [Problem 2 - B]
    # calculate and return a total Manhattan distance between state1 and state2
    locations1=[ [0, 0], [0, 0], [0, 0],
                 [0, 0], [0, 0], [0, 0],
                 [0, 0], [0, 0], [0, 0], ]
    locations2=[ [0, 0], [0, 0], [0, 0],
                 [0, 0], [0, 0], [0, 0],
                 [0, 0], [0, 0], [0, 0], ]


    for i in range(3):
        for j in range(3):
            my_state1=state1.tiles[i][j]
            locations1[my_state1]=[i, j]

            my_state2=state2.tiles[i][j]
            locations2[my_state2]=[i, j]

    total_distance=0
    for i in range(8):
        total_distance+=calculate_manhattan_distance(locations1[1+i], locations2[1+i])

    return total_distance

# [Problem 2 - C]
class GreedyBestFirstSearchFringe(object): # a fringe for the greedy best-first search
    def __init__(self, goal_state, elements=None):
        if not elements:
            elements = []

        # store the goal_state to calculate heuristic values
        self.goal_state=goal_state

        # initialize a queue with the given elements
        self.elements=Queue.PriorityQueue()
        self.insert_all(elements)

    def is_empty(self):
        # return true only if there are no more elements in the queue
        return self.elements.empty()

    def front(self):
        # return the first element of this queue
        return self.elements.queue[0][1]

    def remove_front(self):
        # return self.front() and remove it from the queue
        # HINT: you can use the heapq library in python
        # https://docs.python.org/2/library/heapq.html
        return self.elements.get()[1]

    def insert(self, element):
        # insert an element into the queue (consider a type of queue you will use for this fringe)
        self.elements.put((self.heuristic_function(element), element))

    def insert_all(self, elements):
        # insert a set of elements into the queue
        for element in elements:
            self.insert(element)

    def heuristic_function(self, node):
        # calculate and return a heuristic value of the node
        # use the calculate_total_manhattan_distance function as a heuristic function
        # HINT: use this function as a priority of an element(an instance of Node)
        return calculate_total_manhattan_distance(self.goal_state, node.state)

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
