# Automatically generated by Pynguin.
import ansible.module_utils.common.text.formatters as module_0

def test_case_0():
    try:
        dict_0 = None
        var_0 = module_0.human_to_bytes(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 1687
        str_0 = "~p\x0bM9F^Lkmvpb'C=-"
        var_0 = module_0.human_to_bytes(int_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 1442
        str_0 = "G'Jn6m\r]4xaSI"
        var_0 = module_0.human_to_bytes(int_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 427
        var_0 = module_0.human_to_bytes(int_0)
        int_1 = 1330
        bool_0 = False
        str_0 = 'K'
        var_1 = module_0.bytes_to_human(int_1, bool_0, str_0)
        str_1 = 'K'
        var_2 = module_0.human_to_bytes(int_0, str_1)
        float_0 = -1625.0
        tuple_0 = (float_0,)
        dict_0 = {tuple_0: float_0, float_0: var_0}
        var_3 = module_0.lenient_lowercase(dict_0)
        var_4 = module_0.bytes_to_human(int_0)
        var_5 = module_0.human_to_bytes(tuple_0, var_3, tuple_0)
    except BaseException:
        pass