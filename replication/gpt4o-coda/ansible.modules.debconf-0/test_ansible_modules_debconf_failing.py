# Automatically generated by Pynguin.
import ansible.modules.debconf as module_0

def test_case_0():
    try:
        tuple_0 = ()
        var_0 = module_0.get_selections(tuple_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 2206.823
        float_1 = None
        bool_0 = False
        float_2 = 112.3
        bytes_0 = b'(2j\\\x19<?&\xf9K\xca\x9c\xce\x16E&\xbb\xa1'
        set_0 = {float_1, float_2, bool_0, bytes_0}
        dict_0 = {bytes_0: bool_0}
        var_0 = module_0.set_selection(float_0, float_1, bool_0, float_2, set_0, dict_0)
    except BaseException:
        pass