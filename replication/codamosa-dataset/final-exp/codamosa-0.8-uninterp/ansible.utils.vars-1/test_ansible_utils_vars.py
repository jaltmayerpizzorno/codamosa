# Automatically generated by Pynguin.
import ansible.utils.vars as module_0

def test_case_0():
    pass

def test_case_1():
    var_0 = module_0.get_unique_id()

def test_case_2():
    float_0 = -4519.0
    var_0 = module_0.load_extra_vars(float_0)

def test_case_3():
    str_0 = None
    var_0 = module_0.load_options_vars(str_0)

def test_case_4():
    dict_0 = {}
    var_0 = module_0.load_options_vars(dict_0)
    str_0 = ',;BthRg`Kr"euF:)cY|'
    var_1 = module_0._isidentifier_PY3(str_0)
    bool_0 = None
    var_2 = module_0._isidentifier_PY3(bool_0)

def test_case_5():
    var_0 = module_0.get_unique_id()
    var_1 = module_0.get_unique_id()
    complex_0 = None
    var_2 = module_0._isidentifier_PY3(complex_0)

def test_case_6():
    str_0 = '["a", "b", "c"]'
    var_0 = module_0.load_options_vars(str_0)

def test_case_7():
    str_0 = 'a'
    int_0 = 1
    int_1 = {str_0: int_0}
    str_1 = 'b'
    int_2 = 2
    int_3 = {str_1: int_2}
    bool_0 = False
    var_0 = module_0.combine_vars(int_1, int_3, bool_0)
    bool_1 = {str_0: bool_0}
    int_4 = {str_0: int_2}
    bool_2 = True
    var_1 = module_0.combine_vars(bool_1, int_4, bool_2)
    bool_3 = {str_0: bool_2}
    var_2 = [bool_2, int_2]
    var_3 = {str_0: var_2}
    bool_4 = True
    var_4 = module_0.combine_vars(bool_3, var_3, bool_4)
    var_5 = {}
    var_6 = {str_0: var_5}
    int_5 = {str_0: int_2}
    bool_5 = True
    var_7 = module_0.combine_vars(var_6, int_5, bool_5)
    var_8 = {}
    var_9 = {str_0: var_8}
    var_10 = module_0.get_unique_id()
    int_6 = {str_1: int_2}
    int_7 = {str_0: int_6}
    bool_6 = True
    var_11 = module_0.combine_vars(var_9, int_7, bool_6)

def test_case_8():
    int_0 = 1
    int_1 = 2
    var_0 = dict(b1=int_0, b2=int_1)
    int_2 = [int_0, int_1, int_1]
    str_0 = 'abc'
    var_1 = dict(a=int_0, b=var_0, c=int_2, d=int_2, e=str_0)
    var_2 = dict(b1=int_1, b3=int_1)
    int_3 = 4
    int_4 = 5
    int_5 = 6
    int_6 = [int_3, int_4, int_5]
    var_3 = dict(a=int_0, b=int_1, c=int_2)
    var_4 = dict(a=int_1, b=var_2, c=int_4, d=int_6, e=var_3)
    var_5 = module_0.merge_hash(var_1, var_4)

def test_case_9():
    str_0 = 'a'
    int_0 = 1
    int_1 = {str_0: int_0}
    str_1 = 'b'
    int_2 = 2
    int_3 = {str_1: int_2}
    bool_0 = True
    var_0 = module_0.combine_vars(int_1, int_3, bool_0)
    bool_1 = {str_0: bool_0}
    int_4 = {str_0: int_2}
    bool_2 = True
    var_1 = module_0.combine_vars(bool_1, int_4, bool_2)
    bool_3 = {str_0: bool_2}
    var_2 = [bool_2, int_2]
    var_3 = {str_0: var_2}
    bool_4 = True
    var_4 = module_0.combine_vars(bool_3, var_3, bool_4)
    var_5 = {}
    var_6 = {str_0: var_5}
    int_5 = {str_0: int_2}
    bool_5 = True
    var_7 = module_0.combine_vars(var_6, int_5, bool_5)
    var_8 = {}
    var_9 = {str_0: var_8}
    int_6 = {str_1: int_2}
    int_7 = {str_0: int_6}
    bool_6 = True
    var_10 = module_0.combine_vars(var_9, int_7, bool_6)

