# Automatically generated by Pynguin.
import typesystem.composites as module_0
import typesystem.fields as module_1

def test_case_0():
    try:
        list_0 = []
        bool_0 = True
        never_match_0 = module_0.NeverMatch()
        any_0 = never_match_0.validate(list_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        if_then_else_0 = None
        list_0 = []
        one_of_0 = module_0.OneOf(list_0)
        any_0 = one_of_0.validate(if_then_else_0)
    except BaseException:
        pass

def test_case_2():
    try:
        never_match_0 = module_0.NeverMatch()
        field_0 = None
        list_0 = [field_0, field_0, field_0, field_0]
        one_of_0 = module_0.OneOf(list_0)
        any_0 = one_of_0.validate(never_match_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'u'
        field_0 = module_1.Field(default=str_0)
        list_0 = None
        one_of_0 = module_0.OneOf(list_0)
        list_1 = [field_0, field_0]
        all_of_0 = module_0.AllOf(list_1)
        any_0 = all_of_0.validate(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 1387
        str_0 = '>\tgUb{0'
        list_0 = []
        dict_0 = {}
        list_1 = []
        list_2 = [list_1, list_1, int_0, list_0]
        bool_0 = False
        all_of_0 = module_0.AllOf(list_0)
        any_0 = all_of_0.validate(list_2, bool_0)
        one_of_0 = module_0.OneOf(list_0, **dict_0)
        any_1 = one_of_0.validate(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        any_0 = module_1.Any()
        not_0 = module_0.Not(any_0)
        any_1 = not_0.validate(not_0)
    except BaseException:
        pass

def test_case_6():
    try:
        never_match_0 = module_0.NeverMatch()
        never_match_1 = module_0.NeverMatch()
        never_match_2 = module_0.NeverMatch()
        if_then_else_0 = module_0.IfThenElse(never_match_0, never_match_1, never_match_2)
        var_0 = None
        bool_0 = False
        any_0 = if_then_else_0.validate(var_0, bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        never_match_0 = module_0.NeverMatch()
        never_match_1 = module_0.NeverMatch()
        never_match_2 = [never_match_0, never_match_1]
        one_of_0 = module_0.OneOf(never_match_2)
        str_0 = 'nothing'
        any_0 = one_of_0.validate(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        any_0 = module_1.Any()
        any_1 = [any_0]
        one_of_0 = module_0.OneOf(any_1)
        str_0 = 'somevalue'
        any_2 = one_of_0.validate(str_0)
        any_3 = module_1.Any()
        any_4 = module_1.Any()
        any_5 = [any_3, any_4]
        one_of_1 = module_0.OneOf(any_5)
        str_1 = 'somevalue'
        any_6 = one_of_1.validate(str_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'allow_null'
        field_0 = module_1.Field(title=str_0, default=str_0)
        str_1 = "`HY'j\\C G$ZU!iH#%k\tx"
        dict_0 = {str_0: field_0, str_1: field_0, str_1: field_0}
        if_then_else_0 = module_0.IfThenElse(field_0, field_0, **dict_0)
    except BaseException:
        pass