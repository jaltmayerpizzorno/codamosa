# Automatically generated by Pynguin.
import pymonet.immutable_list as module_0
import builtins as module_1

def test_case_0():
    try:
        int_0 = -20
        immutable_list_0 = module_0.ImmutableList(int_0)
        var_0 = immutable_list_0.append(int_0)
        optional_0 = immutable_list_0.find(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = None
        bool_0 = False
        immutable_list_0 = module_0.ImmutableList(bool_0, bool_0)
        var_1 = immutable_list_0.append(var_0)
        list_0 = []
        optional_0 = immutable_list_0.find(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        object_0 = module_1.object()
        var_0 = None
        immutable_list_0 = module_0.ImmutableList()
        var_1 = immutable_list_0.__add__(var_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 0
        immutable_list_0 = module_0.ImmutableList()
        var_0 = immutable_list_0.__len__()
        immutable_list_1 = module_0.ImmutableList(int_0)
        optional_0 = immutable_list_1.find(immutable_list_1)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 1277
        immutable_list_0 = module_0.ImmutableList(int_0)
        var_0 = immutable_list_0.__len__()
        optional_0 = immutable_list_0.find(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 2
        immutable_list_0 = module_0.ImmutableList(int_0)
        immutable_list_1 = module_0.ImmutableList(int_0, immutable_list_0)
        var_0 = immutable_list_1.to_list()
        var_1 = lambda x: x == int_0
        optional_0 = immutable_list_1.find(var_1)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 1266
        immutable_list_0 = module_0.ImmutableList(int_0)
        float_0 = -1292.2
        var_0 = immutable_list_0.unshift(float_0)
        optional_0 = immutable_list_0.find(immutable_list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = ''
        list_0 = [str_0]
        int_0 = -1101
        bytes_0 = b'\xc7]\xbb\xb7[Y\xf5\xc2n\xd5.\xd8'
        immutable_list_0 = module_0.ImmutableList(int_0, bytes_0)
        var_0 = immutable_list_0.map(list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        callable_0 = None
        immutable_list_0 = module_0.ImmutableList()
        var_0 = immutable_list_0.map(callable_0)
    except BaseException:
        pass

def test_case_9():
    try:
        immutable_list_0 = module_0.ImmutableList()
        immutable_list_1 = module_0.ImmutableList()
        str_0 = immutable_list_1.__str__()
        set_0 = set()
        list_0 = [set_0]
        optional_0 = immutable_list_0.find(list_0)
        callable_0 = None
        int_0 = True
        var_0 = immutable_list_1.append(int_0)
        bool_0 = False
        immutable_list_2 = module_0.ImmutableList(var_0, bool_0)
        var_1 = immutable_list_2.filter(callable_0)
    except BaseException:
        pass

def test_case_10():
    try:
        callable_0 = None
        immutable_list_0 = module_0.ImmutableList()
        var_0 = immutable_list_0.filter(callable_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 1
        immutable_list_0 = module_0.ImmutableList(int_0)
        optional_0 = immutable_list_0.find(int_0)
    except BaseException:
        pass

def test_case_12():
    try:
        callable_0 = None
        immutable_list_0 = module_0.ImmutableList()
        optional_0 = immutable_list_0.find(callable_0)
        set_0 = {optional_0}
        immutable_list_1 = module_0.ImmutableList(set_0)
        var_0 = immutable_list_1.filter(callable_0)
    except BaseException:
        pass

def test_case_13():
    try:
        object_0 = module_1.object()
        callable_0 = None
        var_0 = None
        immutable_list_0 = module_0.ImmutableList()
        var_1 = immutable_list_0.reduce(callable_0, var_0)
        str_0 = 'YE0zB\tfi'
        bool_0 = True
        immutable_list_1 = module_0.ImmutableList(str_0, bool_0)
        var_2 = immutable_list_1.reduce(callable_0, var_1)
    except BaseException:
        pass

def test_case_14():
    try:
        optional_0 = None
        immutable_list_0 = module_0.ImmutableList(optional_0)
        list_0 = [immutable_list_0]
        str_0 = 'R2)mE*.<I'
        str_1 = None
        dict_0 = {str_0: str_0, str_0: optional_0, str_1: list_0}
        tuple_0 = (dict_0, immutable_list_0)
        var_0 = immutable_list_0.append(tuple_0)
        callable_0 = None
        var_1 = None
        var_2 = immutable_list_0.reduce(callable_0, var_1)
        bool_0 = False
        immutable_list_1 = module_0.ImmutableList(bool_0)
        var_3 = immutable_list_1.reduce(var_0, var_2)
    except BaseException:
        pass

def test_case_15():
    try:
        int_0 = 2
        immutable_list_0 = module_0.ImmutableList(int_0)
        immutable_list_1 = module_0.ImmutableList(int_0, immutable_list_0)
        var_0 = lambda x: x == int_0
        optional_0 = immutable_list_1.find(var_0)
    except BaseException:
        pass

def test_case_16():
    try:
        int_0 = 1
        set_0 = {int_0, int_0, int_0}
        list_0 = [set_0]
        bool_0 = True
        immutable_list_0 = module_0.ImmutableList(set_0, list_0, bool_0)
        var_0 = immutable_list_0.__len__()
        var_1 = lambda x: x == int_0
        optional_0 = immutable_list_0.find(var_1)
    except BaseException:
        pass