from dataclasses import dataclass
from .errors import SemanticError


@dataclass
class Symbol:
    name: str
    variable_type: str
    initialized: bool = False
    value: object = None


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def declare(self, name, variable_type):
        if name in self.symbols:
            raise SemanticError(
                f"Semantic Error: Variable '{name}' is already declared."
            )

        self.symbols[name] = Symbol(
            name=name,
            variable_type=variable_type
        )

    def lookup(self, name):
        if name not in self.symbols:
            raise SemanticError(
                f"Semantic Error: Variable '{name}' is not declared."
            )

        return self.symbols[name]

    def set_value(self, name, value):
        symbol = self.lookup(name)
        symbol.value = value
        symbol.initialized = True

    def get_value(self, name):
        symbol = self.lookup(name)

        if not symbol.initialized:
            raise SemanticError(
                f"Semantic Error: Variable '{name}' is not initialized."
            )

        return symbol.value

    def display(self):
        print("\nSymbol Table")
        print("-" * 50)
        print(f"{'Name':<15}{'Type':<10}{'Initialized':<15}{'Value'}")
        print("-" * 50)

        for symbol in self.symbols.values():
            print(
                f"{symbol.name:<15}"
                f"{symbol.variable_type:<10}"
                f"{str(symbol.initialized):<15}"
                f"{symbol.value}"
            )
