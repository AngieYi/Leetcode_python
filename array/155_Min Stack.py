'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack(object):
    # 51.81%
    def __init__(self):
        self.stack= []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.stack:              # if it's the first element
            self.stack.append((x,x))    # save a tuple at the end of array
        else:
            self.stack.append((x,min(x,self.stack[-1][1]))) # second element of top element always the mini element


    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack:          # always need to judge whether it's empty
            self.stack.pop()    # pop the top elements and return nothing


    def top(self):
        """
        :rtype: int
        """
        if self.stack:          # always need to judge whether it's empty
            return self.stack[-1][0]    # just return the first element of the top tuple
        else:
            return None


    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:          # always need to judge whether it's empty
            return self.stack[-1][1]    # just return the second element of the top tuple
        else:
            return None


minStack = MinStack()
print minStack.push(-2);
print minStack.push(0);
print minStack.push(-3);
print minStack.getMin();
print minStack.pop();
print minStack.top();
print minStack.getMin();
