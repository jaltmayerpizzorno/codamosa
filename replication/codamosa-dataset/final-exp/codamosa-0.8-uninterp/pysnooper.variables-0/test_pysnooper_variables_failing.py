# Automatically generated by Pynguin.
import pysnooper.variables as module_0

def test_case_0():
    try:
        str_0 = '^wCT}cFQBz*#;'
        indices_0 = module_0.Indices(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'path'
        indices_0 = module_0.Indices(str_0)
        bytes_0 = b'\xec\x8a_\xbce^F\x90\xaa\xbf\xa1\x8fF2O'
        var_0 = indices_0.__getitem__(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '{}.x'
        attrs_0 = module_0.Attrs(str_0)
        var_0 = attrs_0.__eq__(attrs_0)
        bool_0 = True
        var_1 = attrs_0.__eq__(bool_0)
        bool_1 = None
        var_2 = attrs_0.items(bool_1)
        float_0 = -1517.8663
        base_variable_0 = module_0.BaseVariable(float_0)
    except BaseException:
        pass