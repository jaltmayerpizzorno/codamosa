# Automatically generated by Pynguin.
import typesystem.composites as module_0
import typesystem.fields as module_1

def test_case_0():
    try:
        str_0 = 'Must have no more than {max_properties} properties.'
        never_match_0 = module_0.NeverMatch()
        any_0 = never_match_0.validate(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        any_0 = module_1.Any()
        any_1 = [any_0, any_0]
        one_of_0 = module_0.OneOf(any_1)
        str_0 = 'foo'
        any_2 = one_of_0.validate(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 2340.22621
        list_0 = []
        one_of_0 = module_0.OneOf(list_0)
        any_0 = one_of_0.validate(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'date-time'
        field_0 = None
        dict_0 = {str_0: str_0}
        not_0 = module_0.Not(field_0, **dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        any_0 = module_1.Any()
        not_0 = module_0.Not(any_0)
        bool_0 = False
        any_1 = not_0.validate(bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ".\\:s]`/^'>)oz*D"
        bool_0 = False
        field_0 = module_1.Field(description=str_0, default=str_0, allow_null=bool_0)
        list_0 = [field_0, field_0, field_0, field_0]
        all_of_0 = module_0.AllOf(list_0)
        field_1 = module_1.Field()
        if_then_else_0 = module_0.IfThenElse(field_1)
        any_0 = if_then_else_0.validate(all_of_0, bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'if_clause'
        never_match_0 = module_0.NeverMatch()
        str_1 = 'then_clause'
        never_match_1 = module_0.NeverMatch()
        str_2 = 'else_clause'
        never_match_2 = module_0.NeverMatch()
        if_then_else_0 = module_0.IfThenElse(never_match_0, never_match_1, never_match_2)
        int_0 = 1
        any_0 = if_then_else_0.validate(int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'ojh)Vmr7j:<\\'
        bool_0 = None
        field_0 = module_1.Field(title=str_0, allow_null=bool_0)
        dict_0 = {}
        if_then_else_0 = module_0.IfThenElse(field_0, field_0, **dict_0)
        bool_1 = False
        str_1 = '(?P<year>\\d{4})-(?P<month>\\d{1,2})-(?P<day>\\d{1,2})[T ](?P<hour>\\d{1,2}):(?P<minute>\\d{1,2})(?::(?P<second>\\d{1,2})(?:\\.(?P<microsecond>\\d{1,6})\\d{0,6})?)?(?P<tzinfo>Z|[+-]\\d{2}(?::?\\d{2})?)?$'
        field_1 = module_1.Field(title=str_1, description=str_1, allow_null=bool_1)
        dict_1 = {}
        not_0 = module_0.Not(field_1, **dict_1)
        list_0 = [field_1]
        all_of_0 = module_0.AllOf(list_0, **dict_1)
        any_0 = all_of_0.validate(bool_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'allow_null'
        bool_0 = False
        field_0 = module_1.Field(title=str_0, allow_null=bool_0)
        list_0 = [field_0, field_0, field_0]
        str_1 = 'gE'
        dict_0 = {str_0: list_0, str_0: field_0, str_1: bool_0}
        all_of_0 = module_0.AllOf(list_0, **dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'allow_null'
        bool_0 = False
        field_0 = module_1.Field(title=str_0, allow_null=bool_0)
        if_then_else_0 = module_0.IfThenElse(field_0)
        dict_0 = {str_0: if_then_else_0}
        never_match_0 = module_0.NeverMatch(**dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'allow_null'
        bool_0 = False
        field_0 = module_1.Field(title=str_0, allow_null=bool_0)
        list_0 = [field_0, field_0, field_0, field_0]
        if_then_else_0 = module_0.IfThenElse(field_0)
        dict_0 = {str_0: if_then_else_0}
        one_of_0 = module_0.OneOf(list_0, **dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        any_0 = module_1.Any()
        never_match_0 = module_0.NeverMatch()
        any_1 = [any_0, any_0, never_match_0]
        one_of_0 = module_0.OneOf(any_1)
        any_2 = one_of_0.validate(any_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'allow_null'
        bool_0 = False
        field_0 = module_1.Field(title=str_0, allow_null=bool_0)
        if_then_else_0 = module_0.IfThenElse(field_0)
        dict_0 = {str_0: if_then_else_0}
        not_0 = module_0.Not(field_0, **dict_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'allow_null'
        bool_0 = False
        field_0 = module_1.Field(allow_null=bool_0)
        dict_0 = {str_0: field_0, str_0: bool_0, str_0: bool_0, str_0: field_0}
        if_then_else_0 = module_0.IfThenElse(field_0, field_0, **dict_0)
    except BaseException:
        pass