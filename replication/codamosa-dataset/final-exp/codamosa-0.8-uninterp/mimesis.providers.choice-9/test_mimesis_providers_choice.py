# Automatically generated by Pynguin.
import mimesis.providers.choice as module_0

def test_case_0():
    choice_0 = module_0.Choice()

def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    tuple_0 = (list_0,)
    int_0 = 1347
    choice_0 = module_0.Choice()
    var_0 = choice_0.__call__(tuple_0, int_0, bool_0)
    choice_1 = module_0.Choice()

def test_case_2():
    choice_0 = module_0.Choice()
    str_0 = 'a'
    str_1 = 'b'
    str_2 = 'c'
    str_3 = 'd'
    str_4 = 'e'
    str_5 = [str_0, str_1, str_2, str_3, str_4]
    int_0 = 3
    bool_0 = True
    var_0 = choice_0.__call__(str_5, int_0, bool_0)