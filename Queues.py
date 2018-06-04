from queue import deque

queue = deque() # Create empty queue

queue.append("Oscar") # Append to right side of queue
queue.append("Edgy")
queue.append("Andres")

queue.appendleft("Sebastian") # Append to leftside of queue or begining

queue.popleft() # Pop first element in queue
queue.pop() # Pop last element in queue

print(queue.count("Oscar")) # count number of elements equal to input

print(queue)