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
    callable_0 = None
    immutable_list_0 = module_0.ImmutableList()
    str_0 = immutable_list_0.__str__()
    optional_0 = immutable_list_0.find(callable_0)

def test_case_3():
    dict_0 = {}
    tuple_0 = (dict_0, dict_0)
    bool_0 = False
    immutable_list_0 = module_0.ImmutableList(bool_0)
    var_0 = immutable_list_0.unshift(tuple_0)
    immutable_list_1 = module_0.ImmutableList(dict_0, var_0)
    var_1 = immutable_list_1.__len__()

def test_case_4():
    int_0 = 1
    immutable_list_0 = module_0.ImmutableList(int_0)
    immutable_list_1 = module_0.ImmutableList(int_0)
    immutable_list_2 = module_0.ImmutableList(int_0)
    immutable_list_3 = module_0.ImmutableList(int_0, immutable_list_2)
    immutable_list_4 = module_0.ImmutableList(int_0)
    immutable_list_5 = module_0.ImmutableList(int_0, immutable_list_4)
    immutable_list_6 = module_0.ImmutableList(int_0)
    immutable_list_7 = module_0.ImmutableList(int_0)
    immutable_list_8 = module_0.ImmutableList(int_0, immutable_list_7)
    var_0 = immutable_list_6 == immutable_list_4
    var_1 = immutable_list_4 == immutable_list_6
    immutable_list_9 = module_0.ImmutableList(int_0)
    int_1 = 3
    immutable_list_10 = module_0.ImmutableList(int_1)
    immutable_list_11 = module_0.ImmutableList(int_0, immutable_list_10)
    var_2 = immutable_list_9 == immutable_list_11
    immutable_list_12 = module_0.ImmutableList(int_0)
    immutable_list_13 = module_0.ImmutableList(int_0, immutable_list_12)
    var_3 = immutable_list_13 == immutable_list_7

def test_case_5():
    int_0 = 1
    immutable_list_0 = module_0.ImmutableList(int_0)
    immutable_list_1 = module_0.ImmutableList(int_0)
    int_1 = 2
    immutable_list_2 = module_0.ImmutableList(int_1)
    immutable_list_3 = module_0.ImmutableList(int_0, immutable_list_2)
    immutable_list_4 = module_0.ImmutableList(int_1)
    immutable_list_5 = module_0.ImmutableList(int_0)
    immutable_list_6 = module_0.ImmutableList(int_1)
    immutable_list_7 = module_0.ImmutableList(int_0, immutable_list_6)
    var_0 = immutable_list_5 == immutable_list_7
    immutable_list_8 = module_0.ImmutableList(int_0)
    immutable_list_9 = module_0.ImmutableList(int_1)
    var_1 = immutable_list_8 == immutable_list_9
    immutable_list_10 = module_0.ImmutableList(int_0)
    immutable_list_11 = module_0.ImmutableList(int_1)
    immutable_list_12 = module_0.ImmutableList(int_1, immutable_list_11)
    var_2 = immutable_list_10 == immutable_list_12
    immutable_list_13 = module_0.ImmutableList(int_1)
    immutable_list_14 = module_0.ImmutableList(int_0, immutable_list_13)
    immutable_list_15 = module_0.ImmutableList(int_0)
    var_3 = immutable_list_14 == immutable_list_15