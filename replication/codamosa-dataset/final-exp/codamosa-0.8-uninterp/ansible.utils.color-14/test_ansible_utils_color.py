# Automatically generated by Pynguin.
import ansible.utils.color as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'rgb0255255'
    var_0 = module_0.parsecolor(str_0)

def test_case_2():
    bool_0 = False
    str_0 = 'Wj?8$lr(ky'
    var_0 = module_0.stringc(bool_0, str_0)

def test_case_3():
    dict_0 = None
    bytes_0 = b'\xc0\x8e\xfc'
    var_0 = module_0.colorize(dict_0, bytes_0, bytes_0)

def test_case_4():
    float_0 = 512.0
    var_0 = module_0.hostcolor(float_0, float_0)

def test_case_5():
    str_0 = 'blue'
    str_1 = 'rgb512'
    var_0 = module_0.parsecolor(str_1)
    str_2 = 'gray1'
    var_1 = module_0.parsecolor(str_2)
    str_3 = 'color8'
    var_2 = module_0.parsecolor(str_3)
    var_3 = module_0.parsecolor(str_0)