# Automatically generated by Pynguin.
import ansible.module_utils.common.collections as module_0

def test_case_0():
    immutable_dict_0 = module_0.ImmutableDict()
    list_0 = [immutable_dict_0, immutable_dict_0, immutable_dict_0]
    var_0 = module_0.is_string(list_0)

def test_case_1():
    immutable_dict_0 = module_0.ImmutableDict()
    immutable_dict_1 = module_0.ImmutableDict()
    var_0 = immutable_dict_1.difference(immutable_dict_0)

def test_case_2():
    dict_0 = {}
    immutable_dict_0 = module_0.ImmutableDict()
    var_0 = immutable_dict_0.__eq__(dict_0)

def test_case_3():
    str_0 = 'Processor Speed'
    str_1 = '{(f V\t66'
    dict_0 = {str_0: str_0, str_1: str_1, str_1: str_0}
    immutable_dict_0 = module_0.ImmutableDict(**dict_0)
    var_0 = immutable_dict_0.__iter__()
    str_2 = "R='5-d0bJ5\n^"
    var_1 = module_0.is_sequence(str_2)
    var_2 = immutable_dict_0.__len__()
    str_3 = '6-\tRP'
    str_4 = 'yq`\x0bDp|\na,ir9\tGm'
    immutable_dict_1 = module_0.ImmutableDict()
    var_3 = immutable_dict_1.__hash__()
    var_4 = module_0.is_sequence(str_3, str_4)
    set_0 = set()
    var_5 = module_0.is_iterable(immutable_dict_0)
    immutable_dict_2 = module_0.ImmutableDict()
    var_6 = immutable_dict_2.__hash__()
    var_7 = immutable_dict_2.__eq__(immutable_dict_2)
    var_8 = immutable_dict_2.__eq__(set_0)
    var_9 = immutable_dict_0.__hash__()

def test_case_4():
    str_0 = '3#k'
    dict_0 = {str_0: str_0}
    var_0 = module_0.is_string(dict_0)
    str_1 = 'CL{MXIAU[RE='
    var_1 = module_0.is_iterable(str_1)

def test_case_5():
    str_0 = 'HF}-twFI!McW#Qa.j`'
    dict_0 = {str_0: str_0}
    var_0 = module_0.count(dict_0)
    immutable_dict_0 = module_0.ImmutableDict()

def test_case_6():
    str_0 = '*w5q'
    list_0 = [str_0, str_0, str_0, str_0]
    list_1 = [list_0]
    var_0 = module_0.is_sequence(list_1)

def test_case_7():
    str_0 = '\\[s]}~\x0b^8k'
    var_0 = module_0.is_string(str_0)
    immutable_dict_0 = module_0.ImmutableDict()
    var_1 = immutable_dict_0.__hash__()

def test_case_8():
    int_0 = -1073
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.is_iterable(int_0, list_0)

def test_case_9():
    bool_0 = True
    str_0 = 'module_setup'
    str_1 = None
    str_2 = 'Unable to move git dir. %s'
    dict_0 = {}
    var_0 = module_0.is_iterable(dict_0, bool_0)
    str_3 = 'x:}\\$eAb^N'
    dict_1 = {str_0: str_0, str_1: str_1, str_2: str_2, str_3: str_1}
    bytes_0 = b"'=\xfd\x10\x86\xfd&\xd7M^"
    var_1 = module_0.is_sequence(dict_1, bytes_0)
    var_2 = module_0.is_iterable(bool_0)
    int_0 = 32
    var_3 = module_0.is_sequence(int_0)