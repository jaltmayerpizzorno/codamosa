# Automatically generated by Pynguin.
import youtube_dl.jsinterp as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = ')J)*Gwc'
    j_s_interpreter_0 = module_0.JSInterpreter(str_0)

def test_case_2():
    str_0 = '\n    var f = function(a,b) {\n        return a*b;\n    }\n    \n    var g = function(c) {\n        return c + 100;\n    }\n    \n    var h = function() {\n        return 5 + 10;\n    }\n    '
    j_s_interpreter_0 = module_0.JSInterpreter(str_0)
    str_1 = 'h'
    var_0 = j_s_interpreter_0.call_function(str_1)

def test_case_3():
    tuple_0 = ()
    str_0 = 'ta'
    str_1 = ''
    str_2 = None
    set_0 = set()
    j_s_interpreter_0 = module_0.JSInterpreter(set_0)
    var_0 = j_s_interpreter_0.interpret_statement(str_1, str_2)
    bytes_0 = b'\x0e*\xb9\xbc\xa6\x7f&,\xee\x8a\xf0\xd3C\xa3\xc09*\xa3\xbe'
    dict_0 = {str_0: bytes_0}
    j_s_interpreter_1 = module_0.JSInterpreter(dict_0)
    j_s_interpreter_2 = module_0.JSInterpreter(tuple_0)