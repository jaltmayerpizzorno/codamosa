# Automatically generated by Pynguin.
import codetiming._timers as module_0

def test_case_0():
    pass

def test_case_1():
    timers_0 = module_0.Timers()

def test_case_2():
    timers_0 = module_0.Timers()
    str_0 = 'minutes'
    float_0 = -2129.810056
    timers_0.add(str_0, float_0)

def test_case_3():
    str_0 = 'Unt test for method mean of classTimers'
    timers_0 = module_0.Timers()
    int_0 = 3
    timers_0.add(str_0, int_0)
    float_0 = timers_0.min(str_0)
    float_1 = timers_0.mean(str_0)
    float_2 = timers_0.median(str_0)
    float_3 = timers_0.stdev(str_0)
    float_4 = timers_0.total(str_0)
    float_5 = timers_0.stdev(str_0)
    var_0 = AssertionError(str_0)
    var_1 = timers_0

def test_case_4():
    timers_0 = module_0.Timers()
    str_0 = 'delay'
    float_0 = 1.0
    timers_0.add(str_0, float_0)
    float_1 = timers_0.mean(str_0)

def test_case_5():
    timers_0 = module_0.Timers()
    str_0 = 'Test'
    float_0 = 1.0
    timers_0.add(str_0, float_0)
    float_1 = timers_0.min(str_0)

def test_case_6():
    timers_0 = module_0.Timers()
    str_0 = 'test'
    float_0 = 1.0
    timers_0.add(str_0, float_0)
    timers_0.add(str_0, float_0)
    float_1 = timers_0.stdev(str_0)
    timers_0.add(str_0, float_1)
    float_2 = timers_0.stdev(str_0)

def test_case_7():
    timers_0 = module_0.Timers()
    str_0 = 'test'
    int_0 = 42
    timers_0.add(str_0, int_0)
    float_0 = timers_0.max(str_0)

def test_case_8():
    timers_0 = module_0.Timers()
    str_0 = 'test'
    int_0 = 10
    timers_0.add(str_0, int_0)
    float_0 = timers_0.median(str_0)

def test_case_9():
    timers_0 = module_0.Timers()
    str_0 = 'test'
    float_0 = 1.0
    timers_0.add(str_0, float_0)
    float_1 = 2.0
    float_2 = timers_0.stdev(str_0)
    timers_0.add(str_0, float_1)
    float_3 = timers_0.stdev(str_0)