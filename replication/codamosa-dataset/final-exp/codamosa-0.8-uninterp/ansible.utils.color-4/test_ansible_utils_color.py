# Automatically generated by Pynguin.
import ansible.utils.color as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    var_0 = module_0.stringc(list_0, list_0)

def test_case_2():
    float_0 = -1646.75933
    tuple_0 = (float_0,)
    var_0 = module_0.colorize(float_0, float_0, tuple_0)

def test_case_3():
    str_0 = 'g@Bnz\td@lP>Dt\ne'
    var_0 = module_0.hostcolor(str_0, str_0)

def test_case_4():
    str_0 = 'x:2+YMY@QS=-\\Q30/v{g'
    bytes_0 = b'\xfc&\x9av2\xa0U\x86\xb7\x01*\xab\xfa\xaa,'
    bytes_1 = b'\x10(\x9cmcA\xbb~\xe4\xea\x0b\xfc\xb9\\\x9a'
    var_0 = module_0.hostcolor(bytes_0, bytes_1, bytes_0)
    int_0 = -1143
    bytes_2 = b'\xed\x8f\xd8\xb4\xb5%'
    tuple_0 = ()
    var_1 = module_0.colorize(bytes_2, tuple_0, tuple_0)
    bool_0 = False
    str_1 = '%s %-9s # %s'
    var_2 = module_0.colorize(tuple_0, bool_0, str_1)
    var_3 = module_0.stringc(str_0, int_0)

def test_case_5():
    str_0 = 'rgb000'
    var_0 = module_0.parsecolor(str_0)

def test_case_6():
    str_0 = 'gray0'
    var_0 = module_0.parsecolor(str_0)

def test_case_7():
    str_0 = 'color16'
    var_0 = module_0.parsecolor(str_0)
    str_1 = 'gray0'
    var_1 = module_0.parsecolor(str_1)
    var_2 = module_0.parsecolor(str_0)
    var_3 = module_0.parsecolor(str_0)