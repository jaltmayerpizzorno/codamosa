# Automatically generated by Pynguin.
import cookiecutter.prompt as module_0

def test_case_0():
    try:
        complex_0 = None
        bool_0 = True
        var_0 = module_0.read_user_variable(complex_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'j#CsOB.^]$Wx\x0b'
        str_1 = 'https://gitlab.com/{0}.git'
        var_0 = module_0.read_user_yes_no(str_0, str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 763.66
        var_0 = module_0.read_repo_password(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 543
        str_0 = '<3y'
        var_0 = module_0.read_user_choice(int_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        var_0 = module_0.process_json(bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '$R=T4"\'l\\U'
        var_0 = module_0.read_user_dict(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        tuple_0 = (bool_0,)
        str_0 = '1OEiB7&/i<arOcaU'
        bytes_0 = None
        var_0 = module_0.render_variable(tuple_0, str_0, bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        template_0 = None
        str_0 = "='Clr0"
        strict_environment_0 = None
        var_0 = module_0.render_variable(str_0, template_0, strict_environment_0)
        template_1 = None
        var_1 = module_0.process_json(template_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'U'
        bytes_0 = b'\x8d\x93\x14\x9e\x9b\x17~.H\xd0\x03\x9f\xc3,'
        list_0 = []
        float_0 = 1630.84678
        var_0 = module_0.prompt_choice_for_config(str_0, bytes_0, list_0, bytes_0, float_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = None
        str_1 = 'D \n/}tDb0'
        list_0 = [str_1, str_0]
        int_0 = None
        dict_0 = {}
        bytes_0 = b'R\x90\x9e\x99?\x8b\xef\x18l\xe2\xb1G\xb0\x8e\x90\x81\x82'
        var_0 = module_0.prompt_choice_for_config(str_1, list_0, int_0, dict_0, bytes_0)
    except BaseException:
        pass

def test_case_10():
    try:
        dict_0 = {}
        float_0 = -1835.0
        tuple_0 = (dict_0, float_0)
        list_0 = [tuple_0]
        bool_0 = False
        float_1 = 2305.07667
        var_0 = module_0.prompt_choice_for_config(tuple_0, list_0, bool_0, float_1, dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = None
        int_1 = 4
        tuple_0 = ()
        str_0 = None
        var_0 = module_0.prompt_choice_for_config(int_0, int_0, int_1, tuple_0, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = None
        bool_0 = False
        dict_0 = {}
        list_0 = [str_0, str_0, bool_0]
        var_0 = module_0.render_variable(bool_0, dict_0, list_0)
        int_0 = 1088
        var_1 = module_0.prompt_for_config(int_0)
    except BaseException:
        pass

def test_case_13():
    try:
        dict_0 = None
        str_0 = 'U'
        list_0 = [dict_0, str_0]
        bool_0 = False
        var_0 = module_0.render_variable(bool_0, list_0, list_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bytes_0 = b'\xd1^\xa5\x07\xb4Y1m\xc7\x04'
        int_0 = 1027
        list_0 = [bytes_0, int_0, int_0]
        var_0 = module_0.read_user_choice(int_0, list_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'The resulting file already exists: %s'
        list_0 = [str_0, str_0, str_0]
        dict_0 = {str_0: list_0, str_0: str_0}
        var_0 = module_0.read_user_dict(dict_0, dict_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = None
        bool_0 = False
        dict_0 = {str_0: str_0, str_0: str_0}
        list_0 = [str_0, str_0, bool_0]
        var_0 = module_0.render_variable(bool_0, dict_0, list_0)
        tuple_0 = ()
        var_1 = module_0.read_user_dict(bool_0, tuple_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '{"name": "John", "address": {"number": 3, "street": "High Street"}}'
        var_0 = module_0.process_json(str_0)
        str_1 = '0'
        var_1 = module_0.process_json(str_1)
    except BaseException:
        pass