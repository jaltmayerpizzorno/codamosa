# Automatically generated by Pynguin.
import cookiecutter.prompt as module_0

def test_case_0():
    try:
        bool_0 = True
        int_0 = 2132
        var_0 = module_0.read_user_variable(bool_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = None
        set_0 = {int_0}
        str_0 = '!QY(e'
        str_1 = 'no'
        int_1 = 1887
        list_0 = [int_1, str_0, set_0]
        tuple_0 = (str_0, str_1, int_1, list_0)
        str_2 = 'lWfdljV[03CP}SsXK'
        var_0 = module_0.read_user_yes_no(tuple_0, str_2)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = set()
        var_0 = module_0.read_repo_password(set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        set_0 = {bool_0, bool_0}
        set_1 = {bool_0}
        list_0 = [set_0, set_1, bool_0]
        var_0 = module_0.read_user_choice(set_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = -2019.13707
        set_0 = {float_0}
        var_0 = module_0.read_user_choice(float_0, set_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -207.15
        int_0 = -1672
        list_0 = []
        set_0 = None
        var_0 = module_0.prompt_choice_for_config(float_0, int_0, list_0, list_0, set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 2555
        var_0 = module_0.process_json(int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = False
        var_0 = module_0.read_user_dict(bool_0, bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = -2077.07595
        set_0 = {float_0, float_0}
        bytes_0 = b'\x85\xfd\xc5\xdfh\xa7'
        str_0 = 'a'
        var_0 = module_0.render_variable(set_0, bytes_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bytes_0 = b'\xb8'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
        str_0 = 'cUX'
        float_0 = 12.90134
        var_0 = module_0.prompt_choice_for_config(str_0, float_0, dict_0, str_0, bytes_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = False
        var_0 = module_0.prompt_for_config(bool_0)
    except BaseException:
        pass

def test_case_11():
    try:
        bytes_0 = b'7\x13\x8d\x912*9\x9a\xff9\xa0\xe43\x05+\xee\xfd3\x96\xc7'
        float_0 = -724.0955
        str_0 = None
        var_0 = module_0.render_variable(float_0, str_0, str_0)
        bytes_1 = b'\x88\x1fiD\xb9'
        list_0 = [str_0, var_0, bytes_0]
        var_1 = module_0.read_user_dict(bytes_1, list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bool_0 = False
        bool_1 = False
        list_0 = []
        float_0 = 169.035
        var_0 = module_0.prompt_choice_for_config(bool_0, bool_1, list_0, list_0, float_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'Unit tes\\ fxr function process_json'
        int_0 = 731
        set_0 = set()
        dict_0 = {str_0: str_0, str_0: int_0}
        var_0 = module_0.read_user_dict(set_0, dict_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bytes_0 = b'7\x13\x8d\x912*9\x9a\xff9\xa0\xe43\x05+\xee\xfd3\x96\xc7'
        float_0 = -724.0955
        str_0 = None
        var_0 = module_0.render_variable(float_0, str_0, str_0)
        bool_0 = True
        bytes_1 = b'\xa1\x87z]\xa7\xdb\x98\x0e\xb3V\xc4'
        list_0 = [str_0, var_0, bytes_0]
        var_1 = module_0.render_variable(bytes_1, list_0, bool_0)
    except BaseException:
        pass

def test_case_15():
    try:
        bytes_0 = b'\xb5\xce\xb6\x9fA\x87\xd0 \xd5W\xbev\xc4dL='
        float_0 = 933.287339
        str_0 = None
        str_1 = ''
        str_2 = 'cookiecutters_dir'
        list_0 = [str_0, str_0]
        dict_0 = {str_1: list_0}
        var_0 = module_0.render_variable(str_2, list_0, dict_0)
        var_1 = module_0.render_variable(float_0, str_0, str_1)
        bool_0 = True
        bytes_1 = b'\xa1\x87z]\xa7\xdb\x98\x0e\xb3V\xc4'
        list_1 = [str_1, var_1, bytes_0]
        var_2 = module_0.render_variable(bytes_1, list_1, bool_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '(lFO_)2WXEwrd-O ,/'
        dict_0 = {}
        str_1 = 'User config not found or not specified. Loading default config.'
        var_0 = module_0.render_variable(str_0, dict_0, str_1)
        int_0 = -2318
        bytes_0 = b'\xb5\xce\xb6\x9fA\x87\xd0 \xd5W\xbev\xc4dL='
        str_2 = ''
        bool_0 = True
        list_0 = [str_2, int_0, int_0, bytes_0, str_2, int_0]
        var_1 = module_0.render_variable(bytes_0, list_0, bool_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '(lFO_)2WXEwrd-O ,/'
        dict_0 = {str_0: str_0}
        str_1 = 'User config not found or not specified. Loading default config.'
        var_0 = module_0.render_variable(str_0, dict_0, str_1)
    except BaseException:
        pass

def test_case_18():
    try:
        int_0 = -2318
        float_0 = -724.0955
        str_0 = None
        str_1 = ''
        var_0 = module_0.render_variable(float_0, str_0, str_1)
        bool_0 = False
        bytes_0 = b'.\xaa\x14?\xd3\x81RP|'
        dict_0 = {str_0: bool_0, float_0: bytes_0}
        str_2 = '__'
        var_1 = module_0.render_variable(int_0, dict_0, str_2)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '{"test": "test"}'
        var_0 = module_0.process_json(str_0)
        str_1 = '["test"]'
        var_1 = module_0.process_json(str_1)
    except BaseException:
        pass