# Automatically generated by Pynguin.
import mimesis.providers.choice as module_0

def test_case_0():
    choice_0 = module_0.Choice()
    choice_1 = module_0.Choice()

def test_case_1():
    str_0 = 'Bugatti'
    bool_0 = True
    choice_0 = module_0.Choice()
    var_0 = choice_0.__call__(str_0, bool_0)

def test_case_2():
    choice_0 = module_0.Choice()
    choice_1 = module_0.Choice()
    choice_2 = module_0.Choice()
    str_0 = None
    tuple_0 = (str_0,)
    int_0 = 1668
    var_0 = choice_1.__call__(tuple_0, int_0)