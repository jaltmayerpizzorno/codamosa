# Automatically generated by Pynguin.
import ansible.module_utils.facts.compat as module_0

def test_case_0():
    try:
        str_0 = '\ni{tzrA-\x0bW!`BGvmP9{&'
        var_0 = module_0.get_all_facts(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 297
        var_0 = module_0.ansible_facts(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xd4\xe7\xcb\xeb>\x1c\xfa[)\xcb\xa8\x0c\x9829'
        str_0 = '1D]C(4+m$&aZgB'
        var_0 = module_0.ansible_facts(bytes_0, str_0)
    except BaseException:
        pass