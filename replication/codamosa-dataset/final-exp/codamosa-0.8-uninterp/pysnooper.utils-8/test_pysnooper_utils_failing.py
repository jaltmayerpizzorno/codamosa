# Automatically generated by Pynguin.
import pysnooper.utils as module_0

def test_case_0():
    try:
        list_0 = []
        list_1 = [list_0, list_0, list_0, list_0]
        var_0 = module_0.get_shortish_repr(list_1)
        str_0 = ' W'
        var_1 = module_0.shitcode(str_0)
        writable_stream_0 = module_0.WritableStream(*list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        str_0 = ']2\tpBxAr8;@J.'
        float_0 = 1779.578408
        var_0 = module_0.truncate(str_0, float_0)
        list_1 = [list_0, list_0]
        var_1 = module_0.get_shortish_repr(list_1)
        str_1 = '\x0c'
        var_2 = module_0.normalize_repr(str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = set()
        list_0 = [set_0, set_0, set_0]
        var_0 = module_0.truncate(set_0, list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\n'
        dict_0 = {str_0: str_0, str_0: str_0}
        float_0 = None
        tuple_0 = (dict_0, float_0)
        var_0 = module_0.ensure_tuple(tuple_0)
        str_1 = 'zPh+Z"G'
        str_2 = 'PathLike'
        dict_1 = {str_1: float_0, str_2: tuple_0}
        writable_stream_0 = module_0.WritableStream(**dict_1)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 9
        var_0 = (int_0, int_0)
        var_1 = (var_0,)
        var_2 = module_0.get_repr_function(int_0, var_1)
    except BaseException:
        pass

def test_case_5():
    try:
        list_0 = []
        list_1 = [list_0, list_0, list_0, list_0]
        var_0 = module_0.get_shortish_repr(list_1)
        str_0 = '/'
        var_1 = module_0.shitcode(str_0)
        bool_0 = False
        str_1 = None
        var_2 = module_0.truncate(bool_0, str_1)
        dict_0 = {str_0: var_1}
        var_3 = module_0.truncate(list_0, dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        list_0 = []
        list_1 = [list_0, list_0]
        str_0 = 'q5c%~C\x0c`{"RD^'
        str_1 = None
        var_0 = module_0.ensure_tuple(str_1)
        var_1 = module_0.get_shortish_repr(list_1)
        var_2 = module_0.shitcode(str_0)
        bool_0 = True
        var_3 = module_0.normalize_repr(bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = ")'Wbkti<.!"
        dict_0 = {str_0: str_0, str_0: str_0}
        list_0 = []
        tuple_0 = (dict_0,)
        tuple_1 = (tuple_0,)
        var_0 = module_0.get_shortish_repr(dict_0, list_0, tuple_1)
    except BaseException:
        pass

def test_case_8():
    try:
        list_0 = []
        str_0 = '{indent}Elapsed time: {elapsed_time_string}'
        list_1 = [str_0, list_0, str_0, str_0]
        float_0 = -3091.0
        var_0 = module_0.truncate(list_1, float_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'V\ta!H(`+bn@ '
        var_0 = module_0.shitcode(str_0)
        int_0 = -18
        str_1 = ''
        var_1 = module_0.get_shortish_repr(str_1)
        var_2 = lambda x: str(x) * int_0
        int_1 = 38
        var_3 = lambda x: x > int_1
        var_4 = lambda x: str(x) * int_1
        int_2 = 144
        float_0 = -2508.5
        dict_0 = {var_2: var_4}
        var_5 = module_0.get_shortish_repr(int_2, str_1, float_0, dict_0)
    except BaseException:
        pass