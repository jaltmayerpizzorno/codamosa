# Automatically generated by Pynguin.
import ansible.plugins.become.sudo as module_0

def test_case_0():
    try:
        float_0 = -69.1
        bytes_0 = b'\xfb\x19\xcf\xfc\x89\x1f\x04\xb4\nK\xe7\xc7J\x06\xfdu'
        become_module_0 = module_0.BecomeModule()
        var_0 = become_module_0.build_become_command(float_0, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        become_module_0 = module_0.BecomeModule()
        tuple_0 = None
        var_0 = become_module_0.build_become_command(tuple_0, tuple_0)
        var_1 = become_module_0.build_become_command(become_module_0, tuple_0)
    except BaseException:
        pass