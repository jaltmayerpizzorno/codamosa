# Automatically generated by Pynguin.
import pytutils.path as module_0

def test_case_0():
    int_0 = 679
    bool_0 = None
    var_0 = module_0.join_each(int_0, bool_0)

def test_case_1():
    str_0 = '/home'
    str_1 = 'local'
    str_2 = 'user'
    str_3 = [str_1, str_2]
    var_0 = module_0.join_each(str_0, str_3)
    var_1 = list(var_0)