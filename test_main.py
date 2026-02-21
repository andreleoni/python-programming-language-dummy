from main import main


sum_variables = """
a = 1
b = 2
a + b"""

function_declare = """
func myfunc(a,b) {
  c = a + 1
  d = b + 2
  return c + d
}

myfunc(1, 2)
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

function_declare_with_if_return_else = """
func myfunc(a,b) {
  if (a + b) >= 2 {
    return 1
  } else {
    return 2
  }
}

myfunc(1, 0)
"""


def test_main():
  assert main("1 + 1") == "2"
  assert main("12 + 13") == "25"
  assert main("12 - 13") == "-1"
  assert main("(1 * 2) - 1") == "1"
  assert main("1 - (1 * 2)") == "-1"
  assert main("1 - (1 * 2) * (2 + 3)") == "-9"
  assert main(sum_variables) == "3"
  assert main(function_declare) == "6"
  assert main(function_declare_with_if) == "1"
  assert main(function_declare_with_if_return_else) == "2"
