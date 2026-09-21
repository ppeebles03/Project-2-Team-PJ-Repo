from .token import TokenType
from .errors import SyntaxError
from .ast import (
    Program,
    Declaration,
    Assignment,
    PrintStatement,
    BinaryExpression,
    Identifier,
    Literal,
)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        statements = []

        while not self.check(TokenType.EOF):
            statements.append(self.statement())

        return Program(statements)

    def statement(self):
        if self.match(TokenType.INT):
            return self.declaration("int")

        if self.match(TokenType.REAL):
            return self.declaration("real")

        if self.match(TokenType.PRINT):
            return self.print_statement()

        if self.check(TokenType.IDENTIFIER):
            return self.assignment()

        token = self.peek()

        raise SyntaxError(
            f"Syntax Error on line {token.line}: "
            f"Unexpected token '{token.lexeme}'"
        )

    def declaration(self, variable_type):
        name = self.consume(
            TokenType.IDENTIFIER,
            "Expected identifier after type."
        )

        self.consume(
            TokenType.SEMICOLON,
            "Expected ';' after declaration."
        )

        return Declaration(
            variable_type,
            name.lexeme
        )

    def assignment(self):
        name = self.consume(
            TokenType.IDENTIFIER,
            "Expected identifier."
        )

        self.consume(
            TokenType.ASSIGN,
            "Expected '=' after identifier."
        )

        expression = self.expression()

        self.consume(
            TokenType.SEMICOLON,
            "Expected ';' after assignment."
        )

        return Assignment(
            name.lexeme,
            expression
        )

    def print_statement(self):
        self.consume(
            TokenType.LEFT_PAREN,
            "Expected '(' after print."
        )

        expression = self.expression()

        self.consume(
            TokenType.RIGHT_PAREN,
            "Expected ')' after expression."
        )

        self.consume(
            TokenType.SEMICOLON,
            "Expected ';' after print statement."
        )

        return PrintStatement(expression)

    def expression(self):
        expression = self.term()

        while self.match(
            TokenType.PLUS,
            TokenType.MINUS
        ):
            operator = self.previous().lexeme
            right = self.term()

            expression = BinaryExpression(
                expression,
                operator,
                right
            )

        return expression

    def term(self):
        expression = self.factor()

        while self.match(
            TokenType.MULTIPLY,
            TokenType.DIVIDE
        ):
            operator = self.previous().lexeme
            right = self.factor()

            expression = BinaryExpression(
                expression,
                operator,
                right
            )

        return expression

    def factor(self):
        if self.match(TokenType.INTEGER_LITERAL):
            token = self.previous()

            return Literal(
                int(token.lexeme),
                "int"
            )

        if self.match(TokenType.REAL_LITERAL):
            token = self.previous()

            return Literal(
                float(token.lexeme),
                "real"
            )

        if self.match(TokenType.IDENTIFIER):
            return Identifier(
                self.previous().lexeme
            )

        if self.match(TokenType.LEFT_PAREN):
            expression = self.expression()

            self.consume(
                TokenType.RIGHT_PAREN,
                "Expected ')' after expression."
            )

            return expression

        token = self.peek()

        raise SyntaxError(
            f"Syntax Error on line {token.line}: "
            f"Expected expression."
        )

    def match(self, *types):
        for token_type in types:
            if self.check(token_type):
                self.advance()
                return True

        return False

    def consume(self, token_type, message):
        if self.check(token_type):
            return self.advance()

        token = self.peek()

        raise SyntaxError(
            f"Syntax Error on line {token.line}: {message}"
        )

    def check(self, token_type):
        return self.peek().type == token_type

    def advance(self):
        if not self.check(TokenType.EOF):
            self.current += 1

        return self.previous()

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]