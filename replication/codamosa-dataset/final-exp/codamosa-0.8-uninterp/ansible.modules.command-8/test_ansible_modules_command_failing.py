# Automatically generated by Pynguin.
import ansible.modules.command as module_0

def test_case_0():
    try:
        float_0 = 1.0
        var_0 = module_0.check_command(float_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 32603
        tuple_0 = (int_0,)
        list_0 = []
        var_0 = module_0.check_command(tuple_0, list_0)
    except BaseException:
        pass