# Automatically generated by Pynguin.
import ansible.playbook.conditional as module_0

def test_case_0():
    try:
        conditional_0 = module_0.Conditional()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        float_0 = 1080.1
        conditional_0 = module_0.Conditional(float_0)
        var_0 = conditional_0.extract_defined_undefined(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        int_0 = -2828
        conditional_0 = module_0.Conditional(int_0)
        var_0 = conditional_0.evaluate_conditional(bool_0, bool_0)
    except BaseException:
        pass