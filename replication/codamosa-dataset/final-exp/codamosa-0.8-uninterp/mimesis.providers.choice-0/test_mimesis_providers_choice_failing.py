# Automatically generated by Pynguin.
import mimesis.providers.choice as module_0

def test_case_0():
    try:
        choice_0 = module_0.Choice()
        bytes_0 = b'\xd4_\xf3f\xc6\xbc\xd3/\xf8\x04\xcfI\xde\xc9CU\t'
        bool_0 = True
        var_0 = choice_0.__call__(bytes_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        choice_0 = module_0.Choice()
        var_0 = choice_0.__call__(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\x1eL\x0b\xd4\x01\xa1\xfcZ7\xa4\xb6\x87\x81\x15\xd5\x7f\x1e\xd5'
        choice_0 = module_0.Choice()
        var_0 = choice_0.__call__(bytes_0)
        bytes_1 = None
        list_0 = [bytes_1]
        choice_1 = module_0.Choice(*list_0)
        float_0 = None
        dict_0 = {choice_0: float_0}
        int_0 = None
        var_1 = choice_1.__call__(dict_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        int_0 = 504
        bool_0 = False
        choice_0 = module_0.Choice()
        var_0 = choice_0.__call__(list_0, int_0, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        choice_0 = module_0.Choice()
        int_0 = -1753
        bytes_0 = b'\xb56\xc6\xac\xbe_\xe0'
        var_0 = choice_0.__call__(bytes_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        choice_0 = module_0.Choice()
        str_0 = 'a'
        str_1 = 'b'
        str_2 = (str_0, str_1, str_0, str_0, str_1)
        int_0 = 6
        var_0 = choice_0.__call__(str_2, int_0)
        var_1 = print(var_0)
        str_3 = 'abc'
        bool_0 = True
        var_2 = choice_0.__call__(str_3, int_0, bool_0)
    except BaseException:
        pass