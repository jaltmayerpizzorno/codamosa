# Automatically generated by Pynguin.
import ansible.playbook.conditional as module_0

def test_case_0():
    try:
        conditional_0 = module_0.Conditional()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b"4Yk\x16d\xd8'\x14\xc7=\xad\xfb\xd2"
        conditional_0 = module_0.Conditional(bytes_0)
        dict_0 = {bytes_0: bytes_0}
        var_0 = conditional_0.evaluate_conditional(conditional_0, dict_0)
    except BaseException:
        pass