# Automatically generated by Pynguin.
import ansible.plugins.become.su as module_0

def test_case_0():
    try:
        int_0 = -1189
        become_module_0 = module_0.BecomeModule()
        var_0 = become_module_0.check_password_prompt(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 470
        set_0 = {int_0}
        become_module_0 = module_0.BecomeModule()
        var_0 = become_module_0.build_become_command(int_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = None
        become_module_0 = module_0.BecomeModule()
        var_0 = become_module_0.build_become_command(list_0, become_module_0)
        var_1 = become_module_0.build_become_command(become_module_0, list_0)
    except BaseException:
        pass