# Automatically generated by Pynguin.
import collections as module_0
import flutils.codecs.b64 as module_1

def test_case_0():
    str_0 = 'LfX~w]aW0vV"Ycd'
    int_0 = -1336
    tuple_0 = (str_0, int_0)
    set_0 = {tuple_0}
    list_0 = [set_0, set_0]
    user_string_0 = module_0.UserString(list_0)
    tuple_1 = module_1.encode(user_string_0)

def test_case_1():
    dict_0 = {}
    bytes_0 = b'\xf2w\xf5\xf2'
    int_0 = -2366
    tuple_0 = (bytes_0, int_0)
    user_string_0 = module_0.UserString(tuple_0)
    tuple_1 = module_1.decode(dict_0, user_string_0)

def test_case_2():
    module_1.register()