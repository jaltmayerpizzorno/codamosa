# Automatically generated by Pynguin.
import ansible.playbook.conditional as module_0

def test_case_0():
    try:
        conditional_0 = module_0.Conditional()
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = None
        float_0 = 827.6
        tuple_0 = (float_0,)
        conditional_0 = module_0.Conditional(tuple_0)
        var_0 = conditional_0.evaluate_conditional(set_0, float_0)
    except BaseException:
        pass