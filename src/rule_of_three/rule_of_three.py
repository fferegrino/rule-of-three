def rule_of_three(left_dividend, left_divisor, right_dividend):
    """"
    Calculates the value of 'x' in the following equation:

     left_dividend     right_dividend
    --------------- = ----------------
     left_divisor            x

    """
    return (right_dividend * left_divisor) / left_dividend
