class MinStack:

    def __init__(self):
        
        self.main_stack = []
       
        self.min_stack = []

    def push(self, val: int) -> None:
        # 1. Always add the number to the main stack
        self.main_stack.append(val)
        
        # 2. Add the number to the min stack too, but follow a rule:
        # If the min stack is empty, this new val is the minimum.
        # Otherwise, compare the new val with the current minimum on top of the min stack.
        # We push whichever number is smaller.
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = self.min_stack[-1]
            if val < current_min:
                self.min_stack.append(val)
            else:
                self.min_stack.append(current_min)

    def pop(self) -> None:
        # Remove the top element from both stacks to keep them perfectly synced
        self.main_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Return the last item in the main stack (-1 gets the last item in Python)
        return self.main_stack[-1]

    def getMin(self) -> int:
        # The top element of the min stack will always be the smallest number currently in the stack
        return self.min_stack[-1]
