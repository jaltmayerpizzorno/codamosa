# Automatically generated by Pynguin.
import cookiecutter.prompt as module_0
import json as module_1
import collections as module_2

def test_case_0():
    try:
        str_0 = 'Ib<iF7!0#=I5M7PXJS('
        set_0 = {str_0}
        var_0 = module_0.read_user_variable(set_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '.=VXZyV\tgLI&l-y'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        int_0 = -3060
        var_0 = module_0.read_user_yes_no(dict_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = None
        var_0 = module_0.read_repo_password(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "WHmR2w\t'D?4nVMp*3"
        bool_0 = None
        dict_0 = {}
        var_0 = module_0.prompt_choice_for_config(str_0, str_0, bool_0, dict_0, dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        set_0 = set()
        str_0 = 'not found'
        var_0 = module_0.read_user_choice(str_0, set_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -1058.667434
        var_0 = module_0.process_json(float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b',\x85'
        var_0 = module_0.read_user_dict(bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'e#Vw;TG='
        float_0 = 583.4
        set_0 = {float_0, str_0, float_0}
        dict_0 = {float_0: set_0, str_0: set_0}
        var_0 = module_0.render_variable(set_0, dict_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        int_0 = None
        str_0 = '^\n^rAOY{f!i8v!J6T'
        var_0 = module_0.render_variable(int_0, int_0, str_0)
        var_1 = module_0.process_json(bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = -2238.496014
        list_0 = []
        bytes_0 = b'\x8b\xf6\n\xda\x0b\x82\x95\xd2\xd5\xee\x91\xe6\xcb \x0c<'
        var_0 = module_0.prompt_choice_for_config(float_0, list_0, list_0, list_0, bytes_0)
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = -4853.715094
        var_0 = module_0.prompt_for_config(float_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'lCc-eubCR0@Ky}uy'
        bytes_0 = b'ZX'
        dict_0 = None
        list_0 = [str_0, dict_0, str_0, dict_0]
        set_0 = {dict_0, bytes_0, str_0}
        var_0 = module_0.prompt_choice_for_config(bytes_0, dict_0, list_0, set_0, list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bool_0 = False
        list_0 = []
        str_0 = "Stopping generation because %s hook script didn't exit successfully"
        var_0 = module_0.render_variable(bool_0, list_0, str_0)
        var_1 = module_0.process_json(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'CS.'
        list_0 = [str_0, str_0, str_0, str_0]
        var_0 = module_0.render_variable(str_0, list_0, list_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'S51j=\tmO\r'
        dict_0 = {}
        var_0 = module_0.read_user_dict(str_0, dict_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'O'
        float_0 = -430.823
        tuple_0 = ()
        list_0 = [tuple_0, str_0]
        var_0 = module_0.read_user_choice(float_0, list_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'e#]w;TG='
        float_0 = 583.4
        set_0 = {str_0, float_0}
        dict_0 = {}
        var_0 = module_0.render_variable(set_0, dict_0, str_0)
        list_0 = [str_0, str_0, str_0, str_0]
        var_1 = module_0.render_variable(str_0, list_0, list_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '{"test": "string"}'
        str_1 = '["test", "string"]'
        var_0 = module_1.loads(str_0)
        var_1 = module_0.process_json(str_0)
        var_2 = module_1.loads(str_1)
        var_3 = module_0.process_json(str_1)
    except BaseException:
        pass

def test_case_18():
    try:
        bytes_0 = None
        str_0 = None
        str_1 = '{self.message}. Error message: {self.error.message}. Context: {self.context}'
        dict_0 = {str_0: str_0, str_1: bytes_0}
        ordered_dict_0 = module_2.OrderedDict(**dict_0)
        str_2 = 'aATE%e\rf^f.ux\r`Y\nh'
        var_0 = module_0.render_variable(bytes_0, ordered_dict_0, str_2)
    except BaseException:
        pass