# Automatically generated by Pynguin.
import typesystem.composites as module_0

def test_case_0():
    pass

def test_case_1():
    never_match_0 = module_0.NeverMatch()

def test_case_2():
    never_match_0 = module_0.NeverMatch()
    not_0 = module_0.Not(never_match_0)
    int_0 = 1
    any_0 = not_0.validate(int_0)

def test_case_3():
    list_0 = []
    all_of_0 = module_0.AllOf(list_0)

def test_case_4():
    field_0 = None
    list_0 = [field_0, field_0, field_0, field_0]
    all_of_0 = module_0.AllOf(list_0)
    not_0 = module_0.Not(field_0)