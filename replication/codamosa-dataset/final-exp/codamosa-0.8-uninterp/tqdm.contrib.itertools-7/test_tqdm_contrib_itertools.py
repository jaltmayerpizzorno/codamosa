# Automatically generated by Pynguin.
import tqdm.contrib.itertools as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 10
    var_0 = range(int_0)
    int_1 = 1
    var_1 = range(int_1, int_0)
    int_2 = 2
    var_2 = range(int_2, int_0)
    int_3 = 3
    var_3 = range(int_3, int_0)
    var_4 = (var_0, var_1, var_2, var_3)
    var_5 = module_0.product(*var_4)
    var_6 = list(var_5)
    var_7 = module_0.product(*var_4)
    var_8 = list(var_7)
    var_9 = module_0.product(*var_4)
    var_10 = list(var_9)