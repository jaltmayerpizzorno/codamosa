# Automatically generated by Pynguin.
import sty.primitive as module_0

def test_case_0():
    pass

def test_case_1():
    style_0 = module_0.Style()

def test_case_2():
    int_0 = -906
    int_1 = None
    list_0 = [int_0, int_1]
    register_0 = module_0.Register()
    register_1 = register_0.copy()
    str_0 = register_1.__call__(*list_0)
    str_1 = ''
    style_0 = module_0.Style()
    register_2 = module_0.Register()
    var_0 = register_2.__setattr__(str_1, style_0)

def test_case_3():
    register_0 = module_0.Register()

def test_case_4():
    bytes_0 = b'l\x1c\xa3\x84!\xf6\xd5'
    callable_0 = None
    register_0 = module_0.Register()
    register_0.set_renderfunc(bytes_0, callable_0)

def test_case_5():
    register_0 = module_0.Register()
    register_0.mute()

def test_case_6():
    register_0 = module_0.Register()
    register_1 = register_0.copy()
    var_0 = register_0.as_namedtuple()
    register_0.unmute()
    register_0.mute()
    float_0 = 2078.414
    tuple_0 = (float_0,)
    str_0 = register_0.__call__()
    register_2 = module_0.Register()
    register_2.set_renderfunc(tuple_0, tuple_0)

def test_case_7():
    register_0 = module_0.Register()
    register_1 = register_0.copy()
    register_1.mute()
    register_1.mute()
    register_2 = register_1.copy()
    register_3 = module_0.Register()