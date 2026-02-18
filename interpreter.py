from asyntotictree import *

class ReturnSignal(Exception):
    def __init__(self, value):
        self.value = value

class Interpreter:
    def __init__(self):
        self.functions = {}
        self.env = {}

    def evaluate(self, node):
        # programa
        if isinstance(node, ProgramNode):
            result = None
            for stmt in node.body:
                result = self.evaluate(stmt)
            return result

        # define função (não executa corpo)
        if isinstance(node, FuncDefNode):
            self.functions[node.name] = node
            return None

        # return
        if isinstance(node, ReturnNode):
            value = self.evaluate(node.value)
            raise ReturnSignal(value)

        # chamada de função
        if isinstance(node, CallNode):
            fn = self.functions.get(node.name)
            if fn is None:
                raise NameError(f"função não definida: {node.name}")

            if len(node.args) != len(fn.params):
                raise TypeError(
                    f"{node.name} espera {len(fn.params)} args, recebeu {len(node.args)}"
                )

            arg_values = [self.evaluate(a) for a in node.args]

            old_env = self.env
            local_env = dict(old_env)  # simples por enquanto
            for p, v in zip(fn.params, arg_values):
                local_env[p] = v
            self.env = local_env

            try:
                result = None
                for stmt in fn.body:
                    result = self.evaluate(stmt)
                return result  # se não tiver return, retorna última expr
            except ReturnSignal as r:
                return r.value
            finally:
                self.env = old_env

        # literais/variáveis
        if isinstance(node, NumberNode):
            return node.value

        if isinstance(node, VarNode):
            if node.name not in self.env:
                raise NameError(f"variável não definida: {node.name}")
            return self.env[node.name]

        if isinstance(node, AssignNode):
            value = self.evaluate(node.value)
            self.env[node.name] = value
            return value

        # binários
        if isinstance(node, BinaryNode):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)

            if node.op == "+":
                return left + right
            if node.op == "-":
                return left - right
            if node.op == "*":
                return left * right
            if node.op == "/":
                return left / right

            raise ValueError(f"operador não suportado: {node.op}")

        raise TypeError(f"nó desconhecido: {type(node)}")