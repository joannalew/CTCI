# LeetCode 155: Min Stack
# Design a stack that supports push, pop, top, 
#   and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# Example:
#   MinStack minStack = new MinStack();
#   minStack.push(-2);
#   minStack.push(0);
#   minStack.push(-3);
#   minStack.getMin();   --> Returns -3.
#   minStack.pop();
#   minStack.top();      --> Returns 0.
#   minStack.getMin();   --> Returns -2.

class MinStack:
    def __init__(self):
        self.store = []
        
    def push(self, x):
        self.store.append((x, min(x, self.getMin())))

    def pop(self):
        el = self.store.pop()
        return el[0]

    def top(self):
        return self.store[-1][0]
        
    def getMin(self):
        if len(self.store) < 1:
            return 2147483647
        return self.store[-1][1]

def main():
    m = MinStack()
    m.push(1)
    m.push(3)
    m.push(2)
    m.push(5)
    m.push(-1)
    m.push(0)

    print(m.getMin()) # => -1
    m.pop()
    print(m.getMin()) # => -1
    m.pop()
    print(m.getMin()) # => 1
    print(m.top())    # => 5

if __name__ == "__main__":
    main()