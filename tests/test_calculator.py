from calculator.calc import add_ints

def test_add_ints():
  """
  test add function in main.py
  """
  assert add_ints(1, 2) == 3
  assert add_ints(2, 3) == 5
  assert add_ints(5, 5) != 5

  print("passed!")
