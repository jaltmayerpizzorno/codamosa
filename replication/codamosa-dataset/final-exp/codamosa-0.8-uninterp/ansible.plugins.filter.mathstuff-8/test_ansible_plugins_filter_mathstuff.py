# Automatically generated by Pynguin.
import ansible.plugins.filter.mathstuff as module_0

def test_case_0():
    filter_module_0 = module_0.FilterModule()

def test_case_1():
    float_0 = 1005.0
    list_0 = []
    var_0 = module_0.difference(float_0, list_0, float_0)

def test_case_2():
    int_0 = -1233
    set_0 = {int_0, int_0, int_0}
    var_0 = module_0.intersect(int_0, set_0, set_0)

def test_case_3():
    int_0 = 100
    var_0 = module_0.logarithm(int_0, int_0)

def test_case_4():
    filter_module_0 = module_0.FilterModule()
    var_0 = filter_module_0.filters()

def test_case_5():
    int_0 = 2340
    tuple_0 = ()
    tuple_1 = (tuple_0,)
    set_0 = set()
    var_0 = module_0.difference(int_0, tuple_1, set_0)

def test_case_6():
    bytes_0 = b'\xfc\xa8@eB,\x1b'
    list_0 = [bytes_0]
    dict_0 = {}
    var_0 = module_0.rekey_on_member(dict_0, list_0)

def test_case_7():
    str_0 = 't8C^|\x0c2EMk\x0c}Y`f\\FD\x0c?'
    dict_0 = {str_0: str_0}
    tuple_0 = (dict_0,)
    var_0 = module_0.rekey_on_member(tuple_0, str_0)

def test_case_8():
    int_0 = 10
    var_0 = module_0.logarithm(int_0, int_0)