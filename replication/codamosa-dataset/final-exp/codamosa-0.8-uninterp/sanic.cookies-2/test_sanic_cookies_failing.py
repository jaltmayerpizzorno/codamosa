# Automatically generated by Pynguin.
import sanic.cookies as module_0

def test_case_0():
    try:
        float_0 = -3514.0
        bytes_0 = b'1\x08\x1du\x0b'
        cookie_jar_0 = module_0.CookieJar(bytes_0)
        var_0 = cookie_jar_0.__delitem__(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'wEcfJ{P{o0E!3W:'
        dict_0 = None
        cookie_jar_0 = module_0.CookieJar(dict_0)
        cookie_0 = module_0.Cookie(str_0, cookie_jar_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'haha'
        cookie_0 = module_0.Cookie(str_0, str_0)
        var_0 = str(cookie_0)
        tuple_0 = ()
        list_0 = [tuple_0, tuple_0, str_0]
        var_1 = cookie_0.__setitem__(tuple_0, list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 87
        cookie_jar_0 = module_0.CookieJar(int_0)
        str_0 = 'Comment'
        var_0 = cookie_jar_0.__delitem__(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = None
        cookie_jar_0 = module_0.CookieJar(str_0)
        cookie_jar_1 = module_0.CookieJar(cookie_jar_0)
        float_0 = -327.953046
        cookie_jar_2 = module_0.CookieJar(float_0)
        str_1 = 'expires'
        var_0 = cookie_jar_0.__delitem__(str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'value'
        cookie_0 = module_0.Cookie(str_0, str_0)
        str_1 = 'path'
        int_0 = -3395
        var_0 = cookie_0.__setitem__(str_1, int_0)
        var_1 = cookie_0.encode(int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'haha'
        str_1 = None
        cookie_0 = module_0.Cookie(str_0, str_1)
        var_0 = str(str_1)
        str_2 = '{NzuP+]Q`x'
        cookie_jar_0 = module_0.CookieJar(str_2)
        bool_0 = False
        float_0 = -3165.1
        set_0 = {str_0}
        var_1 = cookie_0.__str__()
        cookie_jar_1 = module_0.CookieJar(set_0)
        var_2 = cookie_jar_1.__setitem__(bool_0, float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'value2'
        cookie_0 = module_0.Cookie(str_0, str_0)
        str_1 = 'expires'
        int_0 = -3383
        var_0 = cookie_0.__setitem__(str_1, int_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = "|^HAV'plpSqx9FgtN"
        cookie_0 = module_0.Cookie(str_0, str_0)
        str_1 = 'max-age'
        int_0 = -3373
        var_0 = cookie_0.__setitem__(str_1, int_0)
    except BaseException:
        pass