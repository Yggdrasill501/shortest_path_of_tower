# -*- coding: utf-8 -*-
"""Queue File"""


class Queue:
    """Queue implementation using a list"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
