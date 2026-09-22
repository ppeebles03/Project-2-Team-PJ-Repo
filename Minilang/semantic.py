from .ast import (
    Program,
    Declaration,
    Assignment,
    PrintStatement,
    BinaryExpression,
    Identifier,
    Literal,
)
from .errors import SemanticError
from .symbol_table import SymbolTable


class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def analyze(self, program):
        for statement in program.statements:
            self.analyze_statement(statement)

        return self.symbol_table

    def analyze_statement(self, statement):
        if isinstance(statement, Declaration):
            self.symbol_table.declare(
                statement.name,
                statement.variable_type
            )

        elif isinstance(statement, Assignment):
            symbol = self.symbol_table.lookup(statement.name)
            expression_type = self.analyze_expression(
                statement.expression
            )

            if symbol.variable_type == "int" and expression_type == "real":
                raise SemanticError(
                    f"Semantic Error: Cannot assign real expression "
                    f"to int variable '{statement.name}'."
                )

            symbol.initialized = True

        elif isinstance(statement, PrintStatement):
            self.analyze_expression(statement.expression)

    def analyze_expression(self, expression):
        if isinstance(expression, Literal):
            return expression.literal_type

        if isinstance(expression, Identifier):
            symbol = self.symbol_table.lookup(expression.name)

            if not symbol.initialized:
                raise SemanticError(
                    f"Semantic Error: Variable '{expression.name}' "
                    f"is not initialized."
                )

            return symbol.variable_type

        if isinstance(expression, BinaryExpression):
            left_type = self.analyze_expression(expression.left)
            right_type = self.analyze_expression(expression.right)

            if left_type == "real" or right_type == "real":
                return "real"

            return "int"

        raise SemanticError(
            "Semantic Error: Unknown expression."
        )
