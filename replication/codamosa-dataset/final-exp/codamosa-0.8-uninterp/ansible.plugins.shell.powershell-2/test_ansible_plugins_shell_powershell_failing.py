# Automatically generated by Pynguin.
import ansible.plugins.shell.powershell as module_0
import base64 as module_1

def test_case_0():
    try:
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.join_path()
    except BaseException:
        pass

def test_case_1():
    try:
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.path_has_trailing_slash(shell_module_0)
    except BaseException:
        pass

def test_case_2():
    try:
        shell_module_0 = module_0.ShellModule()
        set_0 = {shell_module_0, shell_module_0, shell_module_0}
        float_0 = 851.836583
        var_0 = shell_module_0.chmod(set_0, float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = None
        bool_1 = False
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.chown(bool_0, bool_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'U\nW'
        str_1 = '70w%'
        bool_0 = None
        shell_module_0 = module_0.ShellModule()
        tuple_0 = (str_1, bool_0, shell_module_0)
        shell_module_1 = module_0.ShellModule()
        var_0 = shell_module_1.set_user_facl(str_0, tuple_0, tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\xd2\xd8A@\x10'
        bool_0 = True
        bool_1 = False
        shell_module_0 = module_0.ShellModule()
        set_0 = {bool_0, bool_0, bytes_0}
        bool_2 = True
        var_0 = shell_module_0.remove(set_0, bool_2)
        shell_module_1 = module_0.ShellModule()
        var_1 = shell_module_1.build_module_command(bytes_0, bool_0, bool_1, shell_module_0)
    except BaseException:
        pass

def test_case_6():
    try:
        var_0 = None
        shell_module_0 = module_0.ShellModule()
        var_1 = shell_module_0.mkdtemp()
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'K\xd3A@\x10'
        bool_0 = True
        bool_1 = False
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.build_module_command(bytes_0, bool_0, bool_1, shell_module_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'Q5!=U~7_Tyb&s_0Q{m'
        set_0 = None
        dict_0 = None
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.build_module_command(str_0, set_0, dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        shell_module_0 = module_0.ShellModule()
        dict_0 = None
        str_0 = 'r*)+'
        var_0 = shell_module_0.build_module_command(dict_0, str_0, dict_0)
        str_1 = '_i1'
        bool_0 = None
        var_1 = shell_module_0.set_user_facl(str_1, bool_0, bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        shell_module_0 = module_0.ShellModule()
        dict_0 = None
        str_0 = 'r*)g'
        var_0 = shell_module_0.build_module_command(dict_0, str_0, dict_0)
        bytes_0 = b'pp\xfa\xf0`4wLX\x1a\xda\xceq-\xfb\x15\xf3Q\xb2'
        list_0 = [bytes_0]
        var_1 = shell_module_0.checksum(list_0)
        int_0 = 8192
        set_0 = None
        list_1 = [var_0, var_1, bytes_0]
        var_2 = shell_module_0.join_path(*list_1)
        int_1 = -1144
        dict_1 = {int_0: set_0, int_0: shell_module_0, str_0: int_1, int_1: int_1}
        var_3 = shell_module_0.build_module_command(bytes_0, dict_1, int_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '\n    Data about an individual host.\n    '
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.exists(str_0)
        var_1 = shell_module_0.mkdtemp(shell_module_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '}<*%=rU&'
        shell_module_0 = module_0.ShellModule()
        bool_0 = True
        float_0 = None
        var_0 = shell_module_0.build_module_command(bool_0, float_0, str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bytes_0 = b'%\xb4XdZ\xb5\xec/'
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.path_has_trailing_slash(bytes_0)
        shell_module_1 = module_0.ShellModule()
        dict_0 = None
        str_0 = 'r*)g'
        var_1 = shell_module_1.build_module_command(dict_0, str_0, dict_0)
        bytes_1 = b'pp\xfa\xf0`4wLX\x1a\xda\xceq-\xfb\x15\xf3Q\xb2'
        list_0 = [bytes_1]
        var_2 = shell_module_1.checksum(list_0)
        list_1 = None
        tuple_0 = ()
        var_3 = shell_module_1.expand_user(list_1, tuple_0)
        list_2 = [var_1, var_2, bytes_1]
        var_4 = shell_module_1.join_path(*list_2)
        var_5 = shell_module_1.path_has_trailing_slash(shell_module_1)
    except BaseException:
        pass

def test_case_14():
    try:
        shell_module_0 = module_0.ShellModule()
        str_0 = 'test'
        bool_0 = False
        var_0 = None
        str_1 = 'c:\\TMP'
        var_1 = shell_module_0.mkdtemp(str_0, bool_0, var_0, str_1)
        str_2 = 'utf-8'
        var_2 = module_1.decode(str_2)
    except BaseException:
        pass

def test_case_15():
    try:
        shell_module_0 = module_0.ShellModule()
        str_0 = '"/tmp\\"'
        var_0 = shell_module_0.path_has_trailing_slash(str_0)
    except BaseException:
        pass