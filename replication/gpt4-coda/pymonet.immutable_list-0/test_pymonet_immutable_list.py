# Automatically generated by Pynguin.
import pymonet.immutable_list as module_0
import builtins as module_1

def test_case_0():
    immutable_list_0 = module_0.ImmutableList()

def test_case_1():
    object_0 = module_1.object()
    immutable_list_0 = module_0.ImmutableList()
    bool_0 = immutable_list_0.__eq__(object_0)

def test_case_2():
    immutable_list_0 = module_0.ImmutableList()
    var_0 = immutable_list_0.to_list()
    object_0 = module_1.object()
    immutable_list_1 = module_0.ImmutableList(object_0)
    var_1 = immutable_list_0.__len__()
    str_0 = immutable_list_1.__str__()

def test_case_3():
    int_0 = 2890
    bool_0 = False
    immutable_list_0 = module_0.ImmutableList(bool_0)
    var_0 = immutable_list_0.unshift(int_0)

def test_case_4():
    bool_0 = False
    immutable_list_0 = module_0.ImmutableList(bool_0)
    var_0 = immutable_list_0.to_list()
    immutable_list_1 = module_0.ImmutableList()
    var_1 = immutable_list_0.__len__()

def test_case_5():
    dict_0 = {}
    immutable_list_0 = module_0.ImmutableList()
    bytes_0 = b'~]a\xef\xc3\xdee~i]Q\xaa\x93\xaa'
    var_0 = immutable_list_0.unshift(bytes_0)
    optional_0 = immutable_list_0.find(dict_0)
    object_0 = module_1.object(**dict_0)
    bool_0 = immutable_list_0.__eq__(object_0)
    object_1 = module_1.object()
    var_1 = immutable_list_0.append(object_1)