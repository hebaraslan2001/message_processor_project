from engine.parser_2 import Lexer, Parser
from engine.operators import ArithmeticOperator, RegexOperator

class ProcessingEngine:
    def __init__(self, equation):
        self.equation = equation

    def evaluate(self, node, message):
        """
        Recursively evaluate the AST using operators.
        """
        if isinstance(node.value, int):  # Numeric literal
            return node.value
        if node.value == "ATTR":  # Dynamic value
            return message["value"]
        if node.value in ("+", "-", "*", "/"):  # Arithmetic operations
            left = self.evaluate(node.left, message)
            right = self.evaluate(node.right, message)
            operator = ArithmeticOperator(node.value)
            return operator.evaluate(left, right)
        elif node.value == "Regex":  # Regex operations
            left = self.evaluate(node.left, message)
            pattern = node.right.value
            operator = RegexOperator()
            return operator.evaluate(left, pattern)
        else:
            raise ValueError(f"Unsupported operation: {node.value}")

    def process_message(self, message):
        """
        Parse the equation, build the AST, and evaluate it.
        """
        lexer = Lexer(self.equation)
        parser = Parser(lexer)
        ast = parser.parse()  # Build the AST
        return self.evaluate(ast, message)  # Evaluate the AST




# from engine.parser_2 import Lexer, Interpreter

# class ProcessingEngine:
#     def __init__(self, equation):
#         """
#         Initialize the processing engine with the equation to evaluate.
#         :param equation: A string equation (e.g., "ATTR + 50 * (ATTR / 10)" or "Regex(ATTR, '^dog')")
#         """
#         self.equation = equation

#     def process_message(self, message):
#         """
#         Process a message by evaluating the equation with dynamic values.
#         :param message: A dictionary containing attributes like {"value": 100}
#         :return: The result of the evaluation (e.g., numeric value or True/False for regex)
#         """
#         # Create a lexer for the equation
#         # breaking the equation (string) into a series of tokens.
#         lexer = Lexer(self.equation)

#         # Create an interpreter with the lexer and the message
        
#         interpreter = Interpreter(lexer, message)

#         # Evaluate the equation and return the result
#         return interpreter.expr()