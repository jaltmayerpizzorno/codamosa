# Automatically generated by Pynguin.
import ansible.module_utils.facts.compat as module_0

def test_case_0():
    try:
        float_0 = 1964.621
        var_0 = module_0.get_all_facts(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x82\xa5/F\xed\xf7\xd5\xe8Q\xa4]A\xf2\x99\xd9'
        var_0 = module_0.ansible_facts(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "(^#f_@Y'3K+8"
        list_0 = [str_0, str_0]
        var_0 = module_0.ansible_facts(str_0, list_0)
    except BaseException:
        pass