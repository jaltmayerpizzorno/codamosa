# Automatically generated by Pynguin.
import codetiming._timers as module_0

def test_case_0():
    timers_0 = module_0.Timers()

def test_case_1():
    str_0 = "S'/n"
    timers_0 = module_0.Timers()
    float_0 = -30.0
    timers_0.add(str_0, float_0)
    float_1 = timers_0.median(str_0)

def test_case_2():
    timers_0 = module_0.Timers()
    timers_0.clear()

def test_case_3():
    list_0 = []
    timers_0 = module_0.Timers(*list_0)
    str_0 = '4\tp'
    float_0 = 73.0
    timers_0.add(str_0, float_0)
    float_1 = timers_0.mean(str_0)
    float_2 = timers_0.stdev(str_0)
    float_3 = timers_0.total(str_0)
    float_4 = timers_0.median(str_0)
    float_5 = timers_0.max(str_0)
    timers_0.clear()

def test_case_4():
    str_0 = "PC(/m_rhJKwP3Zm'"
    timers_0 = module_0.Timers()
    float_0 = -671.772762
    timers_0.add(str_0, float_0)
    float_1 = timers_0.min(str_0)

def test_case_5():
    str_0 = 'L{M4T)>z,AL;H'
    timers_0 = module_0.Timers()
    float_0 = 771.123
    timers_0.add(str_0, float_0)
    float_1 = timers_0.max(str_0)

def test_case_6():
    str_0 = " does not support item assignment. Use '.add()' to update values."
    timers_0 = module_0.Timers()
    float_0 = -1424.851614
    timers_0.add(str_0, float_0)
    float_1 = timers_0.mean(str_0)

def test_case_7():
    list_0 = []
    timers_0 = module_0.Timers(*list_0)
    str_0 = ';4J~YA<(\\'
    float_0 = 1294.348
    timers_0.add(str_0, float_0)
    float_1 = timers_0.stdev(str_0)
    float_2 = timers_0.min(str_0)

def test_case_8():
    list_0 = []
    timers_0 = module_0.Timers(*list_0)
    str_0 = '4\tp'
    float_0 = 73.2018
    timers_0.add(str_0, float_0)
    float_1 = 465.06
    timers_0.add(str_0, float_1)
    float_2 = timers_0.mean(str_0)
    float_3 = timers_0.stdev(str_0)
    float_4 = timers_0.min(str_0)
    float_5 = timers_0.total(str_0)
    float_6 = timers_0.median(str_0)
    float_7 = timers_0.max(str_0)
    timers_1 = module_0.Timers()
    float_8 = timers_0.max(str_0)
    timers_2 = module_0.Timers()