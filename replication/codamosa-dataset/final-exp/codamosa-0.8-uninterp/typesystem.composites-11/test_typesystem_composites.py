# Automatically generated by Pynguin.
import typesystem.composites as module_0
import typesystem.fields as module_1

def test_case_0():
    pass

def test_case_1():
    never_match_0 = module_0.NeverMatch()

def test_case_2():
    list_0 = []
    one_of_0 = module_0.OneOf(list_0)

def test_case_3():
    list_0 = []
    all_of_0 = module_0.AllOf(list_0)

def test_case_4():
    int_0 = -232
    set_0 = {int_0, int_0, int_0, int_0}
    list_0 = []
    all_of_0 = module_0.AllOf(list_0)
    any_0 = all_of_0.validate(set_0)

def test_case_5():
    any_0 = module_1.Any()
    any_1 = [any_0]
    all_of_0 = module_0.AllOf(any_1)
    not_0 = module_0.Not(all_of_0)
    not_1 = module_0.Not(not_0)
    str_0 = 'abc'
    any_2 = not_1.validate(str_0)

def test_case_6():
    never_match_0 = module_0.NeverMatch()
    any_0 = module_1.Any()
    any_1 = [any_0]
    one_of_0 = module_0.OneOf(any_1)
    int_0 = 10
    field_0 = module_1.Field()
    list_0 = [field_0, field_0]
    dict_0 = {}
    all_of_0 = module_0.AllOf(list_0, **dict_0)
    var_0 = int_0
    any_2 = one_of_0.validate(int_0)