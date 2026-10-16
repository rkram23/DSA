from DSAStack import DSAStack
from DSAQueue import DSACircularQueue


class EquationSolver:

    def solve(self, equation):
        postfixQueue = self._parseInfixToPostfix(equation)
        return self._evaluatePostfix(postfixQueue)

    def _parseInfixToPostfix(self, equation):
        tokens = equation.split(" ")
        operatorStack = DSAStack(len(tokens) + 1)
        postfixQueue = DSACircularQueue(len(tokens) + 1)

        for token in tokens:
            if token != "":
                ch = token[0]
            

            if ch in "+-*/":
                while (not operatorStack.isEmpty()
                       and operatorStack.top() != '('
                       and self._precedenceOf(operatorStack.top()) >= self._precedenceOf(ch)):
                    postfixQueue.enqueue(operatorStack.pop())
                operatorStack.push(ch)

            elif ch == '(':
                operatorStack.push(ch)

            elif ch == ')':
                while operatorStack.top() != '(':
                    postfixQueue.enqueue(operatorStack.pop())
                operatorStack.pop()  # discard the '('

            else:
                postfixQueue.enqueue(float(token))

        while not operatorStack.isEmpty():
            postfixQueue.enqueue(operatorStack.pop())

        return postfixQueue

    def _evaluatePostfix(self, postfixQueue):
        operandStack = DSAStack(postfixQueue.getCount() + 1)

        while not postfixQueue.isEmpty():
            term = postfixQueue.dequeue()

            if isinstance(term, str):  # operator
                op2 = operandStack.pop()
                op1 = operandStack.pop()
                result = self._executeOperation(term, op1, op2)
                operandStack.push(result)
            else:  # operand (float)
                operandStack.push(term)

        return operandStack.pop()

    def _executeOperation(self, op, op1, op2):
        if op == '+':
            return op1 + op2
        elif op == '-':
            return op1 - op2
        elif op == '*':
            return op1 * op2
        elif op == '/':
            return op1 / op2
        else:
            raise Exception(f"Unknown operator: {op}")

    def _precedenceOf(self, theOp):
        if theOp in ('+', '-'):
            return 1
        elif theOp in ('*', '/'):
            return 2
        else:
            return 0