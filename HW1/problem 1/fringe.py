# coding: utf-8

import collections

class DepthFirstSearchFringe(object): # a fringe for the depth-first search
    def __init__(self, elements=None):
        if not elements:
            elements = []

        # initialize a queue with the given elements
        self.elements = collections.deque(elements)

    def is_empty(self):
        # return true only if there are no more elements in the queue
        return len(self.elements) == 0

    def front(self):
        # return the first element of this queue
        return self.elements[0]

    def remove_front(self):
        # return self.front() and remove it from the queue
        return self.elements.pop()

    def insert(self, element):
        # insert an element into the queue (consider a type of queue you will use for this fringe)
        self.elements.append(element)

    def insert_all(self, elements):
        # insert a set of elements into the queue
        for element in elements:
            self.insert(element)

# [Problem 1 - A]
class BreadthFirstSearchFringe(object): # a fringe for the breadth-first search
    def __init__(self, elements=None):
        if not elements:
            elements = []

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
        pass

    def insert(self, element):
        # insert an element into the queue (consider a type of queue you will use for this fringe)
        pass

    def insert_all(self, elements):
        # insert a set of elements into the queue
        pass
