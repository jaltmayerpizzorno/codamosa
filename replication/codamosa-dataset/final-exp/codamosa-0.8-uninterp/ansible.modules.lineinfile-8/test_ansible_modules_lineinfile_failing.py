# Automatically generated by Pynguin.
import ansible.modules.lineinfile as module_0

def test_case_0():
    try:
        bytes_0 = b'\xe4\x11\xd3\x92\t\xefUJ\x8d\xa8'
        set_0 = {bytes_0}
        str_0 = '*P-'
        var_0 = module_0.write_changes(bytes_0, set_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = ()
        float_0 = None
        set_0 = {float_0, float_0, tuple_0}
        bytes_0 = b'\x1cb'
        var_0 = module_0.check_file_attrs(float_0, tuple_0, set_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = ()
        str_0 = 'install_recommends'
        dict_0 = {tuple_0: tuple_0, str_0: str_0, str_0: str_0}
        list_0 = [dict_0, dict_0, str_0, tuple_0, dict_0]
        set_0 = {tuple_0, str_0}
        list_1 = [str_0, dict_0, dict_0, list_0]
        var_0 = module_0.present(tuple_0, str_0, dict_0, list_0, list_0, list_0, str_0, set_0, set_0, set_0, list_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '/etc/passwd'
        var_0 = None
        bool_0 = True
        var_1 = module_0.absent(str_0, var_0, str_0, str_0, var_0, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = ()
        str_0 = '\nAM_=-7~3.\\T);\\./7U'
        dict_0 = {tuple_0: tuple_0, str_0: str_0, str_0: str_0}
        list_0 = [str_0, dict_0, dict_0, dict_0, tuple_0]
        set_0 = set()
        list_1 = [str_0, dict_0, tuple_0, dict_0, dict_0, list_0]
        var_0 = module_0.present(tuple_0, str_0, dict_0, list_0, list_0, list_0, str_0, set_0, set_0, set_0, list_1)
    except BaseException:
        pass

def test_case_5():
    try:
        tuple_0 = ()
        str_0 = 'LAM_=-7~3)\\T);\\./7U'
        dict_0 = {tuple_0: tuple_0, str_0: str_0, str_0: str_0}
        list_0 = [dict_0, dict_0, str_0, tuple_0, dict_0]
        set_0 = {tuple_0, str_0}
        list_1 = [str_0, dict_0, dict_0, list_0]
        var_0 = module_0.present(tuple_0, str_0, dict_0, list_0, list_0, list_0, str_0, set_0, set_0, set_0, list_1)
    except BaseException:
        pass

def test_case_6():
    try:
        tuple_0 = ()
        str_0 = '/,!pv2EO3ovAmO\n#TOHR'
        dict_0 = {str_0: str_0, str_0: str_0}
        list_0 = [dict_0, tuple_0, str_0, tuple_0, dict_0, dict_0]
        set_0 = {tuple_0, str_0}
        list_1 = [str_0, dict_0, dict_0, list_0]
        var_0 = module_0.present(tuple_0, str_0, dict_0, list_0, list_0, list_0, str_0, set_0, set_0, set_0, list_1)
    except BaseException:
        pass