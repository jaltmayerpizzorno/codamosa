# Automatically generated by Pynguin.
import ansible.playbook.conditional as module_0

def test_case_0():
    try:
        conditional_0 = module_0.Conditional()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x90\xad\xc0\xc4\xa4\xe8\xae\x94*\xc0\xd5\xc7'
        bool_0 = True
        conditional_0 = module_0.Conditional(bool_0)
        var_0 = conditional_0.extract_defined_undefined(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 20
        str_0 = '6uWx'
        conditional_0 = module_0.Conditional(str_0)
        var_0 = conditional_0.evaluate_conditional(int_0, int_0)
    except BaseException:
        pass