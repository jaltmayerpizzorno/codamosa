# Automatically generated by Pynguin.
import ansible.module_utils.facts.compat as module_0

def test_case_0():
    try:
        int_0 = -2405
        var_0 = module_0.get_all_facts(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -422
        var_0 = module_0.ansible_facts(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xf0\xc2\xb7\xcb\x8e\xb6'
        str_0 = 'failed_when_result'
        var_0 = module_0.ansible_facts(bytes_0, str_0)
    except BaseException:
        pass