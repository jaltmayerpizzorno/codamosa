# Automatically generated by Pynguin.
import ansible.modules.command as module_0

def test_case_0():
    try:
        bool_0 = True
        bytes_0 = b'\xaf=\xf7\x19>\xf5\xa6\xc8\xc6\x15\x0c\x97\x00\x93\xf5\x94\xb8'
        var_0 = module_0.check_command(bool_0, bytes_0)
        list_0 = [bool_0]
        var_1 = module_0.check_command(bytes_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '/bin/yum'
        list_0 = [str_0]
        var_0 = module_0.check_command(list_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'sudo apt-get install'
        str_1 = 'install'
        var_0 = module_0.check_command(str_1, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '/bin/touch'
        set_0 = set()
        list_0 = [str_0]
        var_0 = module_0.check_command(set_0, list_0)
    except BaseException:
        pass