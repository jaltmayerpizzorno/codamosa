# Automatically generated by Pynguin.
import ansible.utils.vars as module_0

def test_case_0():
    pass

def test_case_1():
    var_0 = module_0.get_unique_id()

def test_case_2():
    bool_0 = False
    tuple_0 = (bool_0,)
    var_0 = module_0.load_options_vars(tuple_0)
    int_0 = -1462
    list_0 = [int_0, tuple_0, bool_0, int_0]
    var_1 = module_0._isidentifier_PY3(int_0)
    var_2 = module_0._isidentifier_PY3(list_0)
    var_3 = module_0.get_unique_id()
    dict_0 = {}
    var_4 = module_0.combine_vars(dict_0, dict_0, bool_0)
    str_0 = 'UI03R'
    var_5 = module_0.load_options_vars(str_0)

def test_case_3():
    float_0 = 444.23377
    bytes_0 = b'R\x9d'
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, float_0: float_0}
    var_0 = module_0.merge_hash(dict_0, dict_0)
    var_1 = module_0._isidentifier_PY3(bytes_0)
    int_0 = -2522
    var_2 = module_0.load_options_vars(int_0)

def test_case_4():
    str_0 = 'merge'
    var_0 = module_0.load_extra_vars(str_0)

def test_case_5():
    bool_0 = None
    var_0 = module_0.load_options_vars(bool_0)

def test_case_6():
    str_0 = 'merge'
    var_0 = module_0._isidentifier_PY3(str_0)
    list_0 = []
    var_1 = module_0.load_extra_vars(list_0)

def test_case_7():
    str_0 = '(!+vDr@'
    var_0 = module_0.get_unique_id()
    var_1 = module_0._isidentifier_PY3(str_0)
    bytes_0 = b'\xb6'
    set_0 = {bytes_0, bytes_0, bytes_0}
    var_2 = module_0._isidentifier_PY3(set_0)

def test_case_8():
    bytes_0 = b'R\x9d'
    var_0 = module_0._isidentifier_PY3(bytes_0)
    int_0 = -2522
    var_1 = module_0.load_options_vars(int_0)
    var_2 = module_0.load_extra_vars(int_0)

def test_case_9():
    bytes_0 = b'\xf7\xe57\xa8<\xe7\xd7AB\xb3\xbd?H\xd8\xed'
    var_0 = module_0.load_options_vars(bytes_0)

def test_case_10():
    bool_0 = True
    tuple_0 = (bool_0,)
    var_0 = module_0.load_options_vars(tuple_0)
    int_0 = -1462
    var_1 = module_0._isidentifier_PY3(int_0)
    dict_0 = {}
    var_2 = module_0.combine_vars(dict_0, dict_0, bool_0)
    var_3 = module_0.get_unique_id()
    var_4 = module_0.load_extra_vars(tuple_0)

def test_case_11():
    var_0 = {}
    str_0 = 'k1'
    str_1 = {str_0: str_0}
    bool_0 = False
    var_1 = module_0.merge_hash(var_0, str_1, bool_0)
    str_2 = {str_0: str_0}
    var_2 = {}
    var_3 = module_0.merge_hash(str_2, var_2, bool_0)

def test_case_12():
    var_0 = {}
    str_0 = 'k1'
    str_1 = 'v1'
    str_2 = {str_0: str_1}
    bool_0 = False
    var_1 = module_0.merge_hash(var_0, str_2, bool_0)
    str_3 = {str_0: str_1}
    var_2 = {}
    var_3 = module_0.merge_hash(str_3, var_2, bool_0)
    var_4 = {}
    str_4 = {str_0: str_1}
    var_5 = module_0.merge_hash(var_4, str_4)
    str_5 = {str_0: str_1}
    var_6 = {}
    var_7 = module_0.merge_hash(str_5, var_6)

def test_case_13():
    var_0 = {}
    var_1 = module_0.merge_hash(var_0, var_0)
    var_2 = {}
    str_0 = 'a'
    str_1 = 'b'
    str_2 = {str_0: str_1}
    var_3 = module_0.merge_hash(var_2, str_2)
    var_4 = module_0.merge_hash(str_2, var_3)
    str_3 = {str_0: str_1}
    str_4 = {str_0: str_1}
    var_5 = module_0.merge_hash(str_3, str_4)
    str_5 = {str_0: str_1}
    str_6 = 'c'
    str_7 = {str_0: str_6}
    var_6 = module_0.merge_hash(str_5, str_7)
    str_8 = {str_1: str_6}
    str_9 = {str_0: str_8}
    str_10 = 'd'
    str_11 = {str_1: str_10}
    str_12 = {str_0: str_11}
    var_7 = module_0.merge_hash(str_9, str_12)

def test_case_14():
    var_0 = {}
    str_0 = 'a'
    str_1 = 'b'
    str_2 = {str_0: str_1}
    var_1 = module_0.merge_hash(var_0, str_2)
    str_3 = {str_0: str_1}
    var_2 = module_0.merge_hash(str_2, str_3)
    str_4 = {str_0: str_1}
    str_5 = 'c'
    str_6 = {str_0: str_5}
    var_3 = module_0.merge_hash(str_4, str_6)

def test_case_15():
    str_0 = 'a'
    str_1 = {str_0: str_0}
    str_2 = 'b'
    str_3 = {str_2: str_0, str_2: str_1}
    var_0 = module_0.merge_hash(str_1, str_3)
    str_4 = {str_0: str_0}
    str_5 = {str_0: str_2}
    bool_0 = False
    var_1 = module_0.merge_hash(str_4, str_5, bool_0)
    str_6 = {str_0: str_0}
    str_7 = {str_0: str_2}
    str_8 = 'keep'
    var_2 = module_0.merge_hash(str_6, str_7, bool_0, str_8)
    str_9 = {str_0: str_0}
    str_10 = {str_0: str_2}
    str_11 = 'append'
    var_3 = module_0.merge_hash(str_9, str_10, bool_0, str_11)
    str_12 = {str_0: str_0}
    str_13 = {str_0: str_2}
    str_14 = 'prepend'
    var_4 = module_0.merge_hash(str_12, str_13, bool_0, str_14)

def test_case_16():
    str_0 = 'a'
    str_1 = 'b'
    int_0 = 1
    str_2 = 'b1'
    str_3 = 'b2'
    str_4 = 'b3'
    str_5 = 'b2_1'
    int_1 = 3
    int_2 = {str_5: int_1}
    int_3 = 4
    int_4 = 5
    int_5 = 6
    int_6 = [int_3, int_4, int_5]
    int_7 = {str_2: int_5, str_3: int_2, str_4: int_6}
    int_8 = {str_0: int_0, str_1: int_7}
    str_6 = 'c'
    str_7 = 'b2_2'
    int_9 = {str_7: int_2}
    int_10 = 9
    int_11 = 10
    int_12 = [int_10, int_11]
    int_13 = {str_3: int_9, str_4: int_12}
    str_8 = 'd'
    var_0 = {str_1: int_13, str_6: str_8}
    var_1 = module_0.merge_hash(int_8, var_0)