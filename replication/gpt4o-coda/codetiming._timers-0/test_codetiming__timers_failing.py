# Automatically generated by Pynguin.
import codetiming._timers as module_0

def test_case_0():
    try:
        str_0 = 'M9\rBD=-Jc*I'
        float_0 = -2661.0
        timers_0 = module_0.Timers()
        timers_0.__setitem__(str_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "S'/n"
        timers_0 = module_0.Timers()
        float_0 = timers_0.median(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '>I(`/$5]*4\x0c:GF'
        str_1 = 'u?0Ie{*HGi'
        float_0 = 1784.8758
        timers_0 = module_0.Timers()
        timers_0.add(str_1, float_0)
        timers_1 = module_0.Timers()
        float_1 = timers_1.count(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'Elapsed time: {:0.4f} seconds'
        timers_0 = module_0.Timers()
        float_0 = timers_0.stdev(str_0)
    except BaseException:
        pass