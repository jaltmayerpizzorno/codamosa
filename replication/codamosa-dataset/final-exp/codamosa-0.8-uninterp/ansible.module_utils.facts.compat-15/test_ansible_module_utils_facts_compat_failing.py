# Automatically generated by Pynguin.
import ansible.module_utils.facts.compat as module_0

def test_case_0():
    try:
        set_0 = set()
        var_0 = module_0.get_all_facts(set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b"\x06\xa5'\xb2?\xa62"
        var_0 = module_0.ansible_facts(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = None
        list_0 = [float_0]
        set_0 = None
        float_1 = 1620.846007
        tuple_0 = (float_0, set_0, float_1)
        var_0 = module_0.ansible_facts(list_0, tuple_0)
    except BaseException:
        pass