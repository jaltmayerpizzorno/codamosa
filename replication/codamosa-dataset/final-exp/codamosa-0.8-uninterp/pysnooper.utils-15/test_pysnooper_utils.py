# Automatically generated by Pynguin.
import pysnooper.utils as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    var_0 = module_0.shitcode(list_0)

def test_case_2():
    float_0 = -755.9
    var_0 = module_0.get_shortish_repr(float_0)

def test_case_3():
    str_0 = '\x0c9!)1\\hJm"K?\t'
    bool_0 = True
    var_0 = module_0.truncate(str_0, bool_0)

def test_case_4():
    bool_0 = False
    set_0 = {bool_0}
    var_0 = module_0.ensure_tuple(set_0)

def test_case_5():
    bytes_0 = b'\xec\xf99\xb1\xfey2\xdd\x1f\xda\xb5\x95\n'
    var_0 = module_0.get_shortish_repr(bytes_0)
    str_0 = 'J\nq#28sCP:Rp'
    var_1 = module_0.ensure_tuple(str_0)

def test_case_6():
    str_0 = 'zD]-:-]q\n'
    var_0 = module_0.shitcode(str_0)
    bool_0 = None
    var_1 = module_0.get_shortish_repr(str_0)
    bytes_0 = b'\x15\x1f \x87\xbf\x98\xcdn\x11\xe4\xf6'
    var_2 = module_0.truncate(bytes_0, bool_0)

def test_case_7():
    str_0 = '4m}[$>so\x0c!\tB'
    var_0 = module_0.shitcode(str_0)

def test_case_8():
    str_0 = 'і'
    var_0 = module_0.shitcode(str_0)

def test_case_9():
    str_0 = ' is an int'
    var_0 = lambda x: str(x) + str_0
    str_1 = ' is a str'
    var_1 = lambda x: str(x) + str_1
    str_2 = 'ey)s'
    var_2 = lambda x: str(x) + str_0
    var_3 = lambda x: str(x) + var_0
    var_4 = None
    var_5 = type(var_4)
    var_6 = lambda x: str(x)
    var_7 = (var_5, var_6)
    var_8 = [var_7]
    var_9 = module_0.get_repr_function(str_2, var_8)

def test_case_10():
    str_0 = 'abc'
    var_0 = module_0.shitcode(str_0)
    str_1 = 'abc\x00\x01\x02\x03'
    var_1 = module_0.shitcode(str_1)
    str_2 = '\x00\x01\x02'
    var_2 = module_0.shitcode(str_2)