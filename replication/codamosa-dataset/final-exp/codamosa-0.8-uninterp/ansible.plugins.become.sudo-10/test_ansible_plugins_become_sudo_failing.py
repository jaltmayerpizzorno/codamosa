# Automatically generated by Pynguin.
import ansible.plugins.become.sudo as module_0

def test_case_0():
    try:
        float_0 = 612.69
        str_0 = 'NE3WMv{TK TQ'
        become_module_0 = module_0.BecomeModule()
        var_0 = become_module_0.build_become_command(float_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        become_module_0 = module_0.BecomeModule()
        var_0 = None
        var_1 = become_module_0.build_become_command(var_0, var_0)
        var_2 = become_module_0.build_become_command(become_module_0, become_module_0)
    except BaseException:
        pass