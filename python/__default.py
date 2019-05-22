from main.basic_unit_tests import basic_unit_tests
test = basic_unit_tests()

# DESC
# Make a function that adds two numbers
# --------------- #


def add(n1, n2):
    return n1+n2


# --------------- #
# TEST
test.describe("Addition")
test.assert_equals(add(2, 2), 4)
