class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit =limit
    def isEmpty(self): 
        return len(self.items) == 0 
    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            return f'Stack is full'
        return self.items

    def pop(self):
        if not self.isEmpty(): 
            return self.items.pop() 
    def peek(self):
        self.item.peek()
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.size() >= self.limit

    def search(self, target):
        for num in (self.items): 
             if num == target: 
                 return sorted(self.items , reverse=True).index(num) 
        return -1
