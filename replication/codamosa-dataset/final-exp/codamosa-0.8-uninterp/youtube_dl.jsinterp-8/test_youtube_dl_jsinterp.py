# Automatically generated by Pynguin.
import youtube_dl.jsinterp as module_0

def test_case_0():
    pass

def test_case_1():
    set_0 = set()
    j_s_interpreter_0 = module_0.JSInterpreter(set_0)

def test_case_2():
    str_0 = 'b'
    str_1 = 'var b={"a":function(x,y){return x*y}};'
    j_s_interpreter_0 = module_0.JSInterpreter(str_1)
    var_0 = j_s_interpreter_0.extract_object(str_0)

def test_case_3():
    str_0 = '\n    var f = function(x,y) {  \n        return x;\n    }\n    '
    j_s_interpreter_0 = module_0.JSInterpreter(str_0)
    str_1 = 'f'
    var_0 = j_s_interpreter_0.extract_function(str_1)

def test_case_4():
    str_0 = ''
    j_s_interpreter_0 = module_0.JSInterpreter(str_0, str_0)
    int_0 = 100
    str_1 = 'abc*7'
    str_2 = 'abc'
    int_1 = 6
    int_2 = {str_2: int_1}
    var_0 = j_s_interpreter_0.interpret_expression(str_1, int_2, int_0)