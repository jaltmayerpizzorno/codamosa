# Automatically generated by Pynguin.
import ansible.modules.debconf as module_0

def test_case_0():
    try:
        int_0 = 128
        var_0 = module_0.get_selections(int_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\x0cC'
        bool_0 = False
        complex_0 = None
        list_0 = []
        float_0 = 2066.469
        var_0 = module_0.set_selection(str_0, bool_0, complex_0, list_0, list_0, float_0)
    except BaseException:
        pass