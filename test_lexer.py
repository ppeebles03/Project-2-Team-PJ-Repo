from Minilang.lexer import Lexer


source = """
int x;
real y;

x = 10 + 5;
y = x * 2.5;

print(y);
"""


lexer = Lexer(source)
tokens = lexer.tokenize()


for token in tokens:
    print(token)