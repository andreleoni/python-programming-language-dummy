from lexer import lexer

sum_variables = """
a = 1
b = 2
a + b"""

function_declare = """
func myfunc(a,b) {
  return a + b
}

myfunc(1, 2)
"""

ifelse = """
if a > 1 {
  2
} else {
  3
}
"""


function_declare_with_if = """
func myfunc(a,b) {
  if (a + b) >= 2 {
    return 1
  } else {
    return 2
  }
}

myfunc(1, 2)
"""

def test_lexer():
  assert lexer("1 + 1") == ["1", "+", "1"]
  assert lexer(sum_variables) == ['a', '=', '1', 'b', '=', '2', 'a', '+', 'b']
  assert lexer("(1 * 2) - 1") == ["(", "1", "*", "2", ")", "-", "1"]
  assert lexer(function_declare) == ["func", "myfunc", "(", "a", ",", "b", ")", "{", "return", "a", "+", "b", "}", "myfunc", "(", "1", ",", "2", ")"]
  assert lexer(ifelse) == ["if", "a", ">", "1", "{", "2", "}", "else", "{", "3", "}"]
  assert lexer(function_declare_with_if) == ['func', 'myfunc', '(', 'a', ',', 'b', ')', '{', 'if', '(', 'a', '+', 'b', ')', '>=', '2', '{', 'return', '1', '}', 'else', '{', 'return', '2', '}', '}', 'myfunc', '(', '1', ',', '2', ')']
