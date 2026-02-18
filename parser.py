from asyntotictree import *

from typing import List, Any

class Cursor:
    def __init__(self, tokens: list[str]):
        self.tokens = tokens
        self.i = 0

    def peek(self) -> str | None:
        return self.tokens[self.i] if self.i < len(self.tokens) else None

    def peek_next(self) -> str | None:
        return self.tokens[self.i + 1] if self.i + 1 < len(self.tokens) else None

    def consume(self, expected: str | None = None) -> str:
        tok = self.peek()
        if tok is None:
            raise ValueError("fim inesperado do input")
        if expected is not None and tok != expected:
            raise ValueError(f"esperava {expected!r}, veio {tok!r}")
        self.i += 1
        return tok


def is_ident(tok: str | None) -> bool:
    return tok is not None and tok.isidentifier()


def atom(tok: str):
    if tok.isdigit():
        return NumberNode(value=int(tok))
    return VarNode(name=tok)

def parse_call(cur: Cursor):
    name = str(cur.consume())
    cur.consume("(")

    args: List[Any] = []

    if cur.peek() != ")":
        args.append(parse_expr(cur))

        while cur.peek() == ",":
            cur.consume(",")
            args.append(parse_expr(cur))

    cur.consume(")")
    return CallNode(
        name=name,
        args=args
    )

def parse_funcdef(cur: Cursor) -> FuncDefNode:
    cur.consume("func")

    name = cur.consume()
    params = []
    body = []

    # parâmetros
    cur.consume("(")
    if cur.peek() != ")":
        params.append(cur.consume())
        while cur.peek() == ",":
            cur.consume(",")
            params.append(cur.consume())
    cur.consume(")")

    # corpo
    cur.consume("{")
    while cur.peek() != "}":
        body.append(parse_statement(cur))
        if cur.peek() == ";":
            cur.consume(";")
    cur.consume("}")

    return FuncDefNode(name=name, params=params, body=body)

def parse_factor(cur: Cursor):
    tok = cur.peek()

    if is_ident(tok) and cur.peek_next() == "(":
        return parse_call(cur)

    if tok == "(":
        cur.consume("(")
        node = parse_expr(cur)
        cur.consume(")")
        return node

    # número ou variável
    return atom(cur.consume())


def parse_term(cur: Cursor):
    node = parse_factor(cur)

    while cur.peek() in ("*", "/"):
        op = cur.consume()
        right = parse_factor(cur)
        node = BinaryNode(left=node, op=op, right=right)

    return node


def parse_expr(cur: Cursor):
    node = parse_term(cur)

    while cur.peek() in ("+", "-"):
        op = cur.consume()
        right = parse_term(cur)
        node = BinaryNode(left=node, op=op, right=right)

    return node


def parse_statement(cur: Cursor):
    # AQUI NASCE AS RESERVED KEYWORDS
    if cur.peek() == "func":
        return parse_funcdef(cur)

    if cur.peek() == "return":
        cur.consume("return")
        value = parse_expr(cur)
        return ReturnNode(value=value)

    # assignment: a = expr
    if is_ident(cur.peek()) and cur.peek_next() == "=":
        name = cur.consume()
        cur.consume("=")
        value = parse_expr(cur)
        return AssignNode(name=name, value=value)

    # senão, é expressão normal
    return parse_expr(cur)

def parser(tokens: list[str]) -> ProgramNode:
    cur = Cursor(tokens)
    statements = []

    while cur.peek() is not None:
        statements.append(parse_statement(cur))

    return ProgramNode(body=statements)