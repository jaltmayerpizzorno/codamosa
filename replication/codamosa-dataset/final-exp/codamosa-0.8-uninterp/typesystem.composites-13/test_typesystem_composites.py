# Automatically generated by Pynguin.
import typesystem.composites as module_0
import typesystem.fields as module_1

def test_case_0():
    pass

def test_case_1():
    dict_0 = {}
    never_match_0 = module_0.NeverMatch(**dict_0)

def test_case_2():
    field_0 = module_1.Field()
    list_0 = []
    all_of_0 = module_0.AllOf(list_0)
    any_0 = all_of_0.validate(field_0)

def test_case_3():
    field_0 = None
    if_then_else_0 = module_0.IfThenElse(field_0, field_0, field_0)

def test_case_4():
    any_0 = module_1.Any()
    if_then_else_0 = module_0.IfThenElse(any_0, any_0, any_0)
    any_1 = if_then_else_0.validate(if_then_else_0)

def test_case_5():
    any_0 = module_1.Any()
    any_1 = [any_0]
    bool_0 = True
    one_of_0 = module_0.OneOf(any_1)
    any_2 = any_0.serialize(any_1)
    any_3 = one_of_0.validate(bool_0)
    int_0 = 1
    int_1 = [int_0]
    any_4 = one_of_0.validate(int_1)

def test_case_6():
    never_match_0 = module_0.NeverMatch()
    not_0 = module_0.Not(never_match_0)
    bool_0 = True
    any_0 = not_0.validate(not_0, bool_0)

def test_case_7():
    int_0 = 17
    any_0 = module_1.Any()
    if_then_else_0 = module_0.IfThenElse(any_0)
    any_1 = if_then_else_0.validate(int_0)
    any_2 = module_1.Any()
    any_3 = module_1.Any()
    if_then_else_1 = module_0.IfThenElse(any_2, any_3)
    any_4 = if_then_else_1.validate(int_0)
    any_5 = module_1.Any()
    any_6 = module_1.Any()
    if_then_else_2 = module_0.IfThenElse(any_5, any_6)
    any_7 = if_then_else_2.validate(int_0)
    any_8 = module_1.Any()
    any_9 = module_1.Any()
    any_10 = module_1.Any()
    if_then_else_3 = module_0.IfThenElse(any_8, any_9, any_10)
    any_11 = if_then_else_3.validate(int_0)
    never_match_0 = module_0.NeverMatch()
    any_12 = module_1.Any()
    if_then_else_4 = module_0.IfThenElse(never_match_0, any_12)
    any_13 = if_then_else_4.validate(int_0)