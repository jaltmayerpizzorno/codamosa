# Automatically generated by Pynguin.
import flutils.objutils as module_0

def test_case_0():
    pass

def test_case_1():
    complex_0 = None
    bool_0 = module_0.has_any_attrs(complex_0)

def test_case_2():
    str_0 = '__class__'
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    bool_0 = module_0.has_any_callables(list_0, *list_0)

def test_case_3():
    bytes_0 = None
    list_0 = []
    bool_0 = module_0.has_any_callables(bytes_0, *list_0)

def test_case_4():
    set_0 = None
    bool_0 = module_0.has_attrs(set_0)

def test_case_5():
    str_0 = '\tJ@{Wg'
    list_0 = [str_0]
    bool_0 = module_0.has_callables(str_0, *list_0)
    bool_1 = module_0.is_list_like(str_0)

def test_case_6():
    list_0 = []
    list_1 = [list_0, list_0]
    list_2 = []
    bool_0 = module_0.has_callables(list_1, *list_2)

def test_case_7():
    str_0 = 'cK ]S^_'
    dict_0 = {str_0: str_0}
    bool_0 = module_0.is_list_like(dict_0)

def test_case_8():
    var_0 = dict()
    str_0 = 'get'
    list_0 = [str_0]
    bool_0 = module_0.has_callables(var_0, *list_0)
    bool_1 = module_0.is_list_like(list_0)
    var_1 = dict()

def test_case_9():
    bytes_0 = None
    bool_0 = module_0.is_subclass_of_any(bytes_0)

def test_case_10():
    bool_0 = False
    str_0 = 'Brm{^1:T6%/l\n\tak;%#'
    list_0 = [str_0, str_0]
    bool_1 = module_0.has_any_attrs(bool_0, *list_0)

def test_case_11():
    var_0 = dict()
    str_0 = 'get'
    list_0 = [str_0]
    bool_0 = module_0.has_callables(var_0, *list_0)
    var_1 = dict()

def test_case_12():
    var_0 = dict()
    bool_0 = module_0.has_any_callables(var_0)
    str_0 = 'd N\x0bh?gX5Dpj6T@n'
    str_1 = '^Z'
    bool_1 = module_0.has_callables(str_1)
    str_2 = 'values'
    str_3 = [str_2, str_0, str_0, str_1, str_2]
    bool_2 = module_0.has_any_attrs(str_2)
    str_4 = '__doc__'
    list_0 = [str_4]
    bool_3 = module_0.has_callables(str_2, *list_0)
    set_0 = {str_4, str_1}
    bool_4 = module_0.is_list_like(bool_1)
    list_1 = []
    bool_5 = module_0.has_callables(str_3, *list_1)
    bool_6 = module_0.is_subclass_of_any(set_0)
    bool_7 = module_0.has_attrs(set_0)