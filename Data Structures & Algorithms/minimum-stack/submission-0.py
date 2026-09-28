class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, value):
        self.stack.append(value)
        if self.minStack==[]:
           self.minStack.append(value)
        elif self.minStack[-1] >= value:
            self.minStack.append(value)
        else:
            self.minStack.append(self.minStack[-1])    




    def pop(self):
        del self.stack[len(self.stack) - 1]
        del self.minStack[len(self.minStack) - 1]
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        if self.minStack == []:
            return None
        else:
            return self.minStack[-1]
        
