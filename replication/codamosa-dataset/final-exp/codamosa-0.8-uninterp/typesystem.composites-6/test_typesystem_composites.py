# Automatically generated by Pynguin.
import typesystem.composites as module_0
import typesystem.fields as module_1

def test_case_0():
    pass

def test_case_1():
    never_match_0 = module_0.NeverMatch()

def test_case_2():
    never_match_0 = module_0.NeverMatch()
    not_0 = module_0.Not(never_match_0)
    str_0 = 'a'
    any_0 = not_0.validate(str_0)

def test_case_3():
    field_0 = None
    list_0 = [field_0, field_0, field_0]
    all_of_0 = module_0.AllOf(list_0)

def test_case_4():
    never_match_0 = module_0.NeverMatch()
    list_0 = []
    all_of_0 = module_0.AllOf(list_0)
    any_0 = all_of_0.validate(never_match_0)
    one_of_0 = module_0.OneOf(list_0)

def test_case_5():
    str_0 = '\n\t4G#Q:6=J44B[L'
    field_0 = module_1.Field(title=str_0)
    if_then_else_0 = module_0.IfThenElse(field_0)
    field_1 = module_1.Field()
    list_0 = [field_1, field_1]
    all_of_0 = module_0.AllOf(list_0)
    not_0 = module_0.Not(field_1)

def test_case_6():
    str_0 = 'if_clause'
    any_0 = module_1.Any()
    str_1 = 'then_clause'
    any_1 = module_1.Any()
    if_then_else_0 = module_0.IfThenElse(any_0, any_1)
    int_0 = 1
    any_2 = if_then_else_0.validate(int_0)

def test_case_7():
    any_0 = module_1.Any()
    any_1 = [any_0]
    one_of_0 = module_0.OneOf(any_1)
    any_2 = module_1.Any()
    any_3 = [any_2]
    one_of_1 = module_0.OneOf(any_3)
    any_4 = module_1.Any()
    any_5 = [any_4]
    one_of_2 = module_0.OneOf(any_5)
    if_then_else_0 = module_0.IfThenElse(one_of_0, one_of_1, one_of_2)
    int_0 = 1
    any_6 = if_then_else_0.validate(int_0)

def test_case_8():
    any_0 = module_1.Any()
    any_1 = [any_0, any_0]
    one_of_0 = module_0.OneOf(any_1)
    any_2 = module_1.Any()
    any_3 = [any_2]
    one_of_1 = module_0.OneOf(any_3)
    var_0 = {}
    any_4 = one_of_1.validate(var_0)

def test_case_9():
    any_0 = module_1.Any()
    any_1 = [any_0, any_0]
    one_of_0 = module_0.OneOf(any_1)
    any_2 = module_1.Any()
    any_3 = [any_2]
    one_of_1 = module_0.OneOf(any_3)
    any_4 = module_1.Any()
    any_5 = [any_4]
    one_of_2 = module_0.OneOf(any_5)
    if_then_else_0 = module_0.IfThenElse(one_of_0, one_of_1, one_of_2)
    int_0 = 1
    any_6 = if_then_else_0.validate(int_0)