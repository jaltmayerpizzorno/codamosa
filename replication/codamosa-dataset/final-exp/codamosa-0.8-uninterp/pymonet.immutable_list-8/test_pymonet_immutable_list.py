# Automatically generated by Pynguin.
import pymonet.immutable_list as module_0
import builtins as module_1

def test_case_0():
    immutable_list_0 = module_0.ImmutableList()

def test_case_1():
    object_0 = None
    immutable_list_0 = module_0.ImmutableList()
    bool_0 = immutable_list_0.__eq__(object_0)

def test_case_2():
    immutable_list_0 = module_0.ImmutableList()
    str_0 = immutable_list_0.__str__()

def test_case_3():
    list_0 = None
    immutable_list_0 = module_0.ImmutableList()
    object_0 = module_1.object()
    var_0 = None
    var_1 = immutable_list_0.reduce(object_0, var_0)
    var_2 = immutable_list_0.append(var_1)
    var_3 = immutable_list_0.__add__(var_2)
    var_4 = immutable_list_0.append(list_0)

def test_case_4():
    int_0 = 1
    int_1 = 2
    int_2 = 3
    int_3 = [int_0, int_1, int_2]
    immutable_list_0 = module_0.ImmutableList(int_3)
    int_4 = [int_0, int_1, int_2]
    immutable_list_1 = module_0.ImmutableList(int_4)
    bool_0 = immutable_list_0.__eq__(immutable_list_1)
    int_5 = [int_0, int_1, int_2]
    immutable_list_2 = module_0.ImmutableList(int_5)
    int_6 = 5
    int_7 = [int_0, int_1, int_6]
    immutable_list_3 = module_0.ImmutableList(int_7)
    bool_1 = immutable_list_2.__eq__(immutable_list_3)
    int_8 = [int_0, int_1, int_2]
    immutable_list_4 = module_0.ImmutableList(int_8)
    int_9 = 7
    immutable_list_5 = module_0.ImmutableList(int_9)
    bool_2 = immutable_list_4.__eq__(immutable_list_5)

def test_case_5():
    int_0 = 1
    immutable_list_0 = module_0.ImmutableList(int_0)
    immutable_list_1 = module_0.ImmutableList(int_0)
    immutable_list_2 = module_0.ImmutableList(int_0)
    immutable_list_3 = module_0.ImmutableList(int_0)
    bool_0 = immutable_list_2.__eq__(immutable_list_3)
    int_1 = 2
    immutable_list_4 = module_0.ImmutableList(int_1)
    immutable_list_5 = module_0.ImmutableList(int_0, immutable_list_4)
    immutable_list_6 = module_0.ImmutableList(int_1)
    immutable_list_7 = module_0.ImmutableList(int_0, immutable_list_6)
    int_2 = 3
    immutable_list_8 = module_0.ImmutableList(int_2)
    immutable_list_9 = module_0.ImmutableList(int_1, immutable_list_8)
    immutable_list_10 = module_0.ImmutableList(int_0, immutable_list_9)
    immutable_list_11 = module_0.ImmutableList(int_2)
    immutable_list_12 = module_0.ImmutableList(int_1, immutable_list_11)
    immutable_list_13 = module_0.ImmutableList(int_0, immutable_list_12)
    immutable_list_14 = module_0.ImmutableList(int_1)
    immutable_list_15 = module_0.ImmutableList(int_0, immutable_list_14)
    immutable_list_16 = module_0.ImmutableList(int_2)
    immutable_list_17 = module_0.ImmutableList(int_0, immutable_list_16)
    immutable_list_18 = module_0.ImmutableList(int_0)
    immutable_list_19 = module_0.ImmutableList(int_1)
    immutable_list_20 = module_0.ImmutableList(int_1)
    immutable_list_21 = module_0.ImmutableList(int_0, immutable_list_20)
    immutable_list_22 = module_0.ImmutableList(int_2)
    immutable_list_23 = module_0.ImmutableList(int_0, immutable_list_22)
    bool_1 = immutable_list_21.__eq__(immutable_list_23)
    immutable_list_24 = module_0.ImmutableList(int_0)
    immutable_list_25 = module_0.ImmutableList(int_1)
    bool_2 = immutable_list_24.__eq__(immutable_list_25)