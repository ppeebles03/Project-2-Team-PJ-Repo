from dataclasses import dataclass
from typing import List


class ASTNode:
    pass


@dataclass
class Program(ASTNode):
    statements: List[ASTNode]


@dataclass
class Declaration(ASTNode):
    variable_type: str
    name: str


@dataclass
class Assignment(ASTNode):
    name: str
    expression: ASTNode


@dataclass
class PrintStatement(ASTNode):
    expression: ASTNode


@dataclass
class BinaryExpression(ASTNode):
    left: ASTNode
    operator: str
    right: ASTNode


@dataclass
class Identifier(ASTNode):
    name: str


@dataclass
class Literal(ASTNode):
    value: object
    literal_type: str