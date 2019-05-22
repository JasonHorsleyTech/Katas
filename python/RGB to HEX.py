from main.basic_unit_tests import basic_unit_tests

# DESC
# Make a function that adds two numbers
# --------------- #


def rgb(r, g, b):
    # output_hex: returned value
    # channel_hex: python value (missing characters sometimes)
    # pretty_hex: Always the 2 len str
    o_hex = ''
    for c in [r, g, b]:
        # Trap for out of range
        c_hex = hex(min(max(c, 0), 255))
        # hex() returns 0xFF OR 0x0, so auto fill the other char
        if (len(c_hex) > 3):
            p_hex = c_hex[2:4]
        else:
            p_hex = '0' + c_hex[2]
        o_hex += p_hex
    return o_hex.upper()


# --------------- #
# TEST
test = basic_unit_tests()
test.describe("Addition")
test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")
