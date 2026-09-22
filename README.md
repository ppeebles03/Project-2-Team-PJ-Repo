# CS3210 Project 2 - MiniLang Interpreter

## Project Description

This project implements an interpreter for the MiniLang programming language.

The interpreter processes MiniLang programs through the following stages:

1. Lexical analysis
2. Parsing and AST construction
3. Semantic analysis
4. Interpretation

## Requirements

- Python 3
- No external Python packages are required.

## Running the Interpreter

From the project root directory, run:

python3 compiler.py program1.mini

Replace program1.mini with any MiniLang source file.

Example:

python3 compiler.py program3.mini

## Debug Mode

Use the --debug option to display the internal processing stages:

python3 compiler.py --debug program1.mini

Debug mode displays:

- Token stream
- AST
- Final symbol table
- Program output

## Test Programs

The project includes 11 MiniLang test programs.

Run all tests with:

for file in program{1..11}.mini; do echo "===== $file ====="; python3 compiler.py "$file"; done

Expected results:

program1.mini:
20.0

program2.mini:
20

program3.mini:
14
20

program4.mini:
Semantic Error: Variable 'y' is not declared.

program5.mini:
Semantic Error: Variable 'x' is already declared.

program6.mini:
Semantic Error: Variable 'x' is not initialized.

program7.mini:
Semantic Error: Cannot assign real expression to int variable 'x'.

program8.mini:
10.0

program9.mini:
Runtime Error: Division by zero.

program10.mini:
Lexical Error on line 3: Unknown character '@'

program11.mini:
Syntax Error on line 3: Expected ';' after declaration.

## Error Handling

The interpreter reports errors by category:

- Lexical Error
- Syntax Error
- Semantic Error
- Runtime Error

Errors are reported without raw Python stack traces.

## MiniLang Features

The interpreter supports:

- int and real variable declarations
- variable assignments
- integer and real literals
- arithmetic operators: +, -, *, /
- parentheses
- operator precedence
- variable references
- print statements
- int to real promotion
- semantic checking
- division-by-zero detection

## Example

A MiniLang program can contain:

int x;
x = 5;
int y;
y = 3;
print(x + y * 5);

The interpreter evaluates the expression using normal operator precedence.

## Project Structure

compiler.py
    Main program used to run the interpreter.

Minilang/
    Lexer, parser, AST, semantic analyzer, symbol table,
    interpreter, and error handling modules.

program1.mini - program11.mini
    MiniLang test programs.

test_lexer.py
    Lexer tests.

test_parser.py
    Parser tests.

## Authors

Team PJ
CS 3210 - Project 2
