# Automatically generated by Pynguin.
import mimesis.providers.choice as module_0

def test_case_0():
    try:
        choice_0 = module_0.Choice()
        int_0 = 1318
        float_0 = 1102.336272920441
        tuple_0 = (choice_0, float_0, int_0)
        bool_0 = True
        str_0 = 'Field «{}» is not supported.'
        var_0 = choice_0.__call__(str_0)
        var_1 = choice_0.__call__(tuple_0, bool_0)
        bytes_0 = b')X\xa5\xa7J\xccP0'
        bool_1 = True
        var_2 = choice_0.__call__(bytes_0, int_0, bool_1)
    except BaseException:
        pass

def test_case_1():
    try:
        choice_0 = module_0.Choice()
        list_0 = [choice_0, choice_0]
        int_0 = -3271
        float_0 = 1102.2275115839277
        tuple_0 = (choice_0, float_0, int_0)
        bool_0 = True
        var_0 = choice_0.__call__(tuple_0, bool_0)
        choice_1 = module_0.Choice()
        var_1 = choice_1.__call__(list_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        choice_0 = module_0.Choice()
        str_0 = 'q'
        dict_0 = {str_0: choice_0}
        int_0 = -416
        var_0 = choice_0.__call__(dict_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        choice_0 = module_0.Choice()
        none_type_0 = None
        list_0 = [choice_0, choice_0]
        int_0 = 1334
        choice_1 = module_0.Choice()
        var_0 = choice_1.__call__(list_0, int_0)
        var_1 = choice_0.__call__(none_type_0)
    except BaseException:
        pass

def test_case_4():
    try:
        choice_0 = module_0.Choice()
        list_0 = []
        var_0 = choice_0.__call__(list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        choice_0 = module_0.Choice()
        list_0 = [choice_0, choice_0, choice_0, choice_0]
        int_0 = 1334
        float_0 = 1101.9
        tuple_0 = (choice_0, float_0, int_0)
        bool_0 = True
        var_0 = choice_0.__call__(tuple_0, bool_0)
        choice_1 = module_0.Choice()
        int_1 = None
        var_1 = choice_1.__call__(list_0, int_1)
    except BaseException:
        pass

def test_case_6():
    try:
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
        var_2 = choice_0.__call__(str_5, int_0)
        str_6 = (str_0, str_1, str_2)
        int_1 = 5
        var_3 = choice_0.__call__(str_6, int_1)
        str_7 = 'aabbbccccddddd'
        int_2 = 4
        bool_0 = True
        var_4 = choice_0.__call__(str_7, int_2, bool_0)
        str_8 = 'a'
        str_9 = 'b'
        str_10 = 'c'
        str_11 = (str_8, str_9, str_10)
        var_5 = choice_0.__call__(str_11, str_8)
    except BaseException:
        pass