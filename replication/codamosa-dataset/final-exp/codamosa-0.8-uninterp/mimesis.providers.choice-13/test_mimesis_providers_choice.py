# Automatically generated by Pynguin.
import mimesis.providers.choice as module_0

def test_case_0():
    choice_0 = module_0.Choice()

def test_case_1():
    choice_0 = module_0.Choice()
    str_0 = 'b'
    int_0 = 5
    var_0 = choice_0.__call__(str_0, int_0)

def test_case_2():
    str_0 = 'ce'
    str_1 = (str_0, str_0, str_0)
    choice_0 = module_0.Choice()
    int_0 = 1
    var_0 = choice_0.__call__(str_1, int_0)
    bool_0 = True
    var_1 = choice_0.__call__(str_1, int_0, bool_0)

def test_case_3():
    str_0 = 'w?o~]M+`c?]'
    list_0 = [str_0, str_0, str_0, str_0]
    bool_0 = False
    choice_0 = module_0.Choice()
    var_0 = choice_0.__call__(list_0, bool_0)
    int_0 = 1144
    choice_1 = module_0.Choice()
    var_1 = choice_1.__call__(str_0, int_0)

def test_case_4():
    str_0 = 'w?o~]M+`c?]'
    list_0 = [str_0, str_0, str_0, str_0]
    bool_0 = True
    choice_0 = module_0.Choice()
    var_0 = choice_0.__call__(list_0, bool_0)

def test_case_5():
    str_0 = 'ce'
    choice_0 = module_0.Choice()
    int_0 = 1
    bool_0 = True
    var_0 = choice_0.__call__(str_0, int_0, bool_0)

def test_case_6():
    choice_0 = module_0.Choice()
    str_0 = 'a'
    str_1 = 'b'
    str_2 = 'c'
    str_3 = [str_0, str_1, str_2]
    var_0 = choice_0.__call__(str_3)
    str_4 = [str_0, str_1, str_2]
    int_0 = 1
    var_1 = choice_0.__call__(str_4, int_0)
    str_5 = 'abc'
    int_1 = 2
    var_2 = choice_0.__call__(str_5, int_1)
    str_6 = (str_0, str_1, str_2)
    int_2 = 5
    var_3 = choice_0.__call__(str_6, int_2)
    str_7 = 'aabbbccccddddd'
    int_3 = 4
    bool_0 = True
    var_4 = choice_0.__call__(str_7, int_3, bool_0)