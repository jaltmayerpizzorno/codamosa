# Automatically generated by Pynguin.
import ansible.plugins.shell.powershell as module_0

def test_case_0():
    try:
        bytes_0 = b'\xc2W\xbc'
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.get_remote_filename(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xfc\xe5\xcdw\xafh\x84a\xc8,SN'
        set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.get_remote_filename(set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.path_has_trailing_slash(shell_module_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'passthru'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.chmod(str_0, dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 1010.881642
        str_0 = '\x0bK/Fxt\x0b;'
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.chown(float_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'xUU\x0bE.C]'
        bytes_0 = b'D\x83\xeeBn\xf3~A\x95\x1b\x8e\x0e\xe3\x07]\xe5\xa1 '
        dict_0 = None
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.set_user_facl(str_0, bytes_0, dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        shell_module_0 = module_0.ShellModule()
        tuple_0 = ()
        var_0 = shell_module_0.expand_user(tuple_0, shell_module_0)
        set_0 = {tuple_0}
        var_1 = shell_module_0.remove(tuple_0, set_0)
        var_2 = shell_module_0.join_path()
    except BaseException:
        pass

def test_case_7():
    try:
        shell_module_0 = module_0.ShellModule()
        str_0 = '/tmp'
        var_0 = shell_module_0.mkdtemp(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        dict_0 = {}
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.mkdtemp(dict_0)
    except BaseException:
        pass