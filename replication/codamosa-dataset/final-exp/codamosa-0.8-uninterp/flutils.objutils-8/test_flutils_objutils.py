# Automatically generated by Pynguin.
import flutils.objutils as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    bool_1 = module_0.has_any_attrs(bool_0)

def test_case_2():
    str_0 = 'items'
    var_0 = dict()
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    bool_0 = module_0.has_any_callables(var_0, *list_0)

def test_case_3():
    tuple_0 = ()
    bool_0 = module_0.has_any_callables(tuple_0)

def test_case_4():
    int_0 = -1071
    bool_0 = module_0.has_attrs(int_0)

def test_case_5():
    str_0 = 'Zi'
    list_0 = [str_0, str_0]
    bool_0 = module_0.has_attrs(str_0, *list_0)

def test_case_6():
    bool_0 = True
    bool_1 = module_0.has_callables(bool_0)

def test_case_7():
    str_0 = 'items'
    var_0 = dict()
    list_0 = [str_0, str_0, str_0, str_0]
    bool_0 = module_0.has_any_callables(var_0, *list_0)
    bool_1 = module_0.has_callables(str_0, *list_0)

def test_case_8():
    float_0 = -168.538
    bool_0 = module_0.is_list_like(float_0)

def test_case_9():
    str_0 = '0nC'
    bool_0 = module_0.has_any_attrs(str_0)
    str_1 = 'XI,9kwy_Cx'
    str_2 = '\'"\''
    str_3 = 'DKHOuIYd^Mn1'
    list_0 = [str_1, str_2, str_3, str_0]
    bool_1 = module_0.has_any_callables(bool_0, *list_0)
    list_1 = [str_0, str_0]
    bool_2 = module_0.is_list_like(list_1)

def test_case_10():
    bytes_0 = b'+\xb8\x9d\xe8\xbbs+\xa4b#\x1f%DO'
    bool_0 = module_0.is_subclass_of_any(bytes_0)

def test_case_11():
    bool_0 = False
    str_0 = 'lF5!g]l-%MY'
    str_1 = 'Zi'
    list_0 = [str_0, str_1]
    bool_1 = module_0.has_any_callables(bool_0, *list_0)

def test_case_12():
    str_0 = 'items'
    var_0 = dict()
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    bool_0 = module_0.has_callables(var_0, *list_0)