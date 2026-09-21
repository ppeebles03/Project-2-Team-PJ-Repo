from .token import Token, TokenType
from .errors import LexicalError


class Lexer:
    KEYWORDS = {
        "int": TokenType.INT,
        "real": TokenType.REAL,
        "print": TokenType.PRINT,
    }

    def __init__(self, source):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1

    def tokenize(self):
        tokens = []

        while not self.is_at_end():
            self.skip_whitespace()

            if self.is_at_end():
                break

            tokens.append(self.next_token())

        tokens.append(
            Token(TokenType.EOF, "", self.line, self.column)
        )

        return tokens

    def next_token(self):
        char = self.peek()

        if char.isalpha():
            return self.identifier_or_keyword()

        if char.isdigit():
            return self.number()

        line = self.line
        column = self.column

        if char == "=":
            self.advance()
            return Token(TokenType.ASSIGN, "=", line, column)

        if char == "+":
            self.advance()
            return Token(TokenType.PLUS, "+", line, column)

        if char == "-":
            self.advance()
            return Token(TokenType.MINUS, "-", line, column)

        if char == "*":
            self.advance()
            return Token(TokenType.MULTIPLY, "*", line, column)

        if char == "/":
            self.advance()
            return Token(TokenType.DIVIDE, "/", line, column)

        if char == "(":
            self.advance()
            return Token(TokenType.LEFT_PAREN, "(", line, column)

        if char == ")":
            self.advance()
            return Token(TokenType.RIGHT_PAREN, ")", line, column)

        if char == ";":
            self.advance()
            return Token(TokenType.SEMICOLON, ";", line, column)

        raise LexicalError(
            f"Lexical Error on line {line}: Unknown character '{char}'"
        )

    def identifier_or_keyword(self):
        line = self.line
        column = self.column

        start = self.position

        while (
            not self.is_at_end()
            and (
                self.peek().isalnum()
                or self.peek() == "_"
            )
        ):
            self.advance()

        text = self.source[start:self.position]

        token_type = self.KEYWORDS.get(
            text,
            TokenType.IDENTIFIER
        )

        return Token(token_type, text, line, column)

    def number(self):
        line = self.line
        column = self.column

        start = self.position

        while (
            not self.is_at_end()
            and self.peek().isdigit()
        ):
            self.advance()

        if (
            not self.is_at_end()
            and self.peek() == "."
        ):
            self.advance()

            if (
                self.is_at_end()
                or not self.peek().isdigit()
            ):
                raise LexicalError(
                    f"Lexical Error on line {line}: "
                    f"Invalid real number"
                )

            while (
                not self.is_at_end()
                and self.peek().isdigit()
            ):
                self.advance()

            text = self.source[start:self.position]

            return Token(
                TokenType.REAL_LITERAL,
                text,
                line,
                column
            )

        text = self.source[start:self.position]

        return Token(
            TokenType.INTEGER_LITERAL,
            text,
            line,
            column
        )

    def skip_whitespace(self):
        while not self.is_at_end():
            char = self.peek()

            if char == " " or char == "\t":
                self.advance()

            elif char == "\n":
                self.advance()

            else:
                break

    def peek(self):
        if self.is_at_end():
            return "\0"

        return self.source[self.position]

    def advance(self):
        char = self.source[self.position]
        self.position += 1

        if char == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        return char

    def is_at_end(self):
        return self.position >= len(self.source)