# Automatically generated by Pynguin.
import ansible.utils.py3compat as module_0

def test_case_0():
    pass

def test_case_1():
    text_environ_0 = module_0._TextEnviron()

def test_case_2():
    str_0 = 'ke?1'
    str_1 = {str_0: str_0}
    text_environ_0 = module_0._TextEnviron(str_1, str_1)
    var_0 = text_environ_0[str_0]

def test_case_3():
    float_0 = 40.913447
    tuple_0 = (float_0,)
    int_0 = None
    tuple_1 = (tuple_0, int_0)
    text_environ_0 = module_0._TextEnviron(tuple_1)
    var_0 = text_environ_0.__len__()