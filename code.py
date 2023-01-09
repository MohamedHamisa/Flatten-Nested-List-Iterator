class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]
    
    def next(self):
        return self.stack.pop().getInteger()
#return the single integer that this NestedInteger holds, if it holds a single integer
#Return None if this NestedInteger holds a nested list
        
    def hasNext(self):
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            self.stack.extend(self.stack.pop().getList()[::-1]) # pop off the top element and the extend it with the new inner lists
        return False


