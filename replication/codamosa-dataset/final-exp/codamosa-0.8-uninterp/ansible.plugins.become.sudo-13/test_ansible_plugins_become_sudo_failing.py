# Automatically generated by Pynguin.
import ansible.plugins.become.sudo as module_0

def test_case_0():
    try:
        become_module_0 = module_0.BecomeModule()
        set_0 = set()
        var_0 = become_module_0.build_become_command(set_0, become_module_0)
        var_1 = become_module_0.build_become_command(become_module_0, become_module_0)
    except BaseException:
        pass