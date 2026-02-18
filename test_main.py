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

def test_main():
  assert main("1 + 1") == "2"
  assert main("12 + 13") == "25"
  assert main("12 - 13") == "-1"
  assert main("(1 * 2) - 1") == "1"
  assert main("1 - (1 * 2)") == "-1"
  assert main("1 - (1 * 2) * (2 + 3)") == "-9"
  assert main(sum_variables) == "3"
  assert main(function_declare) == "6"
