# Automatically generated by Pynguin.
import tqdm.contrib.itertools as module_0

def test_case_0():
    try:
        int_0 = 10
        int_1 = [int_0, int_0, int_0, int_0]
        var_0 = module_0.product(*int_1)
        var_1 = list(var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 10
        int_1 = [int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0]
        var_0 = module_0.product(*int_1)
        var_1 = list(var_0)
    except BaseException:
        pass