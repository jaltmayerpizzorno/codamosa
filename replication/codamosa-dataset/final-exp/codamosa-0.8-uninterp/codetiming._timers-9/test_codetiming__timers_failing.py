# Automatically generated by Pynguin.
import codetiming._timers as module_0

def test_case_0():
    try:
        str_0 = '9p'
        float_0 = -2035.46
        timers_0 = module_0.Timers()
        timers_0.__setitem__(str_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'AZT/p)s&bN 2+Y/x'
        timers_0 = module_0.Timers()
        float_0 = timers_0.mean(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = None
        timers_0 = module_0.Timers()
        float_0 = timers_0.count(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = None
        str_1 = '{[F$+h'
        list_0 = [str_0]
        timers_0 = module_0.Timers(*list_0)
        float_0 = timers_0.total(str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'AZT/p)m_#bN 2+Y/x'
        timers_0 = module_0.Timers()
        float_0 = timers_0.stdev(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        timers_0 = module_0.Timers()
        str_0 = None
        float_0 = -731.74
        timers_0.add(str_0, float_0)
        float_1 = timers_0.count(str_0)
        float_2 = timers_0.median(str_0)
        float_3 = timers_0.min(str_0)
        float_4 = 1861.22661
        timers_0.add(str_0, float_4)
        float_5 = timers_0.max(str_0)
        float_6 = timers_0.stdev(str_0)
        float_7 = timers_0.max(str_0)
        str_1 = '{:bJoGU'
        float_8 = timers_0.mean(str_0)
        timers_0.clear()
        float_9 = timers_0.mean(str_1)
    except BaseException:
        pass