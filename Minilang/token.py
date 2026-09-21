from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    INT = auto()
    REAL = auto()
    PRINT = auto()

    IDENTIFIER = auto()

    INTEGER_LITERAL = auto()
    REAL_LITERAL = auto()

    ASSIGN = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()

    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    SEMICOLON = auto()

    EOF = auto()


@dataclass
class Token:
    type: TokenType
    lexeme: str
    line: int
    column: int

    def __str__(self):
        return f"{self.type.name}('{self.lexeme}')"