def test_case_10():
    dict_0 = {}
    var_0 = module_0.combine_vars(dict_0, dict_0)
    str_0 = 'N.io3\x0cx%;jxL('
    list_0 = [str_0]
    var_1 = module_0._isidentifier_PY3(list_0)
    str_1 = 'key2'
    str_2 = 'key3'
    bool_0 = True
    var_2 = module_0.load_extra_vars(bool_0)
    var_3 = module_0.get_unique_id()
    int_0 = 21
    int_1 = 3
    int_2 = {var_1: str_1, str_2: int_1, str_2: int_0}
    int_3 = [int_0, int_0]
    str_3 = 'key5_1'
    str_4 = 'key5_1_1'
    int_4 = {str_0: int_0, str_1: int_0, str_4: str_2, str_2: int_2, str_2: int_3, str_4: int_2}
    str_5 = 'key22'
    int_5 = 22
    str_6 = 'y5__2'
    int_6 = {str_2: int_3, str_6: int_0}
    int_7 = {str_5: var_2, str_3: int_6, int_5: var_1}
    bytes_0 = None
    var_4 = module_0.load_options_vars(bytes_0)
    int_8 = {str_6: int_0, str_5: int_5, str_2: int_3, str_5: int_3, str_4: int_7}
    var_5 = module_0.merge_hash(int_4, int_8, bool_0)

def test_case_11():
    str_0 = 'a'
    str_1 = 'b'
    int_0 = 1
    int_1 = 2
    int_2 = 3
    int_3 = [int_1, int_2]
    int_4 = {str_0: int_0, str_1: int_3}
    str_2 = 'c'
    int_5 = 4
    int_6 = 5
    int_7 = [int_5, int_6]
    str_3 = 'd'
    int_8 = 6
    int_9 = {str_3: int_8}
    int_10 = {str_1: int_7, str_2: int_9}
    bool_0 = False
    var_0 = module_0.merge_hash(int_4, int_10, bool_0)
    bool_1 = True
    str_4 = 'keep'
    var_1 = module_0.merge_hash(int_4, int_10, bool_1, str_4)
    str_5 = 'append'
    var_2 = module_0.merge_hash(int_4, int_10, bool_0, str_5)

def test_case_12():
    str_0 = 'abc123'
    var_0 = module_0._isidentifier_PY3(str_0)
    str_1 = 'abc.123'
    var_1 = module_0._isidentifier_PY3(str_1)
    str_2 = 'abc,123'
    var_2 = module_0._isidentifier_PY3(str_2)
    str_3 = 'abc#23'
    var_3 = module_0._isidentifier_PY3(str_3)
    var_4 = module_0._isidentifier_PY3(str_1)
    str_4 = 'abc 123'
    var_5 = module_0._isidentifier_PY3(str_4)
    str_5 = 'None'
    var_6 = module_0._isidentifier_PY3(str_5)
    str_6 = '\n'
    var_7 = module_0._isidentifier_PY3(str_6)
    str_7 = 'abc💩'
    var_8 = module_0._isidentifier_PY3(str_7)
    str_8 = 'abc💩123'
    var_9 = module_0._isidentifier_PY3(str_8)
    str_9 = 'abc💩.123'
    var_10 = module_0._isidentifier_PY3(str_9)

def test_case_13():
    str_0 = 'foo'
    var_0 = module_0._isidentifier_PY3(str_0)
    str_1 = 'bar'
    var_1 = module_0._isidentifier_PY3(str_1)
    str_2 = '_baz'
    var_2 = module_0._isidentifier_PY3(str_2)
    str_3 = 'the_baz'
    var_3 = module_0._isidentifier_PY3(str_3)
    str_4 = 'the_baz_qux'
    var_4 = module_0._isidentifier_PY3(str_4)
    str_5 = ''
    var_5 = module_0._isidentifier_PY3(str_5)
    str_6 = '1'
    var_6 = module_0._isidentifier_PY3(str_6)
    var_7 = module_0._isidentifier_PY3(str_3)
    str_7 = 'True'
    var_8 = module_0._isidentifier_PY3(str_7)
    str_8 = 'False'
    var_9 = module_0._isidentifier_PY3(str_8)
    bytes_0 = b'\x15\xb8Ir.\xb2\x87G~\xe9\xe5D\xd3t'
    var_10 = module_0.load_extra_vars(bytes_0)