# Automatically generated by Pynguin.
import ansible.plugins.become.su as module_0

def test_case_0():
    try:
        int_0 = 594
        become_module_0 = module_0.BecomeModule()
        var_0 = become_module_0.check_password_prompt(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = set()
        become_module_0 = module_0.BecomeModule()
        var_0 = become_module_0.build_become_command(set_0, set_0)
        var_1 = become_module_0.build_become_command(become_module_0, become_module_0)
    except BaseException:
        pass