from main.basic_unit_tests import basic_unit_tests

# DESC
# Create a function that returns the name of the winner in a fight between two
# fighters. Each fighter takes turns attacking the other and whoever kills the
# other first is victorious. Death is defined as having health <= 0. Each
# fighter will be a Fighter object/instance. See the Fighter class below in your
# chosen language. Both health and damagePerAttack (damage_per_attack for
# python) will be integers larger than 0. You can mutate the Fighter objects.
# --------------- #


def declare_winner(fighter1, fighter2, first_attacker):
    attacks = 0
    if (fighter1.name == first_attacker):
        fighters = [fighter1, fighter2]
    else:
        fighters = [fighter2, fighter1]
    # (fighter1, fighter2)[fighter1.name == first_attacker]??
    while (fighters[0].health > 0 and attacks < 1000):
        # while break
        attacks += 1
        fighters[1].health -= fighters[0].damage_per_attack
        fighters.reverse()
    return fighters[1].name


class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(
        self.name, self.health, self.damage_per_attack)

    __repr__ = __str__


# --------------- #
# TEST
test = basic_unit_tests()
test.describe("Example test cases")
test.assert_equals(
    declare_winner(
        Fighter("Lew", 10, 2),
        Fighter("Harry", 5, 4), "Lew"),
    "Lew")
test.assert_equals(
    declare_winner(
        Fighter("Lew", 10, 2),
        Fighter("Harry", 5, 4), "Harry"),
    "Harry")
test.assert_equals(
    declare_winner(
        Fighter("Harald", 20, 5),
        Fighter("Harry", 5, 4),
        "Harry"),
    "Harald")
test.assert_equals(
    declare_winner(
        Fighter("Harald", 20, 5),
        Fighter("Harry", 5, 4), "Harald"),
    "Harald")
test.assert_equals(
    declare_winner(
        Fighter("Jerry", 30, 3),
        Fighter("Harald", 20, 5), "Jerry"),
    "Harald")
test.assert_equals(
    declare_winner(
        Fighter("Jerry", 30, 3),
        Fighter("Harald", 20, 5), "Harald"),
    "Harald")
