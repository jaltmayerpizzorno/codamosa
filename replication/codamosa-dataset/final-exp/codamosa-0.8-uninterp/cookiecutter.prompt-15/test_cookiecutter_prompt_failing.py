# Automatically generated by Pynguin.
import cookiecutter.prompt as module_0

def test_case_0():
    try:
        str_0 = '{"foo": "bar", "baz": "qux"}'
        var_0 = module_0.process_json(str_0)
        int_0 = 2
        set_0 = {str_0}
        var_1 = module_0.read_user_variable(int_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        bool_0 = False
        var_0 = module_0.read_user_yes_no(bool_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xb2\x19s!\xc3RI}\xfd}\xce\xec\xb5W8 '
        var_0 = module_0.read_repo_password(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "n/UZko}'d^URZR&yz$"
        str_1 = "+470U('HM9<"
        dict_0 = {str_0: str_1, str_0: str_0, str_1: str_0}
        tuple_0 = (dict_0,)
        float_0 = -696.0
        bool_0 = True
        list_0 = []
        var_0 = module_0.prompt_choice_for_config(tuple_0, float_0, bool_0, list_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        dict_0 = {bool_0: bool_0}
        var_0 = module_0.read_user_choice(bool_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        var_0 = module_0.process_json(bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'key'
        var_0 = module_0.read_user_dict(str_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        list_0 = []
        bytes_0 = b'g'
        var_0 = module_0.render_variable(list_0, list_0, bytes_0)
        str_0 = 'nGwoin'
        var_1 = module_0.read_user_dict(str_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'o4W@v#GU\\-'
        str_1 = '&l;w=HpxwE`(a%>F%|'
        str_2 = "QFHz@GbXH5J[!/'-h3Zi"
        int_0 = -3016
        dict_0 = {str_2: str_0, str_0: str_2, str_0: str_1, str_0: int_0}
        var_0 = module_0.render_variable(str_0, str_1, dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = None
        set_0 = {int_0, int_0, int_0}
        bytes_0 = b'\xc8\xc0\x82'
        float_0 = -2317.0534
        str_0 = 'x5NX"tq~IBNt.I+'
        tuple_0 = (bytes_0, float_0, str_0)
        set_1 = {float_0}
        int_1 = 1428
        dict_0 = {str_0: set_1, int_1: float_0}
        var_0 = module_0.render_variable(set_0, tuple_0, dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        set_0 = set()
        str_0 = '\x0cR'
        list_0 = [set_0, str_0, set_0]
        tuple_0 = (list_0, str_0, list_0)
        str_1 = ''
        float_0 = 1077.63
        str_2 = '<@>oC'
        var_0 = module_0.prompt_choice_for_config(str_1, tuple_0, float_0, set_0, str_2)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 1589
        set_0 = {int_0, int_0, int_0, int_0}
        var_0 = module_0.prompt_for_config(set_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = 2
        bool_0 = True
        str_0 = 'User configuration file'
        var_0 = module_0.prompt_choice_for_config(int_0, bool_0, str_0, str_0, int_0)
    except BaseException:
        pass

def test_case_13():
    try:
        undefined_0 = None
        template_0 = None
        int_0 = 1005
        var_0 = module_0.render_variable(undefined_0, template_0, int_0)
        str_0 = 'R>#C+0'
        var_1 = module_0.read_user_dict(str_0, str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        list_0 = [bool_0, dict_0, bool_0]
        var_0 = module_0.read_user_choice(bool_0, list_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'key'
        var_0 = {}
        var_1 = module_0.read_user_dict(str_0, var_0)
    except BaseException:
        pass

def test_case_16():
    try:
        bytes_0 = b'\xb2\xa46F|\xb3\xc7\r\x9a\xe4N\xa3\x1fG'
        dict_0 = {}
        var_0 = module_0.render_variable(bytes_0, dict_0, bytes_0)
        var_1 = module_0.read_user_dict(bytes_0, dict_0)
    except BaseException:
        pass

def test_case_17():
    try:
        bool_0 = True
        list_0 = [bool_0]
        str_0 = 't50w*v\\Mdq\t N^j,H96I'
        bytes_0 = b'\xb2\xa46F|\xb3\xc7\r\x9a\xe4N\xa3\x1fG'
        dict_0 = {}
        var_0 = module_0.render_variable(bytes_0, dict_0, bytes_0)
        var_1 = module_0.render_variable(list_0, list_0, str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        bytes_0 = b'\xb2\xa46F|\xb3\xc7\x1b\x9a\xa1N\xa3\x1fG'
        dict_0 = {bytes_0: bytes_0}
        var_0 = module_0.render_variable(bytes_0, dict_0, bytes_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '{}'
        var_0 = module_0.process_json(str_0)
        str_1 = '{"a": 1}'
        var_1 = module_0.process_json(str_1)
        str_2 = '[1,2,3]'
        var_2 = module_0.process_json(str_2)
    except BaseException:
        pass