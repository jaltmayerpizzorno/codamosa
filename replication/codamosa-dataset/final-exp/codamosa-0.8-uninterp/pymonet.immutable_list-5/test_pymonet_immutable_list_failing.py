# Automatically generated by Pynguin.
import pymonet.immutable_list as module_0
import builtins as module_1

def test_case_0():
    try:
        bool_0 = True
        int_0 = True
        str_0 = 'RUkN-F4'
        dict_0 = {str_0: str_0}
        set_0 = {bool_0, int_0, bool_0, int_0}
        immutable_list_0 = module_0.ImmutableList(set_0, bool_0)
        var_0 = immutable_list_0.append(dict_0)
        tuple_0 = (int_0,)
        immutable_list_1 = module_0.ImmutableList(bool_0)
        object_0 = module_1.object()
        immutable_list_2 = module_0.ImmutableList(immutable_list_1, object_0)
        var_1 = immutable_list_2.filter(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        object_0 = module_1.object()
        bytes_0 = b'\xa4\xd2\x92\xd9T\xfeq\xbb\xfa\x16i\xbd\xfaN7\xa4\xf3\x93'
        immutable_list_0 = module_0.ImmutableList(bytes_0)
        bool_0 = immutable_list_0.__eq__(object_0)
        var_0 = None
        var_1 = immutable_list_0.__add__(var_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\n        :param semigroup: other semigroup to concat\n        :type semigroup: Last[B]\n        :returns: new Last with last value\n        :rtype: Last[A]\n        '
        bool_0 = True
        immutable_list_0 = module_0.ImmutableList(str_0, bool_0)
        var_0 = immutable_list_0.__len__()
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        immutable_list_0 = module_0.ImmutableList(bool_0)
        var_0 = immutable_list_0.__len__()
        object_0 = module_1.object()
        var_1 = None
        var_2 = immutable_list_0.reduce(object_0, var_1)
    except BaseException:
        pass

def test_case_4():
    try:
        none_type_0 = None
        bytes_0 = b'+f\x1d\xce\xca\xc8O\xaf\xf2\x04\x86Z\xdb)\x07S\xcc\xc0'
        immutable_list_0 = module_0.ImmutableList()
        str_0 = immutable_list_0.__str__()
        var_0 = immutable_list_0.append(bytes_0)
        var_1 = None
        complex_0 = None
        callable_0 = None
        var_2 = None
        var_3 = immutable_list_0.reduce(callable_0, var_2)
        immutable_list_1 = module_0.ImmutableList()
        var_4 = immutable_list_1.reduce(complex_0, var_3)
        var_5 = immutable_list_0.unshift(var_1)
        immutable_list_2 = module_0.ImmutableList(none_type_0, var_0)
        object_0 = module_1.object()
        optional_0 = immutable_list_2.find(object_0)
        immutable_list_3 = module_0.ImmutableList(var_0)
        bool_0 = immutable_list_2.__eq__(object_0)
        var_6 = immutable_list_3.to_list()
        str_1 = immutable_list_2.__str__()
        list_0 = [var_0]
        immutable_list_4 = module_0.ImmutableList(var_1)
        var_7 = immutable_list_4.filter(list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        immutable_list_0 = module_0.ImmutableList()
        callable_0 = None
        var_0 = None
        immutable_list_1 = module_0.ImmutableList()
        var_1 = immutable_list_1.append(var_0)
        optional_0 = immutable_list_0.find(callable_0)
        var_2 = immutable_list_0.filter(callable_0)
    except BaseException:
        pass

def test_case_6():
    try:
        var_0 = None
        bytes_0 = b'n\x97~Z\x14u4\x9e\xccQT\x81Q\xb8'
        bool_0 = False
        immutable_list_0 = module_0.ImmutableList(bytes_0, bool_0)
        var_1 = immutable_list_0.map(var_0)
    except BaseException:
        pass

def test_case_7():
    try:
        list_0 = []
        immutable_list_0 = module_0.ImmutableList()
        var_0 = immutable_list_0.map(list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        callable_0 = None
        int_0 = -1660
        bool_0 = True
        immutable_list_0 = module_0.ImmutableList(int_0, bool_0)
        var_0 = immutable_list_0.filter(callable_0)
    except BaseException:
        pass

def test_case_9():
    try:
        immutable_list_0 = module_0.ImmutableList()
        callable_0 = None
        var_0 = immutable_list_0.filter(callable_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = False
        immutable_list_0 = module_0.ImmutableList(bool_0)
        optional_0 = immutable_list_0.find(bool_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 1
        int_1 = 2
        immutable_list_0 = module_0.ImmutableList(int_1)
        int_2 = 3
        immutable_list_1 = module_0.ImmutableList(int_2)
        immutable_list_2 = module_0.ImmutableList(int_0, immutable_list_0, immutable_list_1)
        int_3 = 0
        var_0 = immutable_list_2.reduce(int_2, int_3)
    except BaseException:
        pass

def test_case_12():
    try:
        object_0 = module_1.object()
        bool_0 = False
        immutable_list_0 = module_0.ImmutableList(object_0, bool_0)
        optional_0 = immutable_list_0.find(object_0)
    except BaseException:
        pass

def test_case_13():
    try:
        immutable_list_0 = module_0.ImmutableList()
        var_0 = lambda x: x
        var_1 = lambda x: not x
        int_0 = 2
        immutable_list_1 = module_0.ImmutableList(int_0)
        immutable_list_2 = module_0.ImmutableList(int_0, immutable_list_1)
        callable_0 = None
        immutable_list_3 = module_0.ImmutableList(int_0)
        immutable_list_4 = module_0.ImmutableList(int_0, immutable_list_1)
        var_2 = immutable_list_4.filter(var_0)
        object_0 = None
        bool_0 = immutable_list_2.__eq__(object_0)
        optional_0 = immutable_list_3.find(callable_0)
    except BaseException:
        pass

def test_case_14():
    try:
        immutable_list_0 = module_0.ImmutableList()
        var_0 = lambda x: x
        var_1 = immutable_list_0.filter(var_0)
        var_2 = lambda x: not x
        var_3 = lambda x: x
        int_0 = 2
        immutable_list_1 = module_0.ImmutableList(int_0)
        immutable_list_2 = module_0.ImmutableList(int_0, immutable_list_1)
        immutable_list_3 = module_0.ImmutableList(int_0)
        immutable_list_4 = module_0.ImmutableList(int_0)
        immutable_list_5 = module_0.ImmutableList(int_0, immutable_list_4)
        immutable_list_6 = module_0.ImmutableList(int_0, immutable_list_5)
        var_4 = lambda x: x > int_0
        var_5 = immutable_list_6.filter(var_4)
    except BaseException:
        pass

def test_case_15():
    try:
        immutable_list_0 = module_0.ImmutableList()
        var_0 = lambda x: x
        var_1 = immutable_list_0.filter(var_0)
        var_2 = lambda x: not x
        int_0 = 0
        immutable_list_1 = module_0.ImmutableList(int_0)
        immutable_list_2 = module_0.ImmutableList(int_0, immutable_list_1)
        var_3 = lambda x: x > int_0
        callable_0 = None
        immutable_list_3 = module_0.ImmutableList(int_0)
        immutable_list_4 = module_0.ImmutableList(int_0, immutable_list_3)
        immutable_list_5 = module_0.ImmutableList(int_0, immutable_list_4)
        var_4 = immutable_list_5.filter(var_0)
        optional_0 = immutable_list_3.find(callable_0)
    except BaseException:
        pass