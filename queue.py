class StackEmptyException(Exception):
   def __init__(self):
       super(StackEmptyException, self).__init__("Stack is empty")


class StackFullException(Exception):
   def __init__(self):
       super(StackFullException, self).__init__("Stack is full")


class Stack(object):
   def __init__(self, stack_size):
       self.data = []
       self.stack_size = stack_size

   def pop(self):
       if len(self.data) == 0:
         raise StackEmptyException()

       return self.data.pop()

   def push(self, element):
       if len(self.data) == self.stack_size:
           raise StackFullException()

       self.data.append(element)

   def peek(self):
       if len(self.data) == 0:
           raise StackEmptyException()

       return self.data[-1]

   def is_empty(self):
       if len(self.data) == 0:
           return True
       return False


class QueueEmptyException(Exception):
   def __init__(self):
       super(QueueEmptyException, self).__init__("Queue is empty")


class QueueFullException(Exception):
   def __init__(self):
       super(QueueFullException, self).__init__("Queue is full")


class SQueue(object):
   def __init__(self, queue_size):
       self.stack_main = Stack(queue_size)
       self.queue_size = queue_size
       self.current_size = 0
       self.front = None

   def is_empty(self):
       if self.current_size == 0:
           return True
       return False

   def clear(self):
       while self.current_size > 0:
           self.dequeue()

   def enqueue(self, num):
       if self.current_size == self.queue_size:
           raise QueueFullException()
       self.stack_main.push(num)
       if self.front is None:
           self.front = num

       self.current_size += 1

   def dequeue(self):
       if self.current_size == 0:
           raise QueueEmptyException()

       stack_aux = Stack(self.current_size)
       ret_val = None

       while not (self.stack_main.is_empty()):
           ret_val = self.stack_main.pop()
           stack_aux.push(ret_val)

       stack_aux.pop()

       if not stack_aux.is_empty():
           self.front = stack_aux.peek()

       while not(stack_aux.is_empty()):
           self.stack_main.push(stack_aux.pop())

       self.current_size -= 1

       return ret_val

   def get_front(self):
       if self.current_size == 0:
           raise QueueEmptyException()

       return self.front

"""
q= SQueue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
# q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
"""
