# Automatically generated by Pynguin.
import pysnooper.variables as module_0

def test_case_0():
    try:
        str_0 = 'g\n'
        exploding_0 = module_0.Exploding(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        attrs_0 = module_0.Attrs(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'var'
        indices_0 = module_0.Indices(str_0)
        var_0 = indices_0[:]
        var_1 = indices_0.__getitem__(str_0)
    except BaseException:
        pass