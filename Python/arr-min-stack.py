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