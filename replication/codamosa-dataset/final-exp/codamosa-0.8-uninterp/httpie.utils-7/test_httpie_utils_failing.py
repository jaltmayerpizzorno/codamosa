# Automatically generated by Pynguin.
import httpie.utils as module_0

def test_case_0():
    try:
        dict_0 = None
        list_0 = [dict_0]
        float_0 = -4006.172
        dict_1 = {dict_0: list_0, float_0: float_0}
        str_0 = module_0.repr_dict(dict_1)
        list_1 = [dict_1, dict_1, dict_1, dict_1]
        var_0 = module_0.load_json_preserve_order(list_1)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        var_0 = module_0.humanize_bytes(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        var_0 = module_0.humanize_bytes(bool_0)
        list_0 = []
        var_1 = module_0.get_content_type(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'f|'
        float_0 = None
        float_1 = -3064.9188
        var_0 = module_0.humanize_bytes(float_1)
        var_1 = module_0.humanize_bytes(str_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'foo.png'
        var_0 = module_0.get_content_type(str_0)
        str_1 = 'foo.txt'
        var_1 = module_0.get_content_type(str_1)
        str_2 = 'foo.txt.gz'
        var_2 = module_0.get_content_type(str_2)
        list_0 = [var_2, str_0, str_2, str_0]
        var_3 = module_0.get_content_type(list_0)
    except BaseException:
        pass