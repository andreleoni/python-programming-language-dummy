from dataclasses import dataclass
from typing import Any, List

@dataclass
class ProgramNode:
    body: List[Any]

@dataclass
class BinaryNode():
  left: Any
  op: str
  right: Any

@dataclass
class NumberNode():
  value: int

@dataclass
class VarNode:
    name: str

@dataclass
class AssignNode:
    name: str
    value: Any

@dataclass
class FuncDefNode:
   name: str
   params: List[str]
   body: List[Any]

@dataclass
class CallNode:
    name: str
    args: list[Any]

OPERATIONS = {
  "+": BinaryNode,
  "-": BinaryNode,
  "*": BinaryNode,
}


@dataclass
class ReturnNode:
    value: Any