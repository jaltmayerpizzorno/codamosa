# Automatically generated by Pynguin.
import mimesis.providers.choice as module_0

def test_case_0():
    pass

def test_case_1():
    choice_0 = module_0.Choice()

def test_case_2():
    choice_0 = module_0.Choice()
    list_0 = [choice_0, choice_0, choice_0, choice_0]
    var_0 = choice_0.__call__(list_0)

def test_case_3():
    str_0 = '_onh;\\{jL_?'
    int_0 = 1165
    choice_0 = module_0.Choice()
    var_0 = choice_0.__call__(str_0, int_0)

def test_case_4():
    choice_0 = module_0.Choice()
    str_0 = 'c'
    str_1 = [str_0, str_0, str_0]
    var_0 = choice_0.__call__(str_1)
    str_2 = [str_0, str_1, str_0]
    int_0 = 1
    var_1 = choice_0.__call__(str_2, int_0)
    str_3 = 'abc'
    int_1 = 2
    var_2 = choice_0.__call__(str_3, int_1)
    str_4 = 'aabbbccccddddd'
    int_2 = 4
    bool_0 = True
    var_3 = choice_0.__call__(str_4, int_2, bool_0)

def test_case_5():
    choice_0 = module_0.Choice()
    str_0 = 'a'
    str_1 = 'c'
    str_2 = [str_0, str_1, str_1]
    var_0 = choice_0.__call__(str_2)
    str_3 = [str_0, str_2, str_1]
    int_0 = 1
    var_1 = choice_0.__call__(str_3, int_0)
    str_4 = 'abc'
    int_1 = 2
    var_2 = choice_0.__call__(str_4, int_1)
    str_5 = 'aabbbccccddddd'
    int_2 = 4
    bool_0 = True
    var_3 = choice_0.__call__(str_5, int_2, bool_0)