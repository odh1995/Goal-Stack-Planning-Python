class Stack:
    def __init__(self):
        self._data = []

    def __contains__(self):
        return self._data

    def push(self, value):
        self._data.append(value)


    def pop(self):
        return self._data.pop()

    def peek(self):
        #---------------Enter your source code here----------------#
        #Return the value of the element at the top of the stack without removing it from the stack
        return self._data[len(self._data) - 1]

    def isEmpty(selfs):
        return len(selfs._data) == 0


    def peekAt(self,i):
        #---------------Enter your source code here----------------#
        #Return the value of the element at index i without removing it from the stack
        return self._data[i]

    def size(self):
        #---------------Enter your source code here----------------#
        #Return the number of elements in the stack
        return len(self._data)

    def copyFrom(self, aStack):
        #---------------Enter your source code here----------------#
        #Copy all the elements from the input stack aStack to this stack
        for i in range(aStack.size()):
            self.push(aStack.peekAt(i))

    def toString(self):
        #---------------Enter your source code here----------------#
        #Return a string representing the content of this stack
        # str = ''.join(self._data)

        return str(self._data)
