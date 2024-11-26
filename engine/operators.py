from abc import ABC, abstractmethod
import re

class Operator(ABC):
    """
    Abstract base class for operators.
    """
    @abstractmethod
    def evaluate(self, left, right):
        pass

class ArithmeticOperator(Operator):
    """
    Handles arithmetic operations.
    """
    def __init__(self, operation):
        self.operation = operation

    def evaluate(self, left, right):
        if self.operation == "+":
            return left + right
        elif self.operation == "-":
            return left - right
        elif self.operation == "*":
            return left * right
        elif self.operation == "/":
            return left / right
        else:
            raise ValueError(f"Unsupported operation: {self.operation}")

class RegexOperator(Operator):
    """
    Handles regex matching operations.
    """
    def evaluate(self, left, pattern):
        return bool(re.match(pattern, str(left)))
