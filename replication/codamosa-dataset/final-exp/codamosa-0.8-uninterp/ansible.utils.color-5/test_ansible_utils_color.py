# Automatically generated by Pynguin.
import ansible.utils.color as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'gray1'
    var_0 = module_0.parsecolor(str_0)

def test_case_2():
    bytes_0 = b'\x0fi\x14\x8d'
    var_0 = module_0.stringc(bytes_0, bytes_0)

def test_case_3():
    bool_0 = True
    bytes_0 = b'\x95\xd9\x1f\x96\xeed\x94U\xb5a\x8a\x18\xd0'
    var_0 = module_0.colorize(bool_0, bool_0, bytes_0)

def test_case_4():
    bool_0 = False
    set_0 = {bool_0, bool_0}
    var_0 = module_0.hostcolor(bool_0, set_0)

def test_case_5():
    str_0 = 'blue'
    var_0 = module_0.parsecolor(str_0)
    var_1 = module_0.parsecolor(str_0)
    bool_0 = True
    tuple_0 = ()
    var_2 = module_0.hostcolor(bool_0, tuple_0)
    str_1 = 'rgb123'
    var_3 = module_0.parsecolor(str_1)
    str_2 = 'gray8'
    var_4 = module_0.parsecolor(str_2)
    str_3 = 'string'
    float_0 = 1000.0
    set_0 = {var_2, str_3, float_0}
    bool_1 = False
    int_0 = None
    var_5 = module_0.colorize(set_0, bool_1, int_0)
    bytes_0 = None
    var_6 = module_0.stringc(bytes_0, bytes_0, float_0)

def test_case_6():
    str_0 = 'color1'
    var_0 = module_0.parsecolor(str_0)
    str_1 = 'rgb123'
    var_1 = module_0.parsecolor(str_1)
    str_2 = 'gray1'
    var_2 = module_0.parsecolor(str_2)

def test_case_7():
    str_0 = 'rgb123'
    var_0 = module_0.parsecolor(str_0)
    str_1 = 'gray1'
    var_1 = module_0.parsecolor(str_1)