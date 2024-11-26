# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF, ID, REGEX, COMMA, STRING = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', '(', ')', 'EOF', 'ID', 'REGEX', 'COMMA', 'STRING'
)


class Token:
    def __init__(self, type, value):
        self.type = type  # Token type: INTEGER, PLUS, MINUS, etc.
        self.value = value  # Token value: numbers, operators, etc.

    def __str__(self):
        return f'Token({self.type}, {repr(self.value)})'

    def __repr__(self):
        return self.__str__()


