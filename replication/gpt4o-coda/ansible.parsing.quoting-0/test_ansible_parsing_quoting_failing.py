# Automatically generated by Pynguin.
import ansible.parsing.quoting as module_0

def test_case_0():
    try:
        int_0 = -2054
        var_0 = module_0.is_quoted(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        var_0 = module_0.unquote(bool_0)
    except BaseException:
        pass