# Automatically generated by Pynguin.
import ansible.plugins.shell.powershell as module_0

def test_case_0():
    shell_module_0 = module_0.ShellModule()

def test_case_1():
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.env_prefix()

def test_case_2():
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.remove(shell_module_0)

def test_case_3():
    int_0 = 935
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.expand_user(int_0)

def test_case_4():
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.exists(shell_module_0)

def test_case_5():
    shell_module_0 = module_0.ShellModule()
    str_0 = '#!powershll'
    var_0 = shell_module_0.build_module_command(str_0, str_0, str_0, str_0)

def test_case_6():
    str_0 = '9`,}^9*R*D'
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.wrap_for_exec(str_0)

def test_case_7():
    str_0 = "Z&']_V"
    bool_0 = False
    complex_0 = None
    int_0 = 1360
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.build_module_command(bool_0, str_0, complex_0, int_0)
    shell_module_1 = module_0.ShellModule()
    var_1 = shell_module_1.exists(shell_module_0)
    list_0 = [str_0, str_0, str_0, str_0]
    str_1 = 'artifacts_manager'
    var_2 = shell_module_0.join_path(*list_0)
    str_2 = ' ,F\nOQ%m.AhW"GJ\n+u=\''
    dict_0 = {str_0: str_2, str_2: str_1, str_2: shell_module_0, str_1: shell_module_0}
    var_3 = shell_module_0.checksum(str_1, **dict_0)

def test_case_8():
    list_0 = None
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.expand_user(list_0)

def test_case_9():
    shell_module_0 = module_0.ShellModule()
    str_0 = '\r}\x0bB'
    var_0 = shell_module_0.remove(str_0, shell_module_0)

def test_case_10():
    shell_module_0 = module_0.ShellModule()
    str_0 = 'PC$S->9(]E[K;'
    str_1 = ';$8NM]2gzU2;d=UfC'
    shell_module_1 = module_0.ShellModule()
    var_0 = shell_module_1.build_module_command(shell_module_0, str_0, str_1, shell_module_0)

def test_case_11():
    shell_module_0 = module_0.ShellModule()
    str_0 = '#!powershell'
    var_0 = shell_module_0.build_module_command(str_0, str_0, str_0, str_0)

def test_case_12():
    shell_module_0 = module_0.ShellModule()
    str_0 = '~'
    str_1 = 'vagrant'
    var_0 = shell_module_0.expand_user(str_0, str_1)
    str_2 = 'user_home_path: %s'
    var_1 = str_2 % var_0
    var_2 = print(var_1)
    var_3 = shell_module_0.expand_user(str_0)
    var_4 = print(var_3)
    str_3 = '~\\.vagrant.d'
    var_5 = shell_module_0.expand_user(str_3)

def test_case_13():
    shell_module_0 = module_0.ShellModule()
    str_0 = 'foo.ps1'
    var_0 = shell_module_0.get_remote_filename(str_0)
    str_1 = 'foo'
    var_1 = shell_module_0.get_remote_filename(str_1)
    str_2 = 'foo.exe'
    var_2 = shell_module_0.get_remote_filename(str_2)