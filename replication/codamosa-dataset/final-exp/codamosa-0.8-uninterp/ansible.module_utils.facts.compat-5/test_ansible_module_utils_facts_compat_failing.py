# Automatically generated by Pynguin.
import ansible.module_utils.facts.compat as module_0

def test_case_0():
    try:
        str_0 = "'`("
        var_0 = module_0.get_all_facts(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 3199
        var_0 = module_0.ansible_facts(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = None
        dict_0 = {float_0: float_0}
        var_0 = module_0.ansible_facts(float_0, dict_0)
    except BaseException:
        pass