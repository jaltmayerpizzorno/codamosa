# Automatically generated by Pynguin.
import ansible.utils.helpers as module_0

def test_case_0():
    int_0 = -1132
    var_0 = module_0.object_to_dict(int_0)

def test_case_1():
    str_0 = 'BvX/Kb1\x0b1M'
    var_0 = module_0.deduplicate_list(str_0)

def test_case_2():
    str_0 = 'Failed to verify GPG signature of commit/tag "%s"'
    var_0 = module_0.object_to_dict(str_0)
    int_0 = -686
    list_0 = None
    var_1 = module_0.pct_to_int(int_0, list_0)

def test_case_3():
    str_0 = 't}ule'
    list_0 = [str_0, str_0]
    var_0 = module_0.object_to_dict(str_0, list_0)

def test_case_4():
    str_0 = '*PfNl!P)'
    bytes_0 = b'#\xb1h\x9a\xfb\xddCh@y\x89\xfe\xd7?]#\xca'
    float_0 = -244.0
    tuple_0 = (bytes_0,)
    tuple_1 = (bytes_0, float_0, tuple_0, str_0)
    var_0 = module_0.object_to_dict(str_0, tuple_1)

def test_case_5():
    int_0 = 50
    int_1 = 10
    var_0 = module_0.pct_to_int(int_0, int_1)
    str_0 = '10%'
    int_2 = 1000
    var_1 = module_0.pct_to_int(str_0, int_2)
    var_2 = module_0.pct_to_int(int_1, int_2)
    str_1 = '3%'
    var_3 = module_0.pct_to_int(str_1, int_2)