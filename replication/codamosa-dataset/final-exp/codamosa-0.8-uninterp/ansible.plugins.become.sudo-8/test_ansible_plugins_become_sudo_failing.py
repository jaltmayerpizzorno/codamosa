# Automatically generated by Pynguin.
import ansible.plugins.become.sudo as module_0

def test_case_0():
    try:
        float_0 = -884.02
        list_0 = [float_0, float_0, float_0, float_0]
        become_module_0 = module_0.BecomeModule()
        var_0 = become_module_0.build_become_command(float_0, list_0)
    except BaseException:
        pass