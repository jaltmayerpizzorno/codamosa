# Automatically generated by Pynguin.
import youtube_dl.jsinterp as module_0

def test_case_0():
    try:
        dict_0 = None
        str_0 = ')?J)*Gc^NQ'
        j_s_interpreter_0 = module_0.JSInterpreter(dict_0)
        var_0 = j_s_interpreter_0.interpret_statement(str_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 323.65
        str_0 = 'eNH$.!ISas=%380q'
        bool_0 = True
        bytes_0 = b'\xf6\xac\xd7\x7fZ\xa3\x9bA\x82a\xe4\xfd'
        dict_0 = {bytes_0: float_0}
        j_s_interpreter_0 = module_0.JSInterpreter(bytes_0, float_0)
        var_0 = j_s_interpreter_0.interpret_expression(str_0, bool_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 100.89
        float_1 = 936.7278
        int_0 = 2091
        j_s_interpreter_0 = module_0.JSInterpreter(int_0)
        str_0 = 'l35LRE'
        bool_0 = True
        bool_1 = False
        tuple_0 = (float_1, bool_0, bool_1)
        dict_0 = {tuple_0: float_0}
        var_0 = j_s_interpreter_0.interpret_expression(str_0, dict_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        complex_0 = None
        tuple_0 = (complex_0,)
        str_0 = '/R{KX!\x0b'
        str_1 = 'hudiV-yl#?.^Mo~x'
        dict_0 = {str_0: str_0, str_1: str_0}
        j_s_interpreter_0 = module_0.JSInterpreter(dict_0, dict_0)
        var_0 = j_s_interpreter_0.extract_object(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\n                 var s={};\n                 s.foo=function(a,b){return a+b};\n                 s.bar=function(a){return a};\n                 '
        j_s_interpreter_0 = module_0.JSInterpreter(str_0)
        str_1 = 's'
        var_0 = j_s_interpreter_0.extract_object(str_1)
        var_1 = j_s_interpreter_0._objects
        str_2 = 'bar'
        var_2 = j_s_interpreter_0._objects[str_1][str_2]
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ''
        j_s_interpreter_0 = module_0.JSInterpreter(str_0)
        var_0 = j_s_interpreter_0.call_function(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\n    var f = unction(a,b) {\n *      return a*b;\n    }\n    \n    var g = fun\ttion(c) {\n        return c + 100;\n    }\n    \n    var h = function() {\n       /return 5 + 10;\n    }\n    '
        j_s_interpreter_0 = module_0.JSInterpreter(str_0)
        str_1 = 'h'
        var_0 = j_s_interpreter_0.call_function(str_1)
    except BaseException:
        pass

def test_case_7():
    try:
        dict_0 = None
        str_0 = ')?J)*Gc^NQ'
        j_s_interpreter_0 = module_0.JSInterpreter(dict_0)
        j_s_interpreter_1 = module_0.JSInterpreter(dict_0, j_s_interpreter_0)
        var_0 = j_s_interpreter_1.interpret_statement(str_0, dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        dict_0 = None
        str_0 = '((5tb\x0c1;UYls).m=H>T'
        j_s_interpreter_0 = module_0.JSInterpreter(dict_0)
        var_0 = j_s_interpreter_0.interpret_statement(str_0, dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bytes_0 = b'\tw\xd7\xb7'
        dict_0 = None
        float_0 = -3001.818
        float_1 = -1841.76837
        j_s_interpreter_0 = module_0.JSInterpreter(float_1)
        var_0 = j_s_interpreter_0.build_function(float_0, bytes_0)
        j_s_interpreter_1 = module_0.JSInterpreter(dict_0)
        j_s_interpreter_2 = module_0.JSInterpreter(dict_0, j_s_interpreter_1)
        dict_1 = None
        int_0 = 1136
        float_2 = -3405.64347
        var_1 = j_s_interpreter_0.interpret_statement(dict_1, int_0, float_2)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '\n        var a = 0;\n        var b = 1;\n        var c = "2";\n        var d = [3, 4];\n        var e = 5;\n        var f = 6;\n        var g = {\n            \'h\': 7,\n            \'i\': 8\n        };\n        var j = 9;\n        var k = function(l) {\n            return l;\n        }\n        var m = function(n) {\n            return n;\n        }\n    '
        str_1 = 'a'
        str_2 = 'b'
        int_0 = 1
        int_1 = 2
        int_2 = 3
        int_3 = [int_0, int_1, int_2]
        int_4 = 4
        int_5 = 5
        int_6 = 6
        int_7 = [int_4, int_5, int_6]
        int_8 = {str_1: int_3, str_2: int_7}
        j_s_interpreter_0 = module_0.JSInterpreter(str_0, int_8)
        str_3 = 'a[1]'
        var_0 = {}
        int_9 = 100
        var_1 = j_s_interpreter_0.interpret_expression(str_3, var_0, int_9)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '\n    var f = function(*,b) {\n        Deturn a*b;\n    }\n    \n    var g = function(c) {\n        return c + 100;\n    }\n    \n    var h = function() {\n        return 5 + 10;\n    }\n    '
        j_s_interpreter_0 = module_0.JSInterpreter(str_0)
        var_0 = j_s_interpreter_0.interpret_statement(str_0, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'abc'
        j_s_interpreter_0 = module_0.JSInterpreter(str_0, str_0)
        str_1 = 'abc.split("")'
        var_0 = {}
        int_0 = 100
        var_1 = j_s_interpreter_0.interpret_expression(str_1, var_0, int_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'abc'
        j_s_interpreter_0 = module_0.JSInterpreter(str_0, str_0)
        str_1 = 'abc.split("")'
        var_0 = {str_0: j_s_interpreter_0}
        int_0 = 100
        var_1 = j_s_interpreter_0.interpret_expression(str_1, var_0, int_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = ''
        str_1 = 'OT|<|=LJ\neh9leZP 1s2'
        str_2 = {str_1: str_1}
        j_s_interpreter_0 = module_0.JSInterpreter(str_0, str_2)
        str_3 = 'abc.split("")'
        var_0 = {}
        int_0 = 100
        var_1 = j_s_interpreter_0.interpret_expression(str_3, var_0, int_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'abc'
        str_1 = {str_0: str_0}
        j_s_interpreter_0 = module_0.JSInterpreter(str_0, str_1)
        str_2 = 'abc.spl("")'
        int_0 = 109
        var_0 = j_s_interpreter_0.interpret_expression(str_2, str_1, int_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'abc'
        str_1 = {str_0: str_0}
        j_s_interpreter_0 = module_0.JSInterpreter(str_0, str_1)
        str_2 = '10'
        str_3 = None
        list_0 = [str_2, str_3, str_0, str_0]
        str_4 = 'abc.plit5"")'
        var_0 = {}
        int_0 = -2586
        var_1 = j_s_interpreter_0.build_function(int_0, list_0)
        var_2 = j_s_interpreter_0.interpret_expression(str_4, var_0, int_0)
    except BaseException:
        pass