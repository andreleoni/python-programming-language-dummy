import re

def lexer(expr):
  return re.findall(r"[a-zA-Z_]+|\d+|==|!=|>=|<=|=|>|<|[+\-*\/]|[()]|[{}]|[,;]", expr)
