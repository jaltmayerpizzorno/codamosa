# Automatically generated by Pynguin.
import ansible.plugins.become.su as module_0

def test_case_0():
    try:
        str_0 = 'r!fN"bG*7 y'
        set_0 = set()
        bytes_0 = b'\xea\x9fw\x16\xe7\xde=\x17\xe8\x8e'
        become_module_0 = module_0.BecomeModule()
        var_0 = become_module_0.build_become_command(set_0, bytes_0)
        become_module_1 = module_0.BecomeModule()
        become_module_2 = module_0.BecomeModule()
        var_1 = become_module_2.check_password_prompt(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        become_module_0 = module_0.BecomeModule()
        become_module_1 = module_0.BecomeModule()
        str_0 = ' assemble a file from a directory of fragments '
        var_0 = become_module_0.build_become_command(str_0, become_module_1)
    except BaseException:
        pass

def test_case_2():
    try:
        become_module_0 = module_0.BecomeModule()
        str_0 = ''
        str_1 = 'become_exe'
        var_0 = become_module_0.set_option(str_1, str_0)
        str_2 = 'command'
        str_3 = 'become_flags'
        var_1 = become_module_0.set_option(str_3, str_2)
        str_4 = 'become_user'
        var_2 = become_module_0.set_option(str_4, str_4)
        bytes_0 = b'\xb9`\xb1nJu\xdc\x8cz]\x17-\x80zD\xfd\x8dyU\x00'
        set_0 = {str_1, var_2}
        var_3 = become_module_0.build_become_command(bytes_0, set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        become_module_0 = module_0.BecomeModule()
        str_0 = 'become_exe'
        var_0 = become_module_0.set_option(str_0, str_0)
        str_1 = 'become_flags'
        var_1 = become_module_0.set_option(str_1, str_1)
        str_2 = 'become_user'
        str_3 = 'waiting'
        var_2 = become_module_0.set_option(str_2, str_3)
        var_3 = become_module_0.build_become_command(str_0, become_module_0)
    except BaseException:
        pass

def test_case_4():
    try:
        become_module_0 = module_0.BecomeModule()
        str_0 = ''
        bool_0 = False
        var_0 = become_module_0.build_become_command(str_0, bool_0)
        str_1 = 'become_exe'
        var_1 = become_module_0.set_option(str_1, str_1)
        str_2 = 'command'
        str_3 = 'become_flags'
        var_2 = become_module_0.set_option(str_3, str_0)
        var_3 = become_module_0.build_become_command(str_2, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        become_module_0 = module_0.BecomeModule()
        str_0 = ''
        bool_0 = False
        var_0 = become_module_0.build_become_command(str_0, bool_0)
        str_1 = 'become_exe'
        var_1 = become_module_0.set_option(str_1, str_1)
        str_2 = 'command'
        str_3 = 'become_flags'
        var_2 = become_module_0.set_option(str_3, str_2)
        str_4 = 'become_user'
        var_3 = become_module_0.set_option(str_4, str_0)
        bytes_0 = b'e\x90\xd0g\x86\x9a\xccs\xba\x96-\xbf\x1b.\xdd<\xe0\xbb\x96'
        int_0 = 1176
        var_4 = become_module_0.build_become_command(bytes_0, int_0)
    except BaseException:
        pass