# Automatically generated by Pynguin.
import ansible.playbook.conditional as module_0

def test_case_0():
    try:
        conditional_0 = module_0.Conditional()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 601
        conditional_0 = module_0.Conditional(int_0)
        var_0 = conditional_0.evaluate_conditional(conditional_0, int_0)
    except BaseException:
        pass