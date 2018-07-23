class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        self.stack1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        if len(self.stack2)==0 and len(self.stack1)==0:
            return None
        if len(self.stack2)==0:
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    """
    @return: An integer
    """
    def top(self):
        if len(self.stack2)==0 and len(self.stack1)==0:
            return None
        if len(self.stack2)==0:
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

if __name__ == '__main__':
    my_queue=MyQueue()
    my_queue.push(1)
    print(my_queue.pop())
    my_queue.push(2)
    my_queue.push(3)
    print(my_queue.top())
    print(my_queue.pop())


