# Automatically generated by Pynguin.
import codetiming._timers as module_0

def test_case_0():
    try:
        timers_0 = module_0.Timers()
        str_0 = 'iter'
        float_0 = 0.1
        timers_0.add(str_0, float_0)
        float_1 = 0.2
        str_1 = 'Timer is not running. Use .start() to start it'
        float_2 = timers_0.min(str_0)
        float_3 = timers_0.max(str_0)
        float_4 = timers_0.median(str_0)
        timers_0.clear()
        timers_0.add(str_0, float_4)
        float_5 = timers_0.mean(str_0)
        timers_0.__setitem__(str_1, float_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'W2!qQEvP9Y*lGCVQ'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        timers_0 = module_0.Timers(**dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\rfy$*1>eoC'
        timers_0 = module_0.Timers()
        float_0 = timers_0.count(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'i{lisecon8s'
        float_0 = 620.0
        timers_0 = module_0.Timers()
        timers_0.add(str_0, float_0)
        float_1 = -706.4413
        float_2 = timers_0.total(str_0)
        list_0 = []
        float_3 = timers_0.stdev(str_0)
        timers_1 = module_0.Timers(*list_0)
        str_1 = 'NS<b.,:"m'
        dict_0 = {}
        timers_2 = module_0.Timers(*list_0, **dict_0)
        timers_2.add(str_0, float_1)
        float_4 = timers_1.median(str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = None
        timers_0 = module_0.Timers()
        float_0 = timers_0.stdev(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '+*?X$H2$X?$"'
        timers_0 = module_0.Timers()
        float_0 = timers_0.mean(str_0)
    except BaseException:
        pass