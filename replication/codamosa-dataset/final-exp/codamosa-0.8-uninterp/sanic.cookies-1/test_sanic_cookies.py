# Automatically generated by Pynguin.
import sanic.cookies as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'cvalue'
    cookie_0 = module_0.Cookie(str_0, str_0)
    var_0 = str(cookie_0)

def test_case_2():
    bytes_0 = b'\xd3\x165\x0e'
    cookie_jar_0 = module_0.CookieJar(bytes_0)

def test_case_3():
    str_0 = 'name'
    str_1 = 'va+7e?'
    cookie_0 = module_0.Cookie(str_0, str_1)
    var_0 = str(cookie_0)
    var_1 = str(cookie_0)
    var_2 = str(cookie_0)

def test_case_4():
    str_0 = 'value'
    cookie_0 = module_0.Cookie(str_0, str_0)
    str_1 = 'max-age'
    int_0 = 518
    var_0 = cookie_0.__setitem__(str_1, int_0)
    var_1 = cookie_0.__str__()