#!/usr/bin/python3

"""
Implementing a binary heap using priority queue
"""

class BinaryHeap:
    def __init__(self):
        self.heap = [0]
        self.length = 0

    def add(self, value):
        """
        Inserts the expected value in its correct position maintaining heap shape and structure
        """
        self.heap.append(value)
        self.length += 1
        i = self.length 
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    
    def print(self):
        print(self.heap)

new = BinaryHeap()

inlist = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27, 12]

for i in inlist:
    new.add(i)
new.add(2)
new.print()
new.delete()
new.print()

