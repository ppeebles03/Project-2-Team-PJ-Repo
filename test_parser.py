from Minilang.lexer import Lexer
from Minilang.parser import Parser


source = """
int x;
real y;

x = 10 + 5;
y = x * 2.5;

print(y);
"""


lexer = Lexer(source)
tokens = lexer.tokenize()

parser = Parser(tokens)
program = parser.parse()

print("Parser completed successfully!")
print(program)