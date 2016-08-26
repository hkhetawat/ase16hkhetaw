import utest

def fact(n):
    if n < 2:
        return n
    return n * fact(n-1)

@utest.ok
def passing_case_1():
    '''Pass Case for factorial 1'''
    assert fact(1) == 1

@utest.ok
def passing_case_5():
    '''Pass Case for factorial 5'''
    assert fact(5) == 120

@utest.ok
def failing_case_0():
    '''Fail Case for factorial 0'''
    assert fact(0) == 1
