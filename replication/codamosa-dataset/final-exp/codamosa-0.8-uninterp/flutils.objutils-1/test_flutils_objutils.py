# Automatically generated by Pynguin.
import flutils.objutils as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = None
    bool_0 = module_0.has_any_callables(str_0)

def test_case_2():
    str_0 = '__doc__'
    list_0 = [str_0]
    bool_0 = module_0.has_any_callables(list_0, *list_0)

def test_case_3():
    int_0 = None
    bool_0 = module_0.has_attrs(int_0)

def test_case_4():
    list_0 = None
    str_0 = 'm'
    list_1 = [str_0, str_0]
    bool_0 = module_0.has_attrs(list_0, *list_1)

def test_case_5():
    bool_0 = False
    bool_1 = module_0.has_callables(bool_0)

def test_case_6():
    bytes_0 = b'{e\xf5C\xa0\xb1\xe9\xd8\xd5<\xdd?\xf0'
    str_0 = 'k>uZ)@9#`Rt$'
    list_0 = [str_0, str_0]
    bool_0 = module_0.has_callables(bytes_0, *list_0)

def test_case_7():
    float_0 = -1535.0
    bool_0 = module_0.is_list_like(float_0)
    str_0 = '__doc__'
    list_0 = [str_0]
    bool_1 = module_0.has_any_callables(list_0, *list_0)

def test_case_8():
    int_0 = -1417
    bool_0 = module_0.is_subclass_of_any(int_0)
    list_0 = [int_0, int_0, int_0]
    bool_1 = module_0.has_callables(list_0)
    str_0 = ';BH('
    str_1 = 'tY8xA4&UA&^fw:>eT.'
    list_1 = [str_0, str_1, str_0]
    bool_2 = module_0.is_list_like(list_0)
    bool_3 = module_0.has_any_callables(list_1, *list_1)

def test_case_9():
    bytes_0 = b'b\x82\x8b\xa8z\xc9\x9a\x16'
    bool_0 = module_0.is_subclass_of_any(bytes_0)

def test_case_10():
    str_0 = ';BH('
    str_1 = 'tY8xA4&UA&^fw:>eT.'
    list_0 = [str_0, str_1, str_0]
    bool_0 = module_0.has_any_callables(list_0, *list_0)

def test_case_11():
    float_0 = -1535.0
    str_0 = '__doc__'
    list_0 = [str_0]
    bool_0 = module_0.has_callables(float_0, *list_0)

def test_case_12():
    var_0 = dict()
    str_0 = 'get'
    str_1 = None
    list_0 = [str_0, str_0, str_1]
    bool_0 = module_0.has_any_callables(var_0, *list_0)

def test_case_13():
    var_0 = dict()
    str_0 = 'get'
    list_0 = [str_0]
    bool_0 = module_0.has_callables(var_0, *list_0)