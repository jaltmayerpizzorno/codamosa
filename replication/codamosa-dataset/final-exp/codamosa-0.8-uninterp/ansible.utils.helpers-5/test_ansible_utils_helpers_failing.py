# Automatically generated by Pynguin.
import ansible.utils.helpers as module_0

def test_case_0():
    try:
        str_0 = 'DW'
        bool_0 = False
        tuple_0 = None
        var_0 = module_0.pct_to_int(str_0, bool_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'EKQm:3\t`{IB_I17-'
        tuple_0 = (str_0,)
        str_1 = "R\t%A{e!'<ZJ$:>5&xV"
        int_0 = 3237
        var_0 = module_0.pct_to_int(tuple_0, str_1, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'c$'
        float_0 = None
        list_0 = [str_0, float_0]
        int_0 = 165
        tuple_0 = (list_0, int_0)
        float_1 = 1993.0
        var_0 = module_0.object_to_dict(float_1)
        var_1 = module_0.object_to_dict(tuple_0, list_0)
        var_2 = module_0.object_to_dict(tuple_0)
        var_3 = module_0.object_to_dict(int_0)
        var_4 = module_0.object_to_dict(list_0)
        var_5 = module_0.object_to_dict(list_0)
        list_1 = []
        var_6 = module_0.deduplicate_list(var_2)
        var_7 = module_0.pct_to_int(int_0, int_0)
        var_8 = module_0.deduplicate_list(list_1)
        bytes_0 = b'\xdf\xc3\xcd\xd2\xab?'
        var_9 = module_0.object_to_dict(bytes_0, var_6)
        var_10 = module_0.object_to_dict(list_1)
        var_11 = module_0.object_to_dict(tuple_0)
        int_1 = 630
        var_12 = module_0.object_to_dict(tuple_0, int_1)
        float_2 = 48.0
        var_13 = module_0.deduplicate_list(float_2)
    except BaseException:
        pass