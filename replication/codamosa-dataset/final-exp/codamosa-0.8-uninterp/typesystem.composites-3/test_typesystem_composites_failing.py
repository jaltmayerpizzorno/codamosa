# Automatically generated by Pynguin.
import typesystem.composites as module_0
import typesystem.fields as module_1

def test_case_0():
    try:
        bytes_0 = b'\x1c(r#\x15\t'
        bool_0 = False
        never_match_0 = module_0.NeverMatch()
        any_0 = never_match_0.validate(bytes_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        one_of_0 = module_0.OneOf(list_0)
        any_0 = one_of_0.validate(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        any_0 = module_1.Any()
        any_1 = [any_0, any_0]
        one_of_0 = module_0.OneOf(any_1)
        var_0 = None
        any_2 = one_of_0.validate(var_0)
    except BaseException:
        pass

def test_case_3():
    try:
        never_match_0 = module_0.NeverMatch()
        field_0 = module_1.Field()
        list_0 = [field_0, field_0]
        all_of_0 = module_0.AllOf(list_0)
        any_0 = all_of_0.validate(never_match_0)
    except BaseException:
        pass

def test_case_4():
    try:
        any_0 = module_1.Any()
        not_0 = module_0.Not(any_0)
        any_1 = not_0.validate(any_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Ttv]+tU$B;G,/TS_eU\'"'
        field_0 = module_1.Field(title=str_0, description=str_0)
        dict_0 = {str_0: str_0, str_0: str_0, str_0: field_0, str_0: field_0}
        if_then_else_0 = module_0.IfThenElse(field_0, **dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'hello'
        field_0 = module_1.Field()
        if_then_else_0 = module_0.IfThenElse(field_0, field_0, field_0)
        list_0 = [field_0]
        dict_0 = {str_0: field_0, str_0: if_then_else_0, str_0: str_0}
        all_of_0 = module_0.AllOf(list_0, **dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        never_match_0 = module_0.NeverMatch()
        list_0 = []
        one_of_0 = module_0.OneOf(list_0)
        all_of_0 = module_0.AllOf(list_0)
        any_0 = all_of_0.validate(never_match_0)
        bool_0 = True
        any_1 = never_match_0.validate(never_match_0, bool_0)
    except BaseException:
        pass