# Automatically generated by Pynguin.
import codetiming._timers as module_0

def test_case_0():
    timers_0 = module_0.Timers()

def test_case_1():
    timers_0 = module_0.Timers()
    str_0 = 'timers'
    float_0 = -1197.5978
    timers_0.add(str_0, float_0)
    float_1 = timers_0.mean(str_0)
    float_2 = timers_0.stdev(str_0)

def test_case_2():
    str_0 = 'Test the median method of class Timers'
    timers_0 = module_0.Timers()
    float_0 = 3.0
    timers_0.add(str_0, float_0)
    float_1 = timers_0.median(str_0)

def test_case_3():
    timers_0 = module_0.Timers()
    str_0 = 'time(rs'
    float_0 = -1219.6104010169051
    timers_0.add(str_0, float_0)
    float_1 = timers_0.max(str_0)

def test_case_4():
    timers_0 = module_0.Timers()
    str_0 = 'timers'
    float_0 = 15.581597513656334
    timers_0.add(str_0, float_0)
    float_1 = timers_0.min(str_0)

def test_case_5():
    timers_0 = module_0.Timers()
    str_0 = 'timers'
    float_0 = -1219.9350142897226
    timers_0.add(str_0, float_0)
    float_1 = timers_0.mean(str_0)

def test_case_6():
    timers_0 = module_0.Timers()
    timers_0.clear()
    str_0 = '"\r&\t\tK5~NU'
    float_0 = 977.49826
    timers_0.add(str_0, float_0)
    float_1 = 1776.551
    timers_0.add(str_0, float_1)
    float_2 = timers_0.max(str_0)
    float_3 = timers_0.stdev(str_0)