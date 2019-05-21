from main.basic_unit_tests import basic_unit_tests

# DESC
# Write a function that will return the count of distinct case-insensitive
# alphabetic characters and numeric digits that occur more than once in the
# input string. The input string can be assumed to contain only alphabets (both
# uppercase and lowercase) and numeric digits.
# --------------- #


def duplicate_count(text):
    letters = list(str(text).lower())
    used = {}
    # I COULD make a single variable to count duplicates, and only increment
    # when a used[letter] == 2. But the function would be more rigid, and "make
    # it count the number of triplets" would require a rewrite. So I'll use a
    # few more steps for the sake of reusability, and leave golf for >5pm
    for letter in letters:
        at = used[letter] if letter in used else 0
        used[letter] = at + 1

    # used is now each letter by usage count.
    # "aabbc" >> {'a': 2, 'b': 2, 'c': 1}
    duples = 0
    for key, count in used.items():
        if count >= 2:
            duples += 1
    return duples



# --------------- #
# TEST
test = basic_unit_tests()
test.assert_equals(duplicate_count("abcde"), 0)
test.assert_equals(duplicate_count("abcdea"), 1)
test.assert_equals(duplicate_count("indivisibility"), 1)
test.assert_equals(duplicate_count("aabBcde"), 2)
test.assert_equals(duplicate_count("aA11"), 2)
test.assert_equals(duplicate_count("ABBA"), 2)
