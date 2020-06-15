import collections

class Queue:
    def __init__(self):
        self._data = collections.deque([])

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.popleft()

    def isEmpty(self):
        #---------------Enter your source code here----------------#
        #Return True if the queue is empty, False otherwise
        if not self._data:
            return True
        else:
            return False


    def size(self):
        #---------------Enter your source code here----------------#
        #return the number of elements in the queue
        return len(self._data)

    def toString(self):
        return self._data
