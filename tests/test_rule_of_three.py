from rule_of_three.rule_of_three import rule_of_three

def test_rule_of_three():
    a = 1
    b = 2
    c = 3

    expected_x = 6

    actual_x = rule_of_three(a, b, c)

    assert expected_x == actual_x
