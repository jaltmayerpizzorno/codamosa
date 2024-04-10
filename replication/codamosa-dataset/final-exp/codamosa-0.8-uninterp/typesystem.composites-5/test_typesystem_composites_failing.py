# Automatically generated by Pynguin.
import typesystem.composites as module_0
import typesystem.fields as module_1

def test_case_0():
    try:
        never_match_0 = module_0.NeverMatch()
        never_match_1 = [never_match_0, never_match_0, never_match_0]
        one_of_0 = module_0.OneOf(never_match_1)
        str_0 = 'negated'
        any_0 = one_of_0.validate(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        list_0 = []
        one_of_0 = module_0.OneOf(list_0)
        any_0 = one_of_0.validate(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        never_match_0 = module_0.NeverMatch()
        all_of_0 = None
        field_0 = module_1.Field()
        list_0 = [field_0]
        one_of_0 = module_0.OneOf(list_0)
        any_0 = one_of_0.validate(all_of_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'Expecting property name enclosed in double quotes'
        field_0 = module_1.Field(description=str_0)
        not_0 = module_0.Not(field_0)
        str_1 = '5-'
        field_1 = module_1.Field(description=str_1)
        list_0 = [field_1, field_1, field_1, field_1]
        all_of_0 = module_0.AllOf(list_0)
        any_0 = all_of_0.validate(not_0)
    except BaseException:
        pass

def test_case_4():
    try:
        field_0 = None
        if_then_else_0 = module_0.IfThenElse(field_0)
        not_0 = module_0.Not(field_0)
        str_0 = 'oneOf'
        list_0 = []
        never_match_0 = module_0.NeverMatch()
        bool_0 = None
        dict_0 = {str_0: field_0}
        all_of_0 = module_0.AllOf(list_0)
        any_0 = all_of_0.validate(list_0, bool_0)
        one_of_0 = module_0.OneOf(list_0, **dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        any_0 = module_1.Any()
        not_0 = module_0.Not(any_0)
        bool_0 = False
        any_1 = not_0.validate(bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        field_0 = module_1.Field(allow_null=bool_0)
        if_then_else_0 = module_0.IfThenElse(field_0)
        field_1 = None
        str_0 = 'l7mqZr\t5'
        never_match_0 = module_0.NeverMatch()
        dict_0 = {}
        dict_1 = {str_0: str_0, str_0: dict_0}
        not_0 = module_0.Not(field_1, **dict_1)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'never'
        never_match_0 = module_0.NeverMatch()
        bool_0 = True
        list_0 = []
        all_of_0 = module_0.AllOf(list_0)
        never_match_1 = [never_match_0, all_of_0, all_of_0, never_match_0, bool_0]
        one_of_0 = module_0.OneOf(never_match_1)
        not_0 = module_0.Not(never_match_1)
        field_0 = module_1.Field(title=str_0, default=never_match_1)
        if_then_else_0 = module_0.IfThenElse(field_0, field_0, field_0)
        any_0 = one_of_0.validate(one_of_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'never'
        never_match_0 = module_0.NeverMatch()
        list_0 = []
        all_of_0 = module_0.AllOf(list_0)
        str_1 = 'Gl\\Jp'
        str_2 = 'allow_null'
        dict_0 = {str_1: str_0, str_0: str_0, str_0: list_0, str_2: list_0}
        never_match_1 = module_0.NeverMatch(**dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        any_0 = module_1.Any()
        not_0 = module_0.Not(any_0)
        not_1 = module_0.Not(any_0)
        any_1 = module_1.Any()
        not_2 = module_0.Not(any_1)
        if_then_else_0 = module_0.IfThenElse(not_0, not_1, not_2)
        int_0 = 1
        any_2 = if_then_else_0.validate(int_0)
    except BaseException:
        pass

def test_case_10():
    try:
        any_0 = module_1.Any()
        list_0 = []
        str_0 = "`DCHCbWXL4![Gu2'ruF'"
        field_0 = module_1.Field(description=str_0)
        not_0 = module_0.Not(field_0)
        if_then_else_0 = module_0.IfThenElse(field_0, field_0)
        one_of_0 = module_0.OneOf(list_0)
        str_1 = 'allow_null'
        str_2 = ',7.'
        dict_0 = {str_1: field_0, str_2: if_then_else_0}
        all_of_0 = module_0.AllOf(list_0, **dict_0)
    except BaseException:
        pass