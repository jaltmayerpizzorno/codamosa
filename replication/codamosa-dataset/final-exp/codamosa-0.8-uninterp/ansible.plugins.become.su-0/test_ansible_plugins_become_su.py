# Automatically generated by Pynguin.
import ansible.plugins.become.su as module_0

def test_case_0():
    pass

def test_case_1():
    become_module_0 = module_0.BecomeModule()
    str_0 = 'become_exe'
    str_1 = ''
    var_0 = become_module_0.set_option(str_0, str_1)
    str_2 = 'become_flags'
    var_1 = become_module_0.set_option(str_2, str_1)
    str_3 = 'become_user'
    var_2 = become_module_0.set_option(str_3, str_1)
    str_4 = 'ls'
    bool_0 = False
    var_3 = become_module_0.build_become_command(str_4, bool_0)