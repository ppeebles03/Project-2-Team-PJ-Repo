from .ast import (
    Program,
    Declaration,
    Assignment,
    PrintStatement,
    BinaryExpression,
    Identifier,
    Literal,
)
from .errors import RuntimeError


class Interpreter:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def execute(self, program):
        output = []

        for statement in program.statements:
            result = self.execute_statement(statement)

            if isinstance(statement, PrintStatement):
                output.append(result)

        return output

    def execute_statement(self, statement):
        if isinstance(statement, Declaration):
            return None

        if isinstance(statement, Assignment):
            value = self.evaluate(statement.expression)

            symbol = self.symbol_table.lookup(statement.name)

            if symbol.variable_type == "int":
                value = int(value)
            elif symbol.variable_type == "real":
                value = float(value)

            self.symbol_table.set_value(
                statement.name,
                value
            )

            return None

        if isinstance(statement, PrintStatement):
            return self.evaluate(statement.expression)

        raise RuntimeError(
            "Runtime Error: Unknown statement."
        )

    def evaluate(self, expression):
        if isinstance(expression, Literal):
            return expression.value

        if isinstance(expression, Identifier):
            return self.symbol_table.get_value(
                expression.name
            )

        if isinstance(expression, BinaryExpression):
            left = self.evaluate(expression.left)
            right = self.evaluate(expression.right)

            if expression.operator == "+":
                return left + right

            if expression.operator == "-":
                return left - right

            if expression.operator == "*":
                return left * right

            if expression.operator == "/":
                if right == 0:
                    raise RuntimeError(
                        "Runtime Error: Division by zero."
                    )

                result = left / right

                if isinstance(left, int) and isinstance(right, int):
                    return int(result)

                return result

            raise RuntimeError(
                f"Runtime Error: Unknown operator "
                f"'{expression.operator}'."
            )

        raise RuntimeError(
            "Runtime Error: Unknown expression."
        )
