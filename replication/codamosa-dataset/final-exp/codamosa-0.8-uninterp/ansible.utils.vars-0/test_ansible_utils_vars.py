# Automatically generated by Pynguin.
import ansible.utils.vars as module_0

def test_case_0():
    pass

def test_case_1():
    var_0 = module_0.get_unique_id()

def test_case_2():
    bytes_0 = None
    var_0 = module_0.load_extra_vars(bytes_0)

def test_case_3():
    bool_0 = False
    var_0 = module_0.load_options_vars(bool_0)

def test_case_4():
    str_0 = 'key'
    var_0 = module_0._isidentifier_PY3(str_0)

def test_case_5():
    bool_0 = False
    str_0 = '_uAE(($W\rkPeAMB'
    var_0 = module_0._isidentifier_PY3(str_0)
    var_1 = module_0._isidentifier_PY3(bool_0)

def test_case_6():
    str_0 = None
    var_0 = module_0._isidentifier_PY3(str_0)

def test_case_7():
    int_0 = 1
    str_0 = 'b'
    int_1 = {str_0: int_0}
    int_2 = {str_0: int_1}
    int_3 = 2
    int_4 = {str_0: int_3}
    int_5 = {str_0: int_4}
    var_0 = module_0.merge_hash(int_2, int_5)

def test_case_8():
    str_0 = 'x'
    str_1 = 'y'
    str_2 = 'z'
    str_3 = 'u'
    str_4 = 'a'
    str_5 = 'b'
    str_6 = {str_1: str_3}
    str_7 = {str_0: str_6}
    str_8 = {str_2: str_5}
    str_9 = {str_1: str_8}
    str_10 = {str_0: str_9}
    var_0 = module_0.merge_hash(str_7, str_10)
    str_11 = {str_2: str_4, str_3: str_5}
    str_12 = {str_1: str_11}
    str_13 = {str_0: str_12}
    str_14 = {str_2: str_5}
    str_15 = {str_1: str_14}
    str_16 = {str_0: str_15}
    bool_0 = False
    var_1 = module_0.merge_hash(str_13, str_16, bool_0)

def test_case_9():
    str_0 = 'b'
    int_0 = {}
    int_1 = {str_0: int_0}
    int_2 = 2
    int_3 = {str_0: int_2}
    int_4 = {str_0: int_3}
    var_0 = module_0.merge_hash(int_1, int_4)

def test_case_10():
    int_0 = 1
    int_1 = 2
    int_2 = {int_0: int_0}
    int_3 = {int_0: int_1}
    var_0 = module_0.merge_hash(int_2, int_3)
    int_4 = {int_0: int_0}
    var_1 = module_0.merge_hash(int_4, int_2)
    int_5 = [int_0]
    int_6 = {int_0: int_5}
    int_7 = [int_1]
    int_8 = {int_0: int_7}
    var_2 = module_0.merge_hash(int_6, int_8)
    int_9 = [int_0]
    int_10 = {int_0: int_9}
    int_11 = [int_1]
    int_12 = {int_0: int_11}
    bool_0 = False
    var_3 = module_0.merge_hash(int_10, int_12, bool_0)
    int_13 = [int_0]
    int_14 = {int_0: int_13}
    int_15 = {int_0: int_1}
    var_4 = module_0.merge_hash(int_14, int_15)

def test_case_11():
    var_0 = {}
    var_1 = module_0.merge_hash(var_0, var_0)
    int_0 = 1
    int_1 = 2
    int_2 = {int_0: int_0}
    int_3 = {int_0: int_0, int_1: int_2}
    var_2 = {}
    var_3 = module_0.merge_hash(int_3, var_2)
    int_4 = {int_0: int_0}
    int_5 = {int_0: int_1}
    var_4 = module_0.merge_hash(int_4, int_5)
    int_6 = {int_0: int_0}
    int_7 = [int_0]
    int_8 = {int_0: int_7}
    var_5 = module_0.merge_hash(int_6, int_8)
    int_9 = {int_0: int_2}
    int_10 = [int_1]
    int_11 = {int_0: int_10}
    var_6 = module_0.merge_hash(int_9, int_11)
    int_12 = [int_0]
    int_13 = {int_0: int_12}
    int_14 = [int_1]
    int_15 = {int_0: int_14}
    bool_0 = False
    var_7 = module_0.merge_hash(int_13, int_15, bool_0)

def test_case_12():
    var_0 = {}
    var_1 = {}
    var_2 = module_0.merge_hash(var_0, var_1)
    int_0 = 1
    int_1 = {int_0: int_0}
    var_3 = {}
    var_4 = module_0.merge_hash(int_1, var_3)
    var_5 = {}
    int_2 = {int_0: int_0}
    var_6 = module_0.merge_hash(var_5, int_2)
    int_3 = {int_0: int_0}
    int_4 = 2
    int_5 = {int_0: int_4}
    var_7 = module_0.merge_hash(int_3, int_5)
    int_6 = {int_0: int_0}
    int_7 = {int_4: int_4}
    var_8 = module_0.merge_hash(int_6, int_7)
    int_8 = {int_0: int_0}
    int_9 = {int_4: int_4}
    bool_0 = False
    var_9 = module_0.merge_hash(int_8, int_9, bool_0)
    int_10 = {int_0: int_0}
    int_11 = [int_0, int_0]
    int_12 = {int_0: int_11}
    var_10 = module_0.merge_hash(int_10, int_12)

def test_case_13():
    var_0 = None
    var_1 = module_0._isidentifier_PY3(var_0)
    int_0 = 123
    var_2 = module_0._isidentifier_PY3(int_0)
    str_0 = ''
    var_3 = module_0._isidentifier_PY3(str_0)
    str_1 = '1abc'
    var_4 = module_0._isidentifier_PY3(str_1)
    str_2 = 'abc.'
    var_5 = module_0._isidentifier_PY3(str_2)
    str_3 = 'abc-1'
    var_6 = module_0._isidentifier_PY3(str_3)
    str_4 = 'in'
    var_7 = module_0._isidentifier_PY3(str_4)
    str_5 = 'abø'
    var_8 = module_0._isidentifier_PY3(str_5)
    var_9 = module_0._isidentifier_PY3(str_5)
    str_6 = 'False'
    var_10 = module_0._isidentifier_PY3(str_6)
    str_7 = 'None'
    var_11 = module_0._isidentifier_PY3(str_7)

def test_case_14():
    var_0 = None
    var_1 = module_0._isidentifier_PY3(var_0)
    int_0 = 123
    var_2 = module_0._isidentifier_PY3(int_0)
    str_0 = ''
    var_3 = module_0._isidentifier_PY3(str_0)
    str_1 = '1abc'
    var_4 = module_0._isidentifier_PY3(str_1)
    str_2 = 'abc.'
    var_5 = module_0._isidentifier_PY3(str_2)
    str_3 = 'abc '
    var_6 = module_0._isidentifier_PY3(str_3)
    str_4 = 'abc-1'
    var_7 = module_0._isidentifier_PY3(str_4)
    str_5 = 'in'
    var_8 = module_0._isidentifier_PY3(str_5)