# Automatically generated by Pynguin.
import cookiecutter.prompt as module_0
import collections as module_1

def test_case_0():
    try:
        str_0 = '{k2JA`W5d&W;5Z'
        str_1 = 'n;VhXS'
        var_0 = module_0.read_user_variable(str_0, str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\n    Test if the process_json function is working\n    '
        str_1 = '{"name":"test"}'
        var_0 = module_0.process_json(str_1)
        bool_0 = True
        dict_0 = {bool_0: bool_0}
        set_0 = {str_0, str_1}
        tuple_0 = (bool_0, dict_0, set_0)
        str_2 = 'gS0+BK+JA+/b)!'
        var_1 = module_0.read_user_yes_no(tuple_0, str_2)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 197.29685
        var_0 = module_0.read_repo_password(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'wohW^N{\rAdnXo6>'
        bytes_0 = b'\xfc\x86\xd3\x06\xb4m'
        str_1 = 'Config file {} does not exist.'
        tuple_0 = ()
        int_0 = 0
        var_0 = module_0.prompt_choice_for_config(str_0, bytes_0, str_1, tuple_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ''
        list_0 = [str_0, str_0, str_0, str_0]
        var_0 = module_0.read_user_choice(str_0, list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        str_0 = 'E<6ONPshb!9E<7Cgl'
        var_0 = module_0.read_user_choice(list_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        tuple_0 = None
        var_0 = module_0.process_json(tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'\x97%\x01S\xb1\xe4(+e\x8dQm\x04'
        ordered_dict_0 = module_1.OrderedDict()
        var_0 = module_0.read_user_dict(bytes_0, ordered_dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'testkey'
        var_0 = module_0.read_user_dict(str_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        list_0 = []
        str_0 = 'Rendered dir %s must exist in output_dir %s'
        int_0 = 4109
        dict_0 = {int_0: list_0}
        var_0 = module_0.render_variable(list_0, str_0, dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        set_0 = None
        list_0 = []
        var_0 = module_0.render_variable(list_0, set_0, set_0)
        bytes_0 = b'\t\x14\x96\x0eC'
        var_1 = module_0.process_json(bytes_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = -205
        tuple_0 = (int_0,)
        bytes_0 = b'\x97\xe1\x86`g\x98F\xa4BY2\x8cz\xa5\xe9\xeaq8\x9a'
        set_0 = {tuple_0, bytes_0, int_0}
        float_0 = -1899.2059
        var_0 = module_0.render_variable(tuple_0, set_0, float_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bytes_0 = b'\xfc\t\xb1'
        complex_0 = None
        int_0 = -4385
        float_0 = 283.272
        var_0 = module_0.prompt_choice_for_config(complex_0, complex_0, int_0, float_0, bytes_0)
    except BaseException:
        pass

def test_case_13():
    try:
        dict_0 = None
        list_0 = [dict_0, dict_0, dict_0]
        bool_0 = True
        var_0 = module_0.prompt_for_config(list_0, bool_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bytes_0 = b"'\x9f\x92"
        list_0 = [bytes_0, bytes_0]
        bool_0 = True
        int_0 = 1117
        int_1 = 533
        set_0 = {int_1, int_1, bool_0, int_1}
        str_0 = 'kqh)Gw&6nI\r?\x0c(p%ZEn'
        str_1 = 'xjzGVSR=W, -]'
        tuple_0 = (set_0, str_0, str_1)
        var_0 = module_0.prompt_choice_for_config(list_0, bool_0, int_0, list_0, tuple_0)
    except BaseException:
        pass

def test_case_15():
    try:
        list_0 = []
        bool_0 = True
        int_0 = 1117
        int_1 = 533
        set_0 = {int_1, int_1, bool_0, int_1}
        str_0 = '"K<IX|HI\x0c/h\'.LvY6K>L'
        str_1 = 'xjzGVSR=W, -]'
        tuple_0 = (set_0, str_0, str_1)
        var_0 = module_0.prompt_choice_for_config(list_0, bool_0, int_0, list_0, tuple_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = ';estkey+'
        list_0 = []
        dict_0 = {}
        ordered_dict_0 = module_1.OrderedDict(*list_0, **dict_0)
        bool_0 = True
        var_0 = module_0.render_variable(ordered_dict_0, list_0, bool_0)
        var_1 = module_0.read_user_dict(str_0, str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        bytes_0 = b"'\x9f\x92"
        int_0 = None
        dict_0 = {int_0: int_0}
        float_0 = 288.91
        var_0 = module_0.render_variable(bytes_0, dict_0, float_0)
        float_1 = -1330.0
        tuple_0 = (int_0, float_1, bytes_0)
        bool_0 = True
        var_1 = module_0.read_user_dict(bool_0, tuple_0)
    except BaseException:
        pass

def test_case_18():
    try:
        bytes_0 = b"'\x9f\x92"
        str_0 = '|sIw2'
        list_0 = [bytes_0]
        int_0 = None
        float_0 = -1330.3
        tuple_0 = (int_0, float_0, bytes_0)
        var_0 = module_0.render_variable(str_0, list_0, tuple_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '2'
        var_0 = module_0.process_json(str_0)
    except BaseException:
        pass