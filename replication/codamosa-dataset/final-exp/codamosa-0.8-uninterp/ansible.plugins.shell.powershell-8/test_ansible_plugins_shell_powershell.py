# Automatically generated by Pynguin.
import ansible.plugins.shell.powershell as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 1903
    list_0 = [int_0, int_0]
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.join_path(*list_0)

def test_case_2():
    var_0 = None
    bool_0 = False
    shell_module_0 = module_0.ShellModule()
    str_0 = 'tempdir\\testdir\\testfile.txt'
    var_1 = shell_module_0.get_remote_filename(str_0)
    str_1 = 'tempdir\\testdir\\testfile.txt.ext'
    var_2 = shell_module_0.get_remote_filename(str_1)
    str_2 = 'tempdir\\testdir\\testfile'
    var_3 = shell_module_0.get_remote_filename(str_2)

def test_case_3():
    shell_module_0 = module_0.ShellModule()
    str_0 = '/foo/bar/baz.ps1'
    var_0 = shell_module_0.get_remote_filename(str_0)

def test_case_4():
    dict_0 = {}
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.remove(dict_0)

def test_case_5():
    bool_0 = False
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.expand_user(bool_0)

def test_case_6():
    list_0 = []
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.exists(list_0)

def test_case_7():
    float_0 = -21.252924
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.checksum(float_0)

def test_case_8():
    str_0 = '#!powershell'
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.build_module_command(str_0, str_0, str_0, str_0)

def test_case_9():
    str_0 = '#!pow0ershell'
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.build_module_command(str_0, str_0, str_0, str_0)

def test_case_10():
    str_0 = '6#!powershell'
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.build_module_command(str_0, str_0, str_0, str_0)

def test_case_11():
    shell_module_0 = module_0.ShellModule()
    str_0 = ''
    str_1 = 'ansible'
    var_0 = shell_module_0.expand_user(str_0, str_1)
    str_2 = '~\\testpath'
    var_1 = shell_module_0.expand_user(str_2, str_1)
    str_3 = '~'
    var_2 = shell_module_0.expand_user(str_3, str_1)
    str_4 = '~NotSupportedUser'
    var_3 = shell_module_0.expand_user(str_4, str_1)

def test_case_12():
    shell_module_0 = module_0.ShellModule()
    str_0 = ''
    var_0 = shell_module_0.expand_user(str_0, str_0)
    str_1 = '~\\testpath'
    var_1 = shell_module_0.expand_user(str_1, str_0)
    shell_module_1 = module_0.ShellModule()

def test_case_13():
    int_0 = -298
    set_0 = {int_0, int_0, int_0, int_0}
    shell_module_0 = module_0.ShellModule()
    shell_module_1 = module_0.ShellModule()
    var_0 = shell_module_1.expand_user(set_0, shell_module_0)
    list_0 = None
    var_1 = shell_module_1.expand_user(list_0)
    list_1 = [set_0]
    list_2 = [list_1]
    str_0 = 'rQ%5rZ7Jbh<PPC:"uK{'
    str_1 = '50{2ZEr}9L:'
    str_2 = '`'
    var_2 = shell_module_1.remove(list_1)
    var_3 = shell_module_1.build_module_command(str_0, str_1, str_2, shell_module_1)
    bool_0 = None
    bytes_0 = None
    tuple_0 = (bool_0, bytes_0)
    str_3 = "playbook group_vars for '%s'"
    float_0 = None
    var_4 = shell_module_0.mkdtemp(tuple_0, str_3, float_0, list_2)

def test_case_14():
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.env_prefix()
    str_0 = 'test a:Srg'
    shell_module_1 = module_0.ShellModule()
    shell_module_2 = module_0.ShellModule()
    shell_module_3 = module_0.ShellModule()
    dict_0 = {}
    tuple_0 = (str_0, str_0, shell_module_3, dict_0)
    str_1 = 'iu) '
    str_2 = 'YL'
    str_3 = '?vq@'
    shell_module_4 = module_0.ShellModule()
    var_1 = shell_module_4.build_module_command(tuple_0, str_1, str_2, str_3)
    str_4 = '/holders/'
    shell_module_5 = module_0.ShellModule()
    var_2 = shell_module_5.path_has_trailing_slash(str_4)