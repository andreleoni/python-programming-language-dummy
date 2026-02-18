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

def test_lexer():
  assert lexer("1 + 1") == ["1", "+", "1"]
  assert lexer(sum_variables) == ['a', '=', '1', 'b', '=', '2', 'a', '+', 'b']
  assert lexer("(1 * 2) - 1") == ["(", "1", "*", "2", ")", "-", "1"]
  assert lexer(function_declare) == ["func", "myfunc", "(", "a", ",", "b", ")", "{", "return", "a", "+", "b", "}", "myfunc", "(", "1", ",", "2", ")"]
