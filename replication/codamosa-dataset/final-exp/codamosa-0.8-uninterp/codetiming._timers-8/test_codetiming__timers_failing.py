# Automatically generated by Pynguin.
import codetiming._timers as module_0

def test_case_0():
    try:
        timers_0 = module_0.Timers()
        str_0 = 'a'
        int_0 = 1
        timers_0.add(str_0, int_0)
        int_1 = 2
        timers_0.add(str_0, int_1)
        int_2 = 3
        timers_0.add(str_0, int_2)
        float_0 = timers_0.stdev(str_0)
        str_1 = 'b'
        float_1 = timers_0.stdev(str_0)
        timers_0.clear()
        float_2 = timers_0.stdev(str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        timers_0 = module_0.Timers()
        float_0 = -1326.393914
        timers_0.__setitem__(str_0, float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = None
        timers_0 = module_0.Timers()
        float_0 = timers_0.median(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ')~'
        timers_0 = module_0.Timers()
        float_0 = timers_0.count(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        timers_0 = module_0.Timers()
        str_0 = '9bu~*{ZVW'
        float_0 = timers_0.min(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = " does not support item assignment. Use '.add()' to update values."
        timers_0 = module_0.Timers()
        float_0 = timers_0.max(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '$p'
        timers_0 = module_0.Timers()
        float_0 = timers_0.stdev(str_0)
    except BaseException:
        pass