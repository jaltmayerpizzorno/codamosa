# Automatically generated by Pynguin.
import cookiecutter.prompt as module_0
import collections as module_1

def test_case_0():
    try:
        tuple_0 = None
        list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
        float_0 = 783.70383
        var_0 = module_0.read_user_variable(list_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Select {}:'
        set_0 = set()
        var_0 = module_0.read_user_yes_no(str_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 1047
        var_0 = module_0.read_repo_password(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = {}
        str_0 = ''
        bool_0 = False
        var_1 = module_0.prompt_choice_for_config(var_0, str_0, str_0, str_0, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b''
        list_0 = [bytes_0, bytes_0, bytes_0]
        var_0 = module_0.read_user_choice(list_0, list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '{D}nnTcj*z1@.\x0cQAzH0'
        bytes_0 = b'\xe0\xbc\xe4G\xe2\xbe+\xbd\xa5\x08g\xf0\x04'
        var_0 = module_0.read_user_choice(str_0, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '{"a": "b", {"c": "d"}]'
        var_0 = module_0.process_json(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '[{"a": "b"}, {"c": "d"}]'
        var_0 = module_0.process_json(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '`,YPe\tT'
        var_0 = module_0.read_user_dict(str_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bytes_0 = b''
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
        str_0 = 'vb!pP\r{ACy:M'
        var_0 = module_0.render_variable(bytes_0, dict_0, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'X<*aE][HudEF#xt\r'
        bool_0 = None
        list_0 = [str_0]
        var_0 = module_0.render_variable(bool_0, list_0, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        tuple_0 = ()
        dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0}
        float_0 = 401.949
        str_0 = 'e`)%9D\x0bQ\t'
        str_1 = ''
        list_0 = [dict_0, dict_0, str_0]
        var_0 = module_0.prompt_choice_for_config(dict_0, float_0, str_0, str_1, list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'ask'
        bool_0 = False
        list_0 = [str_0, bool_0]
        var_0 = module_0.prompt_for_config(list_0, list_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bytes_0 = b'\x06i\x93e\xc9\x14j\xad\x11\x07\x97\x9e|\x13\x96\x88\xfd'
        str_0 = '7'
        dict_0 = {str_0: bytes_0, str_0: str_0}
        set_0 = {str_0, bytes_0, str_0}
        var_0 = module_0.prompt_choice_for_config(bytes_0, str_0, dict_0, set_0, str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bytes_0 = b'1o\x9a\x84\x91\xbdw;\x83\xa6y\x80\x12}'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
        set_0 = None
        var_0 = module_0.render_variable(dict_0, set_0, dict_0)
        var_1 = module_0.read_repo_password(bytes_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'bu!yf|Alcsw25Q?Jr'
        dict_0 = {}
        var_0 = module_0.read_user_dict(str_0, dict_0)
    except BaseException:
        pass

def test_case_16():
    try:
        int_0 = 1701
        ordered_dict_0 = module_1.OrderedDict()
        str_0 = '2013-2019, Audrey Roy and Cookiecutter community'
        var_0 = module_0.render_variable(int_0, ordered_dict_0, str_0)
        str_1 = 'Check whether the given `path` should only be copied anM not rendered.\n\n    Returns True if `path` matches a pattern in the given `context` dict,\n    otherwise False.\n\n    :param path: A file-system path referring to a file or dir that\n        should be rendered or just copied.\n   :param context: cookiecutter context.\n    '
        var_1 = module_0.read_user_dict(str_1, str_1)
    except BaseException:
        pass

def test_case_17():
    try:
        bool_0 = None
        int_0 = -1041
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: int_0, int_0: int_0}
        list_0 = [bool_0, int_0]
        var_0 = module_0.render_variable(bool_0, dict_0, list_0)
    except BaseException:
        pass