# Automatically generated by Pynguin.
import flutils.objutils as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'JS4Q5||'
    bool_0 = module_0.has_any_callables(str_0)

def test_case_2():
    var_0 = dict()
    str_0 = 'get'
    list_0 = [str_0]
    bool_0 = module_0.has_any_callables(var_0, *list_0)

def test_case_3():
    bytes_0 = b'W\xc9`\x88\x17m'
    bool_0 = module_0.has_attrs(bytes_0)

def test_case_4():
    var_0 = dict()
    str_0 = 'get'
    list_0 = [str_0]
    bool_0 = module_0.has_callables(var_0, *list_0)

def test_case_5():
    var_0 = dict()
    str_0 = 'get'
    list_0 = [str_0]
    bool_0 = module_0.has_callables(list_0, *list_0)
    bool_1 = module_0.has_any_callables(var_0, *list_0)

def test_case_6():
    list_0 = None
    bool_0 = module_0.is_subclass_of_any(list_0)
    bool_1 = module_0.has_callables(bool_0)

def test_case_7():
    str_0 = "a\nFbDY<'O<nqJ]&LXMLO"
    bool_0 = module_0.is_list_like(str_0)

def test_case_8():
    var_0 = dict()
    str_0 = 'get'
    list_0 = [str_0]
    bool_0 = module_0.has_any_callables(var_0, *list_0)
    bool_1 = module_0.is_list_like(list_0)

def test_case_9():
    list_0 = None
    bool_0 = module_0.is_subclass_of_any(list_0)

def test_case_10():
    var_0 = dict()
    str_0 = 'get'
    list_0 = [str_0]
    bool_0 = module_0.has_callables(var_0, *list_0)
    bool_1 = module_0.has_any_callables(str_0, *list_0)