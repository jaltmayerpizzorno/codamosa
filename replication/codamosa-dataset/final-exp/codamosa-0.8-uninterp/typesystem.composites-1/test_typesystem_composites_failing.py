# Automatically generated by Pynguin.
import typesystem.fields as module_0
import typesystem.composites as module_1

def test_case_0():
    try:
        field_0 = module_0.Field()
        if_then_else_0 = module_1.IfThenElse(field_0)
        dict_0 = {if_then_else_0: field_0, field_0: field_0}
        never_match_0 = module_1.NeverMatch()
        any_0 = never_match_0.validate(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        one_of_0 = module_1.OneOf(list_0)
        any_0 = one_of_0.validate(one_of_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'nP4\x07\xd8\x87\x88\xedY'
        field_0 = module_0.Field()
        list_0 = [field_0, field_0]
        one_of_0 = module_1.OneOf(list_0)
        any_0 = one_of_0.validate(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = None
        all_of_0 = module_1.AllOf(list_0)
        field_0 = module_0.Field()
        if_then_else_0 = module_1.IfThenElse(field_0)
        any_0 = if_then_else_0.validate(all_of_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        field_0 = module_0.Field(allow_null=bool_0)
        not_0 = module_1.Not(field_0)
        list_0 = [not_0, not_0, not_0]
        str_0 = 'choices'
        field_1 = module_0.Field(description=str_0)
        list_1 = [field_1, field_1]
        all_of_0 = module_1.AllOf(list_1)
        any_0 = all_of_0.validate(list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        not_0 = None
        str_0 = '-vt;[-6(l(vm=aF`a-{'
        field_0 = module_0.Field(description=str_0)
        not_1 = module_1.Not(field_0)
        any_0 = not_1.validate(not_0)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = {}
        never_match_0 = module_1.NeverMatch(**dict_0)
        list_0 = []
        all_of_0 = module_1.AllOf(list_0)
        any_0 = module_0.Any()
        any_1 = [never_match_0, all_of_0, any_0]
        one_of_0 = module_1.OneOf(any_1)
        validation_result_0 = any_0.validate_or_error(any_1)
        field_0 = module_0.Field(default=never_match_0)
        any_2 = all_of_0.validate(dict_0)
        if_then_else_0 = module_1.IfThenElse(field_0, field_0)
        field_1 = module_0.Field()
        not_0 = module_1.Not(field_0)
        if_then_else_1 = module_1.IfThenElse(field_1, field_0)
        any_3 = one_of_0.validate(list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        any_0 = module_0.Any()
        not_0 = module_1.Not(any_0)
        str_0 = ''
        bool_0 = False
        any_1 = not_0.validate(str_0, bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'ca\x0b29[$w,2/G?z#'
        field_0 = module_0.Field(title=str_0, default=str_0)
        dict_0 = {}
        not_0 = module_1.Not(field_0, **dict_0)
        any_0 = module_0.Any()
        any_1 = module_0.Any()
        if_then_else_0 = module_1.IfThenElse(any_0, any_1)
        any_2 = module_0.Any()
        if_then_else_1 = module_1.IfThenElse(if_then_else_0, any_2)
        int_0 = 1
        any_3 = if_then_else_1.validate(int_0)
        any_4 = module_0.Any()
        any_5 = module_0.Any()
        any_6 = module_0.Any()
        list_0 = None
        all_of_0 = module_1.AllOf(list_0)
        not_1 = module_1.Not(field_0)
        any_7 = module_0.Any()
        str_1 = 'allow_null'
        str_2 = ' wI/l'
        dict_1 = {str_1: if_then_else_0, str_2: str_1}
        never_match_0 = module_1.NeverMatch(**dict_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'name{)y'
        str_1 = 'one_of'
        str_2 = 'allow_null'
        str_3 = 'testOneOf'
        any_0 = module_0.Any()
        any_1 = [any_0]
        bool_0 = True
        var_0 = {str_0: str_3, str_1: any_1, str_2: bool_0}
        one_of_0 = module_1.OneOf(**var_0)
    except BaseException:
        pass