# Automatically generated by Pynguin.
import ansible.module_utils.common.collections as module_0

def test_case_0():
    immutable_dict_0 = module_0.ImmutableDict()
    var_0 = immutable_dict_0.__len__()

def test_case_1():
    immutable_dict_0 = module_0.ImmutableDict()
    immutable_dict_1 = module_0.ImmutableDict()
    var_0 = immutable_dict_1.__hash__()

def test_case_2():
    list_0 = []
    immutable_dict_0 = module_0.ImmutableDict()
    var_0 = immutable_dict_0.__eq__(list_0)

def test_case_3():
    list_0 = []
    immutable_dict_0 = module_0.ImmutableDict(*list_0)
    var_0 = immutable_dict_0.difference(list_0)
    var_1 = immutable_dict_0.__repr__()

def test_case_4():
    float_0 = -1665.54
    var_0 = module_0.is_iterable(float_0)

def test_case_5():
    str_0 = 'u3[L$QB?`lKt{'
    immutable_dict_0 = module_0.ImmutableDict()
    var_0 = immutable_dict_0.__repr__()
    str_1 = None
    immutable_dict_1 = module_0.ImmutableDict()
    str_2 = 'R3oKXGDNz/yqr'
    str_3 = '>w;+Cy>_gu*'
    var_1 = immutable_dict_0.__eq__(str_3)
    dict_0 = {str_0: str_0, str_1: str_0, str_2: str_0}
    var_2 = module_0.is_iterable(dict_0)

def test_case_6():
    immutable_dict_0 = module_0.ImmutableDict()
    var_0 = immutable_dict_0.__repr__()
    str_0 = 'rH:c"n2O%<7{}7\x0b'
    var_1 = module_0.is_sequence(str_0, immutable_dict_0)
    float_0 = 0.2
    var_2 = module_0.is_iterable(float_0)
    var_3 = immutable_dict_0.__iter__()

def test_case_7():
    float_0 = -858.327
    immutable_dict_0 = module_0.ImmutableDict()
    var_0 = immutable_dict_0.__repr__()
    str_0 = '7<s&_=u(<HB$3;Y'
    dict_0 = {str_0: str_0}
    immutable_dict_1 = module_0.ImmutableDict(**dict_0)
    var_1 = module_0.is_sequence(float_0, immutable_dict_1)
    float_1 = None
    var_2 = module_0.is_iterable(float_1)

def test_case_8():
    str_0 = '~(\r\tC9ntKL2'
    dict_0 = {str_0: str_0}
    immutable_dict_0 = module_0.ImmutableDict()
    var_0 = immutable_dict_0.union(dict_0)
    immutable_dict_1 = module_0.ImmutableDict()
    str_1 = '}WPAm,e0EFju/`{Qo'
    immutable_dict_2 = module_0.ImmutableDict(**dict_0)
    var_1 = immutable_dict_2.difference(str_1)