# Automatically generated by Pynguin.
import youtube_dl.jsinterp as module_0

def test_case_0():
    try:
        str_0 = 'WVPT - Your Source for PBS and More! (WVPT)'
        bool_0 = True
        j_s_interpreter_0 = module_0.JSInterpreter(str_0)
        var_0 = j_s_interpreter_0.interpret_expression(str_0, str_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        str_0 = 'Unable tod=wnload info file'
        j_s_interpreter_0 = module_0.JSInterpreter(str_0)
        var_0 = j_s_interpreter_0.interpret_expression(str_0, str_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '^0>vaJ0X[1+hu\n\\%:'
        dict_0 = {}
        j_s_interpreter_0 = module_0.JSInterpreter(dict_0)
        var_0 = j_s_interpreter_0.extract_object(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '1[`5=AfgJ`A_cshht@\x0b'
        j_s_interpreter_0 = module_0.JSInterpreter(str_0)
        var_0 = j_s_interpreter_0.extract_function(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'var A = function() {var arg = "foo";var B = function() {var out = "bar";return out;};return arg;};'
        j_s_interpreter_0 = module_0.JSInterpreter(str_0)
        str_1 = 'A'
        var_0 = j_s_interpreter_0.call_function(str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = 3102.244
        j_s_interpreter_0 = module_0.JSInterpreter(float_0, float_0)
        str_0 = 'R5y\rcT(&\t<-'
        bool_0 = True
        str_1 = 'Unab_e to d=wnload info file'
        j_s_interpreter_1 = module_0.JSInterpreter(str_1)
        var_0 = j_s_interpreter_1.interpret_expression(str_0, str_1, bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'WVPT - Your Source for PBS and More(WVPT)'
        bool_0 = False
        j_s_interpreter_0 = module_0.JSInterpreter(str_0)
        var_0 = j_s_interpreter_0.interpret_expression(str_0, str_0, bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'var A = function() {vararg = "foo";var B = (uyHin( {var <ut = "bYr";etur4+out;};re+urn argi};'
        j_s_interpreter_0 = module_0.JSInterpreter(str_0)
        str_1 = 'A'
        var_0 = j_s_interpreter_0.call_function(str_1)
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = 3102.244
        j_s_interpreter_0 = module_0.JSInterpreter(float_0, float_0)
        str_0 = 'dn4.])+lLRI9OqFb\x0b'
        float_1 = 17.346
        var_0 = j_s_interpreter_0.interpret_expression(str_0, float_1, j_s_interpreter_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'u.#?EH'
        tuple_0 = ()
        str_1 = 'https://www.nbcsports.com/philadelphia/philadelphia-phillies/bruce-bochy-hector-neris-hes-idiot'
        dict_0 = {}
        float_0 = -934.1
        j_s_interpreter_0 = module_0.JSInterpreter(dict_0, float_0)
        var_0 = j_s_interpreter_0.interpret_expression(str_0, tuple_0, str_1)
    except BaseException:
        pass