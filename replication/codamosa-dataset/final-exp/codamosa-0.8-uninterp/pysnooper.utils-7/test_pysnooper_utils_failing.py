# Automatically generated by Pynguin.
import pysnooper.utils as module_0

def test_case_0():
    try:
        var_0 = lambda x: x
        var_1 = lambda x: x
        set_0 = {var_1}
        var_2 = module_0.get_shortish_repr(set_0)
        str_0 = 'works'
        set_1 = None
        dict_0 = None
        var_3 = module_0.truncate(set_1, dict_0)
        var_4 = (var_1, str_0)
        var_5 = [var_4]
        var_6 = module_0.get_shortish_repr(var_0, var_5)
        list_0 = []
        writable_stream_0 = module_0.WritableStream(*list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = lambda x: x
        str_0 = ''
        var_1 = (var_0, str_0)
        var_2 = [var_1]
        var_3 = module_0.get_shortish_repr(var_1, var_2, var_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Td)W9EB'
        var_0 = module_0.ensure_tuple(str_0)
        tuple_0 = ()
        var_1 = module_0.shitcode(tuple_0)
        dict_0 = {}
        int_0 = -1614
        var_2 = module_0.truncate(dict_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'R\x9a\x06\x91\xdb\xef\xa8'
        var_0 = module_0.shitcode(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 467
        str_0 = '_O"wD\x0bJkV'
        var_0 = module_0.get_repr_function(int_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        tuple_0 = None
        bytes_0 = b'ey\x11\xd2h\x05"\x0e\xc8\x95'
        float_0 = -3224.292922075048
        var_0 = module_0.ensure_tuple(float_0)
        set_0 = {bytes_0, tuple_0, tuple_0, tuple_0}
        var_1 = module_0.ensure_tuple(set_0)
        var_2 = module_0.get_repr_function(tuple_0, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'c)'
        var_0 = [str_0]
        var_1 = module_0.get_shortish_repr(str_0, var_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 598
        set_0 = {int_0}
        var_0 = module_0.ensure_tuple(set_0)
        str_0 = '{indent}{newish_string}{name} = {value_repr}'
        var_1 = module_0.shitcode(str_0)
        list_0 = []
        float_0 = 907.59
        var_2 = module_0.truncate(list_0, float_0)
        str_1 = 'JN+1;f-m]l-@WCht'
        var_3 = module_0.get_shortish_repr(list_0, str_1)
    except BaseException:
        pass