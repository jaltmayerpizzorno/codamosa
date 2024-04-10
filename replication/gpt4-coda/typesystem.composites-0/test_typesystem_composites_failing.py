# Automatically generated by Pynguin.
import typesystem.composites as module_0
import typesystem.fields as module_1

def test_case_0():
    try:
        never_match_0 = module_0.NeverMatch()
        field_0 = module_1.Field()
        field_1 = module_1.Field()
        if_then_else_0 = module_0.IfThenElse(never_match_0, field_0, field_1)
        str_0 = 'test_value'
        any_0 = if_then_else_0.validate(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = ()
        field_0 = module_1.Field()
        list_0 = [field_0, field_0]
        one_of_0 = module_0.OneOf(list_0)
        any_0 = one_of_0.validate(tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        all_of_0 = module_0.AllOf(list_0)
        all_of_1 = module_0.AllOf(list_0)
        any_0 = all_of_1.validate(list_0)
        bool_0 = False
        one_of_0 = module_0.OneOf(list_0)
        any_1 = one_of_0.validate(bool_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        never_match_0 = module_0.NeverMatch()
        not_0 = module_0.Not(never_match_0)
        str_0 = 'any value'
        any_0 = not_0.validate(str_0)
        field_0 = module_1.Field()
        not_1 = module_0.Not(field_0)
        list_0 = [field_0, field_0]
        one_of_0 = module_0.OneOf(list_0)
        all_of_0 = module_0.AllOf(list_0)
        any_1 = all_of_0.validate(not_1)
    except BaseException:
        pass

def test_case_4():
    try:
        field_0 = module_1.Field()
        str_0 = 'VLwGk4\x0b'
        str_1 = 'z$p)e@_,o\nwR-eMN'
        dict_0 = {str_0: str_0, str_1: str_0, str_1: field_0}
        not_0 = module_0.Not(field_0, **dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        list_0 = None
        one_of_0 = module_0.OneOf(list_0)
        bool_0 = True
        field_0 = module_1.Field(default=bool_0)
        if_then_else_0 = module_0.IfThenElse(field_0)
        any_0 = if_then_else_0.validate(one_of_0)
    except BaseException:
        pass

def test_case_6():
    try:
        any_0 = module_1.Any()
        never_match_0 = module_0.NeverMatch()
        never_match_1 = [never_match_0, never_match_0]
        one_of_0 = module_0.OneOf(never_match_1)
        str_0 = 'test'
        any_1 = one_of_0.validate(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        any_0 = module_1.Any()
        never_match_0 = module_0.NeverMatch()
        not_0 = module_0.Not(any_0)
        str_0 = 'any value'
        any_1 = not_0.validate(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        any_0 = module_1.Any()
        str_0 = 'test value'
        any_1 = module_1.Any()
        any_2 = [any_0, any_1]
        one_of_0 = module_0.OneOf(any_2)
        bool_0 = False
        field_0 = module_1.Field(title=str_0, description=str_0, allow_null=bool_0)
        bool_1 = True
        any_3 = one_of_0.validate(any_0, bool_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'k$H:b3.E<'
        str_1 = 'b>_'
        bool_0 = False
        field_0 = module_1.Field(title=str_1, description=str_0, default=str_0, allow_null=bool_0)
        list_0 = [field_0]
        str_2 = '__(f@~'
        str_3 = 'none'
        str_4 = 'allow_null'
        dict_0 = {str_2: str_0, str_3: bool_0, str_4: field_0}
        one_of_0 = module_0.OneOf(list_0)
        all_of_0 = module_0.AllOf(list_0, **dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'k$H:b3.E<'
        bool_0 = False
        field_0 = module_1.Field(title=str_0, description=str_0, default=str_0, allow_null=bool_0)
        str_1 = '__(f@~'
        str_2 = 'none'
        str_3 = 'allow_null'
        dict_0 = {str_1: str_0, str_2: bool_0, str_3: field_0}
        str_4 = 'unique_items'
        str_5 = 'AY\x0cOA5GIQvX'
        field_1 = module_1.Field(title=str_4, description=str_5)
        never_match_0 = module_0.NeverMatch()
        not_0 = module_0.Not(field_1)
        field_2 = module_1.Field()
        never_match_1 = module_0.NeverMatch(**dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        list_0 = []
        all_of_0 = module_0.AllOf(list_0)
        any_0 = all_of_0.validate(list_0)
        field_0 = module_1.Field()
        any_1 = all_of_0.validate(list_0)
        if_then_else_0 = module_0.IfThenElse(field_0)
        any_2 = all_of_0.validate(any_0)
        one_of_0 = module_0.OneOf(list_0)
        str_0 = 'allow_ba$~'
        dict_0 = {}
        never_match_0 = module_0.NeverMatch()
        any_3 = all_of_0.validate(if_then_else_0)
        one_of_1 = module_0.OneOf(list_0)
        not_0 = module_0.Not(field_0)
        list_1 = [field_0, field_0, field_0, field_0]
        never_match_1 = module_0.NeverMatch()
        one_of_2 = module_0.OneOf(list_1)
        never_match_2 = module_0.NeverMatch()
        all_of_1 = module_0.AllOf(list_1)
        one_of_3 = module_0.OneOf(list_0)
        str_1 = ' for '
        str_2 = 'allow_null'
        if_then_else_1 = module_0.IfThenElse(field_0, field_0, field_0, **dict_0)
        dict_1 = {str_1: one_of_0, str_2: str_2, str_2: str_2, str_0: one_of_3}
        if_then_else_2 = module_0.IfThenElse(field_0, field_0, **dict_1)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'k$H:b3.E<'
        str_1 = 'b>_'
        bool_0 = False
        field_0 = module_1.Field(title=str_1, description=str_0, default=str_0, allow_null=bool_0)
        list_0 = [field_0]
        str_2 = 'none'
        str_3 = 'allow_null'
        dict_0 = {str_3: str_0, str_2: bool_0, str_3: field_0}
        one_of_0 = module_0.OneOf(list_0)
        list_1 = [field_0]
        one_of_1 = module_0.OneOf(list_1, **dict_0)
    except BaseException:
        pass