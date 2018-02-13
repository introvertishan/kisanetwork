# This generates a random six digit number as OTP.

from random import randint

def generate_random_six(function):
    def wrap_function(*args, **kwargs):
        str = 'Working!'
        range_start = 10 ** (5)
        range_end = (10 ** 6) - 1
        ran_num = randint(range_start, range_end)
        return function(ran_num,*args, **kwargs)
    return wrap_function

