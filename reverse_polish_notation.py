def evalRPN(tokens: list[str]) -> int:
    curr_operands = []

    for token in tokens:
        if token == "+":
            curr_operands.append(curr_operands.pop() + curr_operands.pop())
        elif token == "-":
            second = curr_operands.pop()
            first = curr_operands.pop()
            diff = first - second
            curr_operands.append(diff)
        elif token == "*":
            curr_operands.append(curr_operands.pop() * curr_operands.pop())
        elif token == "/":
            second = curr_operands.pop()
            first = curr_operands.pop()
            quot = int(first / second)
            curr_operands.append(quot)
        else:
            curr_operands.append(int(token))

    return curr_operands.pop()

if __name__ == "__main__":
    print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
