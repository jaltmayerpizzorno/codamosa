# Automatically generated by Pynguin.
import ansible.playbook.conditional as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\xa6\x910f-\xfb'
    conditional_0 = module_0.Conditional(bytes_0)

def test_case_2():
    str_0 = 'foo is not undefined'
    conditional_0 = module_0.Conditional(str_0)
    var_0 = conditional_0.extract_defined_undefined(str_0)

def test_case_3():
    str_0 = '--no-wait'
    float_0 = -1204.5
    conditional_0 = module_0.Conditional(float_0)
    var_0 = conditional_0.extract_defined_undefined(str_0)