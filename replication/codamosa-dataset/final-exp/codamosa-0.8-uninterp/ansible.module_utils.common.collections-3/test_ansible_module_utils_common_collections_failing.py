# Automatically generated by Pynguin.
import ansible.module_utils.common.collections as module_0

def test_case_0():
    try:
        int_0 = -3248
        immutable_dict_0 = module_0.ImmutableDict()
        var_0 = immutable_dict_0.difference(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 1593.0448
        var_0 = module_0.is_string(float_0)
        bytes_0 = b'QT\x1d\xb2\xe1\xee\x9b,4'
        bytes_1 = b'\x14(\xd4\xbf\xe6\x95@\xf9Y\xbd\xcf\x7f\x10\xbe;8'
        set_0 = {bytes_0, bytes_1, bytes_0, bytes_1}
        immutable_dict_0 = module_0.ImmutableDict()
        var_1 = immutable_dict_0.__getitem__(set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = ()
        immutable_dict_0 = module_0.ImmutableDict()
        var_0 = immutable_dict_0.difference(tuple_0)
        immutable_dict_1 = module_0.ImmutableDict()
        set_0 = {immutable_dict_1, tuple_0, var_0}
        var_1 = immutable_dict_0.union(set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        immutable_dict_0 = module_0.ImmutableDict()
        bool_0 = True
        var_0 = immutable_dict_0.__repr__()
        bytes_0 = b'\xe4\x11\xe1\xa9W\xc4'
        var_1 = immutable_dict_0.__repr__()
        tuple_0 = (bool_0, bytes_0)
        var_2 = immutable_dict_0.__getitem__(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        immutable_dict_0 = module_0.ImmutableDict()
        var_0 = immutable_dict_0.__iter__()
        bool_0 = True
        str_0 = '\n    This is a OpenBSD User manipulation class.\n    Main differences are that OpenBSD:-\n     - has no concept of "system" account.\n     - has no force delete user\n\n    This overrides the following methods from the generic class:-\n      - create_user()\n      - remove_user()\n      - modify_user()\n    '
        dict_0 = {str_0: str_0}
        immutable_dict_1 = module_0.ImmutableDict(**dict_0)
        list_0 = [immutable_dict_1]
        immutable_dict_2 = module_0.ImmutableDict(*list_0, **dict_0)
        var_1 = immutable_dict_2.__eq__(bool_0)
        int_0 = -398
        var_2 = module_0.is_sequence(int_0, int_0)
        var_3 = immutable_dict_1.__len__()
        bytes_0 = b'\xf2\xc4'
        var_4 = module_0.count(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = -904428688884713146
        var_0 = module_0.count(int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'running'
        str_1 = '3'
        dict_0 = {str_0: str_0, str_1: str_1, str_0: str_0}
        immutable_dict_0 = module_0.ImmutableDict(**dict_0)
        var_0 = immutable_dict_0.__repr__()
        immutable_dict_1 = module_0.ImmutableDict(**dict_0)
        var_1 = module_0.count(immutable_dict_1)
        immutable_dict_2 = module_0.ImmutableDict()
        var_2 = immutable_dict_2.__iter__()
        var_3 = immutable_dict_1.__iter__()
        var_4 = immutable_dict_1.__hash__()
        immutable_dict_3 = module_0.ImmutableDict()
        var_5 = immutable_dict_3.__len__()
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'\xa77\xcc\x81\xd1\xach\x8c\xa6|\x17I'
        list_0 = [bytes_0]
        str_0 = '$,axS[uh#} :g5,m'
        str_1 = ','
        str_2 = '@n8Z9](\\4:9jbx\r)O'
        dict_0 = {str_0: str_0, str_1: str_1, str_2: str_1, str_0: str_0}
        immutable_dict_0 = module_0.ImmutableDict(**dict_0)
        var_0 = immutable_dict_0.difference(list_0)
        str_3 = "YS{k{-s%'!ZtRu.f"
        immutable_dict_1 = module_0.ImmutableDict(**dict_0)
        var_1 = module_0.is_iterable(immutable_dict_1)
        dict_1 = {str_3: str_3, str_3: str_3, str_3: str_3}
        immutable_dict_2 = module_0.ImmutableDict()
        var_2 = immutable_dict_2.union(dict_1)
        var_3 = immutable_dict_0.__len__()
        var_4 = module_0.count(immutable_dict_2)
        var_5 = module_0.count(list_0)
        list_1 = [var_4, var_4, var_4]
        dict_2 = None
        immutable_dict_3 = module_0.ImmutableDict(*list_1, **dict_2)
    except BaseException:
        pass

def test_case_8():
    try:
        dict_0 = None
        set_0 = {dict_0}
        int_0 = -2712
        var_0 = module_0.is_iterable(set_0, int_0)
        immutable_dict_0 = module_0.ImmutableDict()
        var_1 = immutable_dict_0.__iter__()
        var_2 = immutable_dict_0.__hash__()
        immutable_dict_1 = module_0.ImmutableDict(**dict_0)
    except BaseException:
        pass