import sys

from Minilang.lexer import Lexer
from Minilang.parser import Parser
from Minilang.semantic import SemanticAnalyzer
from Minilang.interpreter import Interpreter
from Minilang.errors import (
    MiniLangError,
    LexicalError,
    SyntaxError,
    SemanticError,
    RuntimeError,
)


def read_source(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except OSError as error:
        print(f"Error: Could not read file '{filename}': {error}")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: python compiler.py [--debug] <source_file>")
        sys.exit(1)

    debug = "--debug" in sys.argv
    filenames = [arg for arg in sys.argv[1:] if arg != "--debug"]

    if not filenames:
        print("Usage: python compiler.py [--debug] <source_file>")
        sys.exit(1)

    filename = filenames[0]
    source = read_source(filename)

    try:
        lexer = Lexer(source)
        tokens = lexer.tokenize()

        if debug:
            print("=== TOKENS ===")
            for token in tokens:
                print(token)

        parser = Parser(tokens)
        program = parser.parse()

        if debug:
            print("\n=== AST ===")
            print(program)

        analyzer = SemanticAnalyzer()
        symbol_table = analyzer.analyze(program)

        interpreter = Interpreter(symbol_table)
        output = interpreter.execute(program)

        if debug:
            symbol_table.display()
            print("\n=== PROGRAM OUTPUT ===")

        for value in output:
            print(value)

    except LexicalError as error:
        print(error)
        sys.exit(1)

    except SyntaxError as error:
        print(error)
        sys.exit(1)

    except SemanticError as error:
        print(error)
        sys.exit(1)

    except RuntimeError as error:
        print(error)
        sys.exit(1)

    except MiniLangError as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
