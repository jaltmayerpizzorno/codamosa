# Automatically generated by Pynguin.
import mimesis.providers.choice as module_0

def test_case_0():
    try:
        choice_0 = module_0.Choice()
        bool_0 = True
        bytes_0 = b'n\x18ra\x8bQ\x92^g}G\x91\x1bbR\xef\x9e'
        var_0 = choice_0.__call__(bytes_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        choice_0 = module_0.Choice()
        bytes_0 = b'r\x8c\x83w\x96\x0c\xc2\x1e\xda\xb4\x05Z\x1f-\xaca5'
        choice_1 = module_0.Choice()
        var_0 = choice_1.__call__(bytes_0)
        str_0 = 'ER7tWW`p'
        var_1 = choice_0.__call__(str_0)
        int_0 = -2130
        var_2 = choice_0.__call__(str_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        choice_0 = module_0.Choice()
        bool_0 = None
        var_0 = choice_0.__call__(bool_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        optional_0 = None
        int_0 = -2582
        list_0 = []
        choice_0 = module_0.Choice(*list_0)
        var_0 = choice_0.__call__(optional_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0, dict_0]
        list_1 = []
        choice_0 = module_0.Choice(*list_1)
        var_0 = choice_0.__call__(list_0)
        str_0 = 'J>mB;+c;o\x0b5\n>Ohj#'
        int_0 = 932
        var_1 = choice_0.__call__(str_0, int_0)
        list_2 = []
        var_2 = choice_0.__call__(list_2)
    except BaseException:
        pass

def test_case_5():
    try:
        choice_0 = module_0.Choice()
        str_0 = '^'
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
        int_3 = 5148
        bool_0 = True
        var_4 = choice_0.__call__(str_7, int_3, bool_0)
    except BaseException:
        pass