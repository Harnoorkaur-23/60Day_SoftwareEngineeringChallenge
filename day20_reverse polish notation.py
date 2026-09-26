def evalRPN(tokens):
    stack = []
    
    for t in tokens:
        if t == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif t == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif t == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif t == "/":
            b = stack.pop()
            a = stack.pop()
            # int() in Python truncates decimal values toward zero
            stack.append(int(a / b))
        else:
            # If it is a number, turn it into an integer and add to stack
            stack.append(int(t))
            
    # The last remaining number is the final answer
    return stack[0]
