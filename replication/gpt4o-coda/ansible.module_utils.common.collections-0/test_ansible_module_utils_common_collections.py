# Automatically generated by Pynguin.
import ansible.module_utils.common.collections as module_0

def test_case_0():
    immutable_dict_0 = module_0.ImmutableDict()
    var_0 = immutable_dict_0.__repr__()

def test_case_1():
    dict_0 = {}
    immutable_dict_0 = module_0.ImmutableDict()
    var_0 = immutable_dict_0.__eq__(dict_0)

def test_case_2():
    immutable_dict_0 = module_0.ImmutableDict()
    immutable_dict_1 = module_0.ImmutableDict()
    var_0 = immutable_dict_1.__eq__(immutable_dict_0)
    str_0 = 'op2o$%)\nDu@N9hwzWGg'
    str_1 = ''
    dict_0 = {str_1: str_1, str_1: str_1, str_1: str_1, str_1: str_1}
    immutable_dict_2 = module_0.ImmutableDict(**dict_0)
    var_1 = immutable_dict_2.difference(str_0)

def test_case_3():
    str_0 = 'A%Y\t`[yl,8_&,^>D6C'
    var_0 = module_0.is_iterable(str_0)
    dict_0 = {}
    var_1 = module_0.count(dict_0)
    immutable_dict_0 = module_0.ImmutableDict(**dict_0)

def test_case_4():
    float_0 = 1963.0
    list_0 = None
    tuple_0 = (float_0, list_0)
    list_1 = [tuple_0, tuple_0]
    var_0 = module_0.is_sequence(list_1)

def test_case_5():
    immutable_dict_0 = module_0.ImmutableDict()
    str_0 = '^!^#\r(\t_,'
    tuple_0 = (immutable_dict_0, immutable_dict_0, str_0)
    var_0 = immutable_dict_0.__eq__(tuple_0)
    var_1 = immutable_dict_0.__repr__()