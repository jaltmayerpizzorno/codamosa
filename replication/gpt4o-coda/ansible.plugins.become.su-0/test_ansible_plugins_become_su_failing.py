# Automatically generated by Pynguin.
import ansible.plugins.become.su as module_0

def test_case_0():
    try:
        list_0 = []
        become_module_0 = module_0.BecomeModule()
        var_0 = become_module_0.check_password_prompt(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'ZP{0x]*~T=[JGPZ'
        int_0 = 301
        become_module_0 = module_0.BecomeModule()
        var_0 = become_module_0.build_become_command(str_0, int_0)
    except BaseException:
        pass