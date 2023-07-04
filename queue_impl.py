# -*- coding: utf-8 -*-
"""Queue File"""


class Queue:
    """Queue implementation using a list"""

    def __init__(self):
        """Init"""
        self.items = []

    def is_empty(self):
        """Check if queue is empty"""
        return self.items == []

    def enqueue(self, item):
        """Add item to queue"""
        self.items.insert(0, item)

    def dequeue(self):
        """Remove item from queue"""
        return self.items.pop()
