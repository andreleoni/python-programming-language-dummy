from lexer import lexer
from parser import parser
from interpreter import Interpreter

def main(language: str):
    tokens = lexer(language)
    ast = parser(tokens)
    result = Interpreter().evaluate(ast)
    return str(result)