# Automatically generated by Pynguin.
import ansible.module_utils.common.collections as module_0

def test_case_0():
    str_0 = 'At most one input file may be used with the --output option'
    var_0 = module_0.is_sequence(str_0)

def test_case_1():
    immutable_dict_0 = module_0.ImmutableDict()
    immutable_dict_1 = module_0.ImmutableDict()

def test_case_2():
    list_0 = []
    dict_0 = {}
    immutable_dict_0 = module_0.ImmutableDict(**dict_0)
    var_0 = immutable_dict_0.__eq__(list_0)

def test_case_3():
    immutable_dict_0 = module_0.ImmutableDict()
    float_0 = 103.8856
    var_0 = immutable_dict_0.__len__()
    var_1 = immutable_dict_0.__eq__(float_0)
    var_2 = immutable_dict_0.__len__()

def test_case_4():
    str_0 = 'Feb'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.is_iterable(dict_0)