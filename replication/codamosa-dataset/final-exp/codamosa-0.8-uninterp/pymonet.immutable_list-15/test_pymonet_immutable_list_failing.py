# Automatically generated by Pynguin.
import pymonet.immutable_list as module_0
import builtins as module_1

def test_case_0():
    try:
        bytes_0 = b'l'
        immutable_list_0 = module_0.ImmutableList(bytes_0, bytes_0)
        var_0 = immutable_list_0.to_list()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        immutable_list_0 = module_0.ImmutableList(bool_0)
        var_0 = None
        str_0 = immutable_list_0.__str__()
        var_1 = immutable_list_0.append(var_0)
        var_2 = immutable_list_0.unshift(var_0)
        var_3 = immutable_list_0.filter(immutable_list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        immutable_list_0 = module_0.ImmutableList(bool_0)
        var_0 = immutable_list_0.to_list()
        float_0 = 1125.04945
        immutable_list_1 = module_0.ImmutableList()
        optional_0 = immutable_list_1.find(float_0)
        var_1 = None
        bool_1 = True
        immutable_list_2 = module_0.ImmutableList()
        var_2 = immutable_list_2.append(bool_1)
        var_3 = immutable_list_2.__add__(var_2)
        bool_2 = True
        var_4 = immutable_list_1.to_list()
        var_5 = immutable_list_2.unshift(var_1)
        var_6 = immutable_list_2.to_list()
        immutable_list_3 = module_0.ImmutableList(var_2, bool_2)
        var_7 = immutable_list_2.__add__(var_5)
        callable_0 = None
        var_8 = immutable_list_3.map(callable_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        immutable_list_0 = module_0.ImmutableList(bool_0)
        var_0 = immutable_list_0.to_list()
        var_1 = None
        var_2 = immutable_list_0.map(var_1)
    except BaseException:
        pass

def test_case_4():
    try:
        object_0 = module_1.object()
        callable_0 = None
        list_0 = [object_0, object_0, object_0]
        bool_0 = False
        immutable_list_0 = module_0.ImmutableList(list_0, bool_0)
        var_0 = immutable_list_0.filter(callable_0)
    except BaseException:
        pass

def test_case_5():
    try:
        immutable_list_0 = module_0.ImmutableList()
        var_0 = immutable_list_0.filter(immutable_list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = 2960.6825
        bool_0 = True
        immutable_list_0 = module_0.ImmutableList(bool_0)
        optional_0 = immutable_list_0.find(float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        callable_0 = None
        immutable_list_0 = None
        tuple_0 = (immutable_list_0,)
        bool_0 = False
        immutable_list_1 = module_0.ImmutableList(tuple_0, bool_0)
        optional_0 = immutable_list_1.find(callable_0)
    except BaseException:
        pass

def test_case_8():
    try:
        immutable_list_0 = module_0.ImmutableList()
        var_0 = immutable_list_0.__len__()
        bool_0 = True
        immutable_list_1 = module_0.ImmutableList(bool_0)
        immutable_list_2 = module_0.ImmutableList()
        var_1 = immutable_list_2.to_list()
        var_2 = immutable_list_2.unshift(immutable_list_2)
        callable_0 = None
        var_3 = None
        var_4 = immutable_list_2.reduce(callable_0, var_3)
        var_5 = immutable_list_0.reduce(callable_0, var_4)
        var_6 = immutable_list_0.reduce(callable_0, var_5)
        var_7 = immutable_list_1.reduce(callable_0, var_6)
    except BaseException:
        pass

def test_case_9():
    try:
        var_0 = None
        immutable_list_0 = module_0.ImmutableList()
        var_1 = immutable_list_0.__add__(var_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = True
        immutable_list_0 = module_0.ImmutableList(bool_0)
        var_0 = immutable_list_0.to_list()
        float_0 = 1125.04945
        str_0 = '5`yFD)dxd<\'M"9Ng'
        var_1 = immutable_list_0.unshift(str_0)
        immutable_list_1 = module_0.ImmutableList()
        optional_0 = immutable_list_1.find(float_0)
        var_2 = None
        bool_1 = True
        immutable_list_2 = module_0.ImmutableList()
        var_3 = immutable_list_2.append(bool_1)
        bool_2 = True
        var_4 = immutable_list_2.unshift(var_2)
        var_5 = immutable_list_2.to_list()
        immutable_list_3 = module_0.ImmutableList(var_3, bool_2)
        var_6 = immutable_list_2.__add__(var_4)
        callable_0 = None
        var_7 = None
        var_8 = immutable_list_3.reduce(callable_0, var_7)
    except BaseException:
        pass

def test_case_11():
    try:
        var_0 = lambda x: x
        int_0 = 1
        immutable_list_0 = module_0.ImmutableList(int_0)
        var_1 = lambda x: x
        var_2 = immutable_list_0.filter(var_1)
        immutable_list_1 = module_0.ImmutableList(int_0)
        var_3 = lambda x: not x
        var_4 = immutable_list_1.filter(var_3)
        int_1 = 2
        immutable_list_2 = module_0.ImmutableList(int_1)
        immutable_list_3 = module_0.ImmutableList(int_0, immutable_list_2)
        var_5 = lambda x: x == int_0
        immutable_list_4 = module_0.ImmutableList(int_0)
        immutable_list_5 = module_0.ImmutableList(int_0, int_1)
        var_6 = lambda x: x
        var_7 = immutable_list_5.filter(var_6)
    except BaseException:
        pass

def test_case_12():
    try:
        var_0 = lambda x: x
        int_0 = 1
        var_1 = lambda x: x
        immutable_list_0 = module_0.ImmutableList(int_0)
        var_2 = lambda x: not x
        var_3 = immutable_list_0.filter(var_2)
        int_1 = 2
        immutable_list_1 = module_0.ImmutableList(int_1)
        var_4 = lambda x: x == int_0
        immutable_list_2 = module_0.ImmutableList(int_0)
        immutable_list_3 = module_0.ImmutableList(int_0, int_1)
        var_5 = lambda x: x
        var_6 = immutable_list_3.filter(var_5)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'E&]^(.'
        immutable_list_0 = module_0.ImmutableList(str_0)
        tuple_0 = None
        immutable_list_1 = module_0.ImmutableList()
        optional_0 = immutable_list_1.find(tuple_0)
        var_0 = immutable_list_0.to_list()
        var_1 = lambda x: x
        var_2 = lambda x: not x
        int_0 = 2
        immutable_list_2 = module_0.ImmutableList(int_0)
        immutable_list_3 = module_0.ImmutableList(int_0, immutable_list_2)
        var_3 = lambda x: x == int_0
        var_4 = lambda x: x
        immutable_list_4 = module_0.ImmutableList(int_0, int_0)
        immutable_list_5 = module_0.ImmutableList(int_0, int_0)
        var_5 = lambda x: not x
        var_6 = immutable_list_5.filter(var_5)
    except BaseException:
        pass