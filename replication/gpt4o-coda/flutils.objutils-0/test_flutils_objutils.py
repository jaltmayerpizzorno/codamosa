# Automatically generated by Pynguin.
import flutils.objutils as module_0

def test_case_0():
    str_0 = 'A custom :obj:`loader <importlib.abc.Loader>` that is used in the\n    execution of cherry-picking-modules.\n    '
    bool_0 = module_0.is_subclass_of_any(str_0)

def test_case_1():
    str_0 = 'A custom :obj:`loader <importlib.abc.Loader>` that is used in the\n    execution of cherry-picking-modules.\n    '
    bool_0 = module_0.has_any_attrs(str_0)

def test_case_2():
    str_0 = 'count'
    list_0 = [str_0, str_0]
    bool_0 = module_0.has_any_callables(list_0, *list_0)

def test_case_3():
    list_0 = []
    bool_0 = module_0.has_any_callables(list_0)

def test_case_4():
    str_0 = ']fEo'
    bool_0 = module_0.has_callables(str_0)

def test_case_5():
    str_0 = 'count'
    list_0 = [str_0]
    bool_0 = module_0.has_callables(str_0, *list_0)

def test_case_6():
    int_0 = -1728
    str_0 = "'mc].=R"
    list_0 = [str_0, str_0]
    bool_0 = module_0.has_attrs(int_0, *list_0)

def test_case_7():
    str_0 = ",ENs'K=txG{o?`?"
    str_1 = 'h&4\\@NYPFL PxJXSDw)\\'
    str_2 = '`ck1Pth;\nea'
    list_0 = [str_0, str_1, str_2]
    bool_0 = module_0.has_callables(str_2)
    bool_1 = module_0.has_any_callables(list_0, *list_0)
    bool_2 = module_0.has_any_attrs(str_0)
    bool_3 = module_0.has_attrs(bool_1)
    bool_4 = module_0.has_any_attrs(bool_2)
    bool_5 = module_0.has_callables(bool_4, *list_0)

def test_case_8():
    str_0 = '1NY\x0cV9pM;b+MYZ1T'
    bool_0 = module_0.is_list_like(str_0)

def test_case_9():
    set_0 = set()
    bool_0 = module_0.is_list_like(set_0)

def test_case_10():
    str_0 = '([K\n%'
    bool_0 = module_0.has_attrs(str_0)
    str_1 = 'p3jL@VM63HJO'
    str_2 = 'rWR_bE\t"P'
    str_3 = '9(]tV;bk7P7,y0=\t'
    list_0 = [str_2, str_3]
    bool_1 = module_0.has_any_callables(str_1, *list_0)