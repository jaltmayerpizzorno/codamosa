# Automatically generated by Pynguin.
import ansible.plugins.become.sudo as module_0

def test_case_0():
    try:
        int_0 = -703
        str_0 = 'Oba/3M6@<d'
        become_module_0 = module_0.BecomeModule()
        var_0 = become_module_0.build_become_command(int_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        become_module_0 = module_0.BecomeModule()
        var_0 = None
        var_1 = become_module_0.build_become_command(var_0, become_module_0)
        var_2 = become_module_0.build_become_command(become_module_0, become_module_0)
    except BaseException:
        pass