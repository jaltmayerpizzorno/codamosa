# Automatically generated by Pynguin.
import ansible.plugins.become.sudo as module_0

def test_case_0():
    try:
        become_module_0 = module_0.BecomeModule()
        str_0 = '!pWK/6wxa+'
        become_module_1 = module_0.BecomeModule()
        var_0 = become_module_1.build_become_command(become_module_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        become_module_0 = module_0.BecomeModule()
        str_0 = 'become_exe'
        var_0 = become_module_0.set_option(str_0, str_0)
        str_1 = 's '
        str_2 = 'sh'
        var_1 = become_module_0.build_become_command(str_1, str_2)
    except BaseException:
        pass

def test_case_2():
    try:
        become_module_0 = module_0.BecomeModule()
        str_0 = 'become_exe'
        str_1 = 'sudo'
        var_0 = become_module_0.set_option(str_0, str_1)
        str_2 = 'become_flags'
        var_1 = become_module_0.set_option(str_2, str_1)
        str_3 = 'ls ~'
        var_2 = become_module_0.build_become_command(str_3, str_1)
    except BaseException:
        pass

def test_case_3():
    try:
        become_module_0 = module_0.BecomeModule()
        str_0 = 'become_exe'
        str_1 = ''
        var_0 = become_module_0.set_option(str_0, str_1)
        str_2 = ']Ly'
        str_3 = 'sh'
        var_1 = become_module_0.build_become_command(str_2, str_3)
    except BaseException:
        pass

def test_case_4():
    try:
        become_module_0 = module_0.BecomeModule()
        str_0 = 'become_exe'
        str_1 = ''
        become_module_1 = module_0.BecomeModule()
        var_0 = become_module_0.set_option(str_0, str_1)
        str_2 = 'become_flags'
        become_module_2 = module_0.BecomeModule()
        var_1 = become_module_0.set_option(str_2, str_1)
        str_3 = 'ls ~'
        list_0 = []
        float_0 = 68.45644
        become_module_3 = module_0.BecomeModule()
        become_module_4 = module_0.BecomeModule()
        var_2 = become_module_0.build_become_command(list_0, float_0)
        var_3 = become_module_0.build_become_command(str_3, str_1)
    except BaseException:
        pass