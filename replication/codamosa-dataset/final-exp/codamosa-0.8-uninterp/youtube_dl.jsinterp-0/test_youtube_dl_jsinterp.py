# Automatically generated by Pynguin.
import youtube_dl.jsinterp as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\xbe\xbf'
    j_s_interpreter_0 = module_0.JSInterpreter(bytes_0)

def test_case_2():
    str_0 = '\n        var d = {"a": function(x, y) { return x + y },\n                 "b": function() { return "abc" }};\n            \n    '
    j_s_interpreter_0 = module_0.JSInterpreter(str_0)
    str_1 = 'd'
    var_0 = j_s_interpreter_0.extract_object(str_1)

def test_case_3():
    dict_0 = None
    str_0 = '[\n\nB0F1tMKi.gH\\v'
    tuple_0 = ()
    j_s_interpreter_0 = module_0.JSInterpreter(tuple_0)
    j_s_interpreter_1 = module_0.JSInterpreter(j_s_interpreter_0)
    var_0 = j_s_interpreter_1.build_function(dict_0, str_0)

def test_case_4():
    str_0 = '\t\n;}62D}):'
    set_0 = {str_0, str_0}
    j_s_interpreter_0 = module_0.JSInterpreter(str_0, set_0)