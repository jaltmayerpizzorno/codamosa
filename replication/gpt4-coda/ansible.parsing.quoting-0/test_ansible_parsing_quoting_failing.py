# Automatically generated by Pynguin.
import ansible.parsing.quoting as module_0

def test_case_0():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0, bool_0]
        var_0 = module_0.unquote(list_0)
        var_1 = module_0.unquote(list_0)
        var_2 = module_0.is_quoted(list_0)
        float_0 = -1825.52
        var_3 = module_0.unquote(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -3046
        set_0 = {int_0, int_0, int_0}
        var_0 = module_0.is_quoted(set_0)
        var_1 = module_0.unquote(int_0)
    except BaseException:
        pass