# Automatically generated by Pynguin.
import httpie.utils as module_0

def test_case_0():
    try:
        str_0 = 'cOa4#TfGZ:~NZ'
        var_0 = module_0.load_json_preserve_order(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 1001
        dict_0 = {}
        explicit_null_auth_0 = module_0.ExplicitNullAuth(**dict_0)
        var_0 = explicit_null_auth_0.__call__(int_0)
        var_1 = module_0.humanize_bytes(explicit_null_auth_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = None
        var_0 = module_0.get_content_type(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = None
        list_0 = [tuple_0, tuple_0]
        list_1 = module_0.get_expired_cookies(list_0)
    except BaseException:
        pass