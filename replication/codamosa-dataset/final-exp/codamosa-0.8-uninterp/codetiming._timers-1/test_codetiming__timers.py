# Automatically generated by Pynguin.
import codetiming._timers as module_0

def test_case_0():
    pass

def test_case_1():
    timers_0 = module_0.Timers()

def test_case_2():
    timers_0 = module_0.Timers()
    str_0 = 'Q4O\tb&uSf'
    float_0 = 558.8154989325044
    timers_0.add(str_0, float_0)
    float_1 = timers_0.stdev(str_0)

def test_case_3():
    timers_0 = module_0.Timers()
    timers_0.clear()

def test_case_4():
    timers_0 = module_0.Timers()
    str_0 = 'a'
    int_0 = 2
    timers_0.add(str_0, int_0)
    float_0 = timers_0.mean(str_0)

def test_case_5():
    timers_0 = module_0.Timers()
    str_0 = 'Q4O\tb&uSf'
    float_0 = 550.48848
    timers_0.add(str_0, float_0)
    float_1 = timers_0.stdev(str_0)
    float_2 = timers_0.count(str_0)

def test_case_6():
    timers_0 = module_0.Timers()
    str_0 = 'fps'
    int_0 = 50
    timers_0.add(str_0, int_0)
    float_0 = timers_0.median(str_0)

def test_case_7():
    timers_0 = module_0.Timers()
    str_0 = 'test_min_func'
    int_0 = 1
    timers_0.add(str_0, int_0)
    float_0 = timers_0.min(str_0)

def test_case_8():
    timers_0 = module_0.Timers()
    str_0 = 'a'
    int_0 = 1
    timers_0.add(str_0, int_0)
    float_0 = timers_0.max(str_0)