# Automatically generated by Pynguin.
import ansible.utils.vars as module_0

def test_case_0():
    pass

def test_case_1():
    var_0 = module_0.get_unique_id()

def test_case_2():
    str_0 = "3%o0T'N"
    var_0 = module_0.load_extra_vars(str_0)

def test_case_3():
    str_0 = 'eC"?2S'
    var_0 = module_0.load_options_vars(str_0)

def test_case_4():
    str_0 = 'replace'
    var_0 = module_0._isidentifier_PY3(str_0)
    bytes_0 = None
    var_1 = module_0._isidentifier_PY3(bytes_0)

def test_case_5():
    bytes_0 = b''
    tuple_0 = (bytes_0,)
    var_0 = module_0._isidentifier_PY3(tuple_0)

def test_case_6():
    str_0 = 'a'
    str_1 = 'b'
    str_2 = '1'
    str_3 = 'c'
    str_4 = {str_0: str_2, str_1: str_3}
    str_5 = '3'
    str_6 = 'd'
    str_7 = '4'
    str_8 = {str_6: str_7}
    str_9 = {str_0: str_5, str_1: str_8}
    var_0 = module_0.merge_hash(str_4, str_9)

def test_case_7():
    set_0 = None
    dict_0 = {set_0: set_0}
    var_0 = module_0.merge_hash(dict_0, dict_0)
    str_0 = '\\\n-lmk'
    var_1 = module_0._isidentifier_PY3(str_0)
    var_2 = module_0.get_unique_id()
    int_0 = 2755
    var_3 = module_0.load_options_vars(int_0)
    tuple_0 = None
    var_4 = module_0.load_extra_vars(tuple_0)
    str_1 = 'nzN'
    var_5 = module_0._isidentifier_PY3(str_1)

def test_case_8():
    var_0 = {}
    var_1 = {}
    var_2 = module_0.merge_hash(var_0, var_1)
    var_3 = {}
    str_0 = 'a'
    str_1 = 'A'
    str_2 = {str_0: str_1}
    var_4 = module_0.merge_hash(var_3, str_2)
    str_3 = {str_0: str_1}
    tuple_0 = ()
    var_5 = module_0.load_options_vars(tuple_0)
    var_6 = {}
    var_7 = module_0.merge_hash(str_3, var_6)
    str_4 = 'b'
    str_5 = 'a1'
    str_6 = 'A1'
    str_7 = {str_5: str_6}
    str_8 = 'B'
    str_9 = {str_0: str_7, str_4: str_8}
    str_10 = 'a2'
    str_11 = 'A2'
    str_12 = {str_10: str_11}
    str_13 = {str_0: str_12, str_4: str_8}
    var_8 = module_0.merge_hash(str_9, str_13)

def test_case_9():
    str_0 = 'a'
    str_1 = 'b'
    str_2 = '1'
    str_3 = 'c'
    str_4 = '2'
    str_5 = {str_3: str_4}
    str_6 = {str_0: str_2, str_1: str_5}
    str_7 = '3'
    str_8 = 'd'
    str_9 = '4'
    str_10 = {str_8: str_9}
    str_11 = {str_0: str_7, str_1: str_10}
    var_0 = module_0.merge_hash(str_6, str_11)

def test_case_10():
    str_0 = 'foo'
    var_0 = module_0._isidentifier_PY3(str_0)
    str_1 = ''
    var_1 = module_0._isidentifier_PY3(str_1)
    str_2 = '123'
    var_2 = module_0._isidentifier_PY3(str_2)
    str_3 = '-'
    var_3 = module_0._isidentifier_PY3(str_3)
    str_4 = 'foo-bar'
    var_4 = module_0._isidentifier_PY3(str_4)
    str_5 = 'foo_bar'
    var_5 = module_0._isidentifier_PY3(str_5)
    str_6 = 'foo:bar'
    var_6 = module_0._isidentifier_PY3(str_6)
    str_7 = 'True'
    var_7 = module_0._isidentifier_PY3(str_7)
    str_8 = 'False'
    var_8 = module_0._isidentifier_PY3(str_8)
    str_9 = 'None'
    var_9 = module_0._isidentifier_PY3(str_9)
    str_10 = 'д'
    var_10 = module_0._isidentifier_PY3(str_10)

def test_case_11():
    str_0 = 'a'
    str_1 = 'b'
    str_2 = '1'
    str_3 = 'c'
    str_4 = {str_3: str_1}
    str_5 = {str_0: str_2, str_1: str_4}
    str_6 = '4'
    str_7 = {str_0: str_5, str_1: str_6}
    var_0 = module_0.merge_hash(str_5, str_7)

def test_case_12():
    str_0 = 'c'
    str_1 = 'b'
    str_2 = {str_1: str_0}
    str_3 = {str_0: str_2, str_0: str_1}
    str_4 = 'd'
    str_5 = 'new_value'
    str_6 = {str_1: str_5}
    str_7 = 'new_key'
    str_8 = {str_7: str_6, str_0: str_5, str_4: str_7}
    bool_0 = True
    var_0 = module_0.merge_hash(str_3, str_8, bool_0)
    str_9 = {str_1: str_1}
    str_10 = {str_7: str_9, str_0: str_5}
    str_11 = {str_1: str_5}
    str_12 = {str_4: str_11, str_0: str_5, str_4: str_7}
    bool_1 = False
    var_1 = module_0.merge_hash(str_10, str_12, bool_1)

def test_case_13():
    int_0 = 5
    int_1 = 6
    int_2 = [int_0, int_1]
    str_0 = 'toto'
    var_0 = dict(a=int_0, b=int_2, c=str_0)
    int_3 = 1
    int_4 = 2
    int_5 = 3
    int_6 = [int_4, int_5]
    var_1 = dict(a=int_3, b=int_6, c=str_0)
    var_2 = print(var_0)
    var_3 = print(var_1)
    var_4 = module_0.merge_hash(var_0, var_1)
    var_5 = print(var_4)
    var_6 = print(var_1)
    bool_0 = True
    var_7 = module_0.merge_hash(var_0, var_1, bool_0)
    var_8 = print(var_7)
    var_9 = print(var_1)
    bool_1 = True
    var_10 = module_0.merge_hash(var_0, var_1, bool_1)
    var_11 = print(var_10)
    var_12 = print(var_1)

def test_case_14():
    int_0 = 5
    int_1 = 6
    int_2 = [int_0, int_1]
    str_0 = 'toto'
    var_0 = dict(a=int_0, b=int_2, c=str_0)
    int_3 = 1
    int_4 = 2
    int_5 = 0
    var_1 = dict(z=int_5)
    var_2 = dict(a=int_3, b=int_4, c=var_1)
    var_3 = print(var_0)
    var_4 = print(var_2)
    var_5 = module_0.get_unique_id()
    var_6 = module_0.merge_hash(var_0, var_2)
    var_7 = print(var_6)
    var_8 = print(var_2)
    bool_0 = True
    var_9 = module_0.merge_hash(var_0, var_2, bool_0)
    var_10 = print(var_9)
    var_11 = print(var_2)
    bool_1 = False
    var_12 = module_0.merge_hash(var_0, var_2, bool_1)
    var_13 = print(var_12)
    var_14 = print(var_2